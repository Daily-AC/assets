#!/usr/bin/env python3

import hashlib
import json
import math
from pathlib import Path

import mlx.core as mx
import numpy as np
from mlx_audio.audio_io import write as audio_write
from mlx_audio.tts.utils import load_model


PROJECT_DIR = Path(__file__).resolve().parent.parent
REQUEST_PATH = PROJECT_DIR / "qwen_voice_request.json"
AUDIO_META_PATH = PROJECT_DIR / "audio_meta.json"
ENGINE_META_PATH = PROJECT_DIR / "audio_engine_meta.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def trim_audio(audio: np.ndarray, sample_rate: int, threshold: float, margin_s: float) -> np.ndarray:
    audio = np.asarray(audio, dtype=np.float32).reshape(-1)
    active = np.flatnonzero(np.abs(audio) >= threshold)
    if not active.size:
        raise ValueError("Qwen TTS returned silence")
    margin = round(sample_rate * margin_s)
    start = max(0, int(active[0]) - margin)
    end = min(len(audio), int(active[-1]) + margin + 1)
    return audio[start:end]


def generate_phrase(model, request: dict, text: str, seed: int) -> tuple[np.ndarray, int]:
    mx.random.seed(seed)
    results = list(
        model.generate(
            text=text,
            voice=request["voice"],
            instruct=request["instruct"],
            lang_code=request["language"],
            temperature=request["temperature"],
            top_p=request["top_p"],
            top_k=request["top_k"],
            repetition_penalty=request["repetition_penalty"],
        )
    )
    if not results:
        raise RuntimeError(f"Qwen TTS produced no audio for: {text}")
    sample_rates = {result.sample_rate for result in results}
    if len(sample_rates) != 1:
        raise RuntimeError(f"Qwen TTS returned mixed sample rates for: {text}")
    audio = np.concatenate([np.asarray(result.audio, dtype=np.float32).reshape(-1) for result in results])
    sample_rate = sample_rates.pop()
    return (
        trim_audio(audio, sample_rate, request["trim_threshold"], request["trim_margin_s"]),
        sample_rate,
    )


def build_frame(model, request: dict, frame: dict) -> tuple[np.ndarray, int, list[dict]]:
    if len(frame["gaps_s"]) != len(frame["phrases"]) - 1:
        raise ValueError(f"frame {frame['id']} gap count does not match phrase count")

    sample_rate = None
    chunks = []
    words = []
    cursor = request["lead_s"]
    chunks.append(np.zeros(round(cursor * 24000), dtype=np.float32))

    for index, text in enumerate(frame["phrases"]):
        phrase_audio, phrase_sample_rate = generate_phrase(
            model,
            request,
            text,
            request["seed"] + frame["frame"] * 100 + index,
        )
        if sample_rate is None:
            sample_rate = phrase_sample_rate
            chunks[0] = np.zeros(round(request["lead_s"] * sample_rate), dtype=np.float32)
        elif phrase_sample_rate != sample_rate:
            raise RuntimeError(f"frame {frame['id']} has inconsistent sample rates")

        start = cursor
        end = start + len(phrase_audio) / sample_rate
        words.append({"id": f"w{index}", "text": text, "start": start, "end": end})
        chunks.append(phrase_audio)
        cursor = end

        if index < len(frame["gaps_s"]):
            gap_s = frame["gaps_s"][index]
            chunks.append(np.zeros(round(gap_s * sample_rate), dtype=np.float32))
            cursor += gap_s

    audio = np.concatenate(chunks)
    target_samples = round(frame["target_duration_s"] * sample_rate)
    if len(audio) > target_samples:
        overflow_s = (len(audio) - target_samples) / sample_rate
        raise RuntimeError(f"frame {frame['id']} exceeds target duration by {overflow_s:.3f}s")
    audio = np.pad(audio, (0, target_samples - len(audio)))

    peak = float(np.max(np.abs(audio)))
    target_peak = math.pow(10.0, request["target_peak_dbfs"] / 20.0)
    if peak > 0:
        audio = audio * (target_peak / peak)
    return audio.astype(np.float32), sample_rate, words


def update_meta(meta: dict, request: dict, generated: list[dict], engine: bool) -> None:
    meta["tts"] = {
        "provider": request["provider"],
        "runtime": request["runtime"],
        "model": request["model"],
        "voice": request["voice"],
        "language": request["language"],
        "instruct": request["instruct"],
        "seed": request["seed"],
    }
    if engine:
        meta["tts_provider"] = request["provider"]
        meta["voice_id"] = request["voice"]
        meta["total_duration_s"] = round(
            sum(frame["target_duration_s"] for frame in request["frames"]), 3
        )

    by_frame = {item["frame"]: item for item in generated}
    for voice in meta["voices"]:
        frame_number = int(voice.get("frame", voice.get("id")))
        item = by_frame[frame_number]
        voice.update(
            {
                "path": item["path"],
                "duration_s": item["duration_s"],
                "words": item["words"],
                "provider": request["provider"],
                "runtime": request["runtime"],
                "model": request["model"],
                "voice": request["voice"],
                "sample_rate_hz": item["sample_rate_hz"],
                "sha256": item["sha256"],
            }
        )


def main() -> None:
    request = load_json(REQUEST_PATH)
    model = load_model(request["model"])
    built = []

    for frame in request["frames"]:
        audio, sample_rate, words = build_frame(model, request, frame)
        built.append((frame, audio, sample_rate, words))
        speech_end = words[-1]["end"]
        print(
            f"frame {frame['id']}: {len(words)} phrases, "
            f"speech {speech_end:.3f}s, target {frame['target_duration_s']:.3f}s"
        )

    generated = []
    for frame, audio, sample_rate, words in built:
        relative_path = f"assets/voice/{frame['id']}.wav"
        output_path = PROJECT_DIR / relative_path
        audio_write(str(output_path), audio, sample_rate, format="wav")
        generated.append(
            {
                "frame": frame["frame"],
                "path": relative_path,
                "duration_s": frame["target_duration_s"],
                "words": words,
                "sample_rate_hz": sample_rate,
                "sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
            }
        )

    audio_meta = load_json(AUDIO_META_PATH)
    engine_meta = load_json(ENGINE_META_PATH)
    update_meta(audio_meta, request, generated, engine=False)
    update_meta(engine_meta, request, generated, engine=True)
    write_json(AUDIO_META_PATH, audio_meta)
    write_json(ENGINE_META_PATH, engine_meta)
    print(f"generated {len(generated)} Qwen voice tracks with {sum(len(item['words']) for item in generated)} phrases")


if __name__ == "__main__":
    main()
