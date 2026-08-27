#!/usr/bin/env python3

import argparse
import math
import struct
import wave
from pathlib import Path


SAMPLE_RATE = 48000
BPM = 132.0
BEAT = 60.0 / BPM
TAU = math.tau
DEFAULT_DURATION = 36.3
BOUNDARIES = (4.2, 9.5, 16.0, 24.3)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def noise(sample: int, salt: int = 0) -> float:
    value = (sample * 1103515245 + 12345 + salt * 2654435761) & 0xFFFFFFFF
    value ^= value >> 13
    value = (value * 1274126177) & 0xFFFFFFFF
    return ((value / 0xFFFFFFFF) * 2.0) - 1.0


def kick(local: float) -> float:
    if local < 0.0 or local >= 0.28:
        return 0.0
    envelope = math.exp(-local * 15.0)
    frequency = 48.0 + 112.0 * math.exp(-local * 24.0)
    click = math.exp(-local * 95.0) * 0.24
    return math.sin(TAU * frequency * local) * envelope + click


def snare(local: float, sample: int) -> float:
    if local < 0.0 or local >= 0.22:
        return 0.0
    envelope = math.exp(-local * 18.0)
    body = math.sin(TAU * 176.0 * local) * math.exp(-local * 26.0)
    return 0.72 * noise(sample, 7) * envelope + 0.28 * body


def hat(local: float, sample: int, open_hat: bool) -> float:
    length = 0.18 if open_hat else 0.075
    if local < 0.0 or local >= length:
        return 0.0
    decay = 24.0 if open_hat else 58.0
    envelope = math.exp(-local * decay)
    bright = noise(sample, 19) - 0.62 * noise(sample - 1, 19)
    return bright * envelope


def impact(local: float, sample: int) -> float:
    if local < 0.0 or local >= 0.65:
        return 0.0
    envelope = math.exp(-local * 7.0)
    sub = math.sin(TAU * (62.0 - 18.0 * local) * local)
    grit = noise(sample, 31) * math.exp(-local * 16.0)
    return sub * envelope + grit * 0.28


def riser(time_s: float, sample: int) -> float:
    value = 0.0
    for boundary in BOUNDARIES:
        local = boundary - time_s
        if 0.0 < local <= 0.72:
            progress = 1.0 - local / 0.72
            flutter = 0.55 + 0.45 * math.sin(TAU * (9.0 + progress * 18.0) * time_s)
            value += noise(sample, 43) * progress * progress * flutter
    return value


def synth_sample(time_s: float, sample: int, duration: float) -> tuple[float, float]:
    beat_index = int(time_s / BEAT)
    beat_phase = time_s - beat_index * BEAT
    eighth = BEAT / 2.0
    eighth_phase = time_s % eighth
    sixteenth = BEAT / 4.0
    sixteenth_index = int(time_s / sixteenth)
    sixteenth_phase = time_s - sixteenth_index * sixteenth

    section = min(4, int(time_s / max(duration / 5.0, 0.001)))
    section_energy = (0.68, 0.78, 0.88, 1.0, 1.08)[section]
    intro = clamp(time_s / 1.2, 0.0, 1.0)
    outro = clamp((duration - time_s) / 1.0, 0.0, 1.0)
    master_env = intro * outro

    kick_value = kick(beat_phase) * 0.68
    snare_value = 0.0
    if beat_index % 4 in (1, 3):
        snare_value = snare(beat_phase, sample) * 0.24

    open_hat = sixteenth_index % 8 == 6
    hat_value = hat(sixteenth_phase, sample, open_hat) * (0.08 if open_hat else 0.055)

    bass_notes = (41.203, 41.203, 49.0, 55.0, 41.203, 61.735, 55.0, 49.0)
    bass_frequency = bass_notes[(beat_index // 2) % len(bass_notes)]
    bass_gate = math.exp(-eighth_phase * 3.6)
    sidechain = 0.28 + 0.72 * clamp(beat_phase / 0.18, 0.0, 1.0)
    bass_phase = TAU * bass_frequency * time_s
    bass_value = (math.sin(bass_phase) + 0.22 * math.sin(2.0 * bass_phase))
    bass_value *= bass_gate * sidechain * 0.22

    arp_notes = (164.814, 195.998, 246.942, 293.665, 246.942, 195.998, 329.628, 246.942)
    arp_frequency = arp_notes[sixteenth_index % len(arp_notes)]
    arp_gate = math.exp(-sixteenth_phase * 20.0)
    arp_phase = TAU * arp_frequency * time_s
    arp_value = (math.sin(arp_phase) + 0.34 * math.sin(2.0 * arp_phase)) * arp_gate
    arp_value *= 0.095 * section_energy
    pan = -0.58 if sixteenth_index % 2 == 0 else 0.58

    pulse_frequency = 82.407 if beat_index % 8 < 4 else 73.416
    pulse = math.sin(TAU * pulse_frequency * time_s)
    pulse *= (0.5 + 0.5 * math.sin(TAU * 2.0 * time_s)) * 0.035 * section_energy

    impact_value = 0.0
    for boundary in (0.0,) + BOUNDARIES:
        impact_value += impact(time_s - boundary, sample) * 0.18
    riser_value = riser(time_s, sample) * 0.045

    center = kick_value + snare_value + hat_value + bass_value + pulse + impact_value
    left = center + arp_value * (1.0 - pan) * 0.5 + riser_value
    right = center + arp_value * (1.0 + pan) * 0.5 - riser_value * 0.4

    left = math.tanh(left * 1.32) * 0.72 * master_env
    right = math.tanh(right * 1.32) * 0.72 * master_env
    return left, right


def write_music(output: Path, duration: float) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    frame_count = round(duration * SAMPLE_RATE)

    with wave.open(str(output), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)

        chunk = bytearray()
        for sample in range(frame_count):
            time_s = sample / SAMPLE_RATE
            left, right = synth_sample(time_s, sample, duration)
            chunk.extend(
                struct.pack(
                    "<hh",
                    round(clamp(left, -1.0, 1.0) * 32767),
                    round(clamp(right, -1.0, 1.0) * 32767),
                )
            )
            if len(chunk) >= 262144:
                wav.writeframesraw(chunk)
                chunk.clear()
        if chunk:
            wav.writeframesraw(chunk)


def parse_args() -> argparse.Namespace:
    project_dir = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Generate Omnireach Overdrive's original music bed")
    parser.add_argument("--duration", type=float, default=DEFAULT_DURATION)
    parser.add_argument("--output", type=Path, default=project_dir / "assets/bgm/overdrive.wav")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.duration <= 0.0:
        raise SystemExit("duration must be positive")
    write_music(args.output.resolve(), args.duration)
    print(f"generated {args.output} ({args.duration:.3f}s, {SAMPLE_RATE} Hz stereo, {BPM:.0f} BPM)")


if __name__ == "__main__":
    main()
