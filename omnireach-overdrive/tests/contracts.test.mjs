import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const projectDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const readJson = (relativePath) =>
  JSON.parse(readFileSync(path.join(projectDir, relativePath), "utf8"));
const sha256 = (filePath) => createHash("sha256").update(readFileSync(filePath)).digest("hex");

test("the production fixture preserves the verified native Douyin run", () => {
  const evidence = readJson("data/evidence.json");

  assert.equal(evidence.transport.forced, "native");
  assert.equal(evidence.transport.opencli_in_path, false);
  assert.equal(evidence.transport.adapter, "native-chrome");
  assert.deepEqual(evidence.errors, []);
  assert.equal(evidence.results.length, 3);
  assert.deepEqual(evidence.chrome.before, { windows: 0, tabs: 0 });
  assert.deepEqual(evidence.chrome.after, { windows: 0, tabs: 0 });
});

test("the narration contract pins Qwen3 TTS and one unique frame id per track", () => {
  const request = readJson("qwen_voice_request.json");
  const ids = request.frames.map((frame) => frame.id);

  assert.equal(request.provider, "qwen3-tts");
  assert.equal(request.runtime, "mlx-audio");
  assert.match(request.model, /Qwen3-TTS/);
  assert.equal(request.voice, "Vivian");
  assert.equal(new Set(ids).size, ids.length);
  assert.ok(request.frames.every((frame) => frame.phrases.every((phrase) => phrase.trim())));
  assert.equal(
    request.frames.reduce((total, frame) => total + frame.target_duration_s, 0),
    36.1,
  );
});

test("generated narration artifacts match their Qwen metadata", () => {
  const request = readJson("qwen_voice_request.json");
  const meta = readJson("audio_meta.json");

  assert.equal(meta.tts.provider, request.provider);
  assert.equal(meta.tts.model, request.model);
  assert.equal(meta.tts.voice, request.voice);
  assert.equal(meta.voices.length, request.frames.length);

  for (const voice of meta.voices) {
    const voicePath = path.join(projectDir, voice.path);
    assert.ok(existsSync(voicePath), `${voice.path} must exist`);
    assert.equal(voice.provider, "qwen3-tts");
    assert.equal(voice.sha256, sha256(voicePath));
    assert.ok(voice.words.length > 0);
  }
});

test("caption groups preserve the sixteen short Qwen phrase cues", () => {
  const captions = readJson("caption_groups.json");

  assert.equal(captions.groups.length, 16);
  assert.ok(captions.groups.every((group) => group.words.length === 1));
  assert.ok(Math.max(...captions.groups.map((group) => group.text.length)) <= 32);
});
