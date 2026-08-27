import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdtempSync, readFileSync, rmSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { fileURLToPath } from "node:url";

const projectDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const generator = path.join(projectDir, "scripts", "generate-overdrive-bgm.py");
const hash = (filePath) => createHash("sha256").update(readFileSync(filePath)).digest("hex");

function generate(outputPath) {
  const result = spawnSync(
    "python3",
    [generator, "--duration", "4", "--output", outputPath],
    { cwd: projectDir, encoding: "utf8" },
  );
  assert.equal(result.status, 0, result.stderr || result.stdout);
}

test("the original music generator writes deterministic 48 kHz stereo PCM", () => {
  const tempDir = mkdtempSync(path.join(os.tmpdir(), "omnireach-overdrive-"));
  const first = path.join(tempDir, "first.wav");
  const second = path.join(tempDir, "second.wav");

  try {
    generate(first);
    generate(second);
    assert.equal(hash(first), hash(second));

    const probe = spawnSync(
      "ffprobe",
      [
        "-v",
        "error",
        "-show_entries",
        "stream=codec_name,sample_rate,channels",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        first,
      ],
      { encoding: "utf8" },
    );
    assert.equal(probe.status, 0, probe.stderr);
    const info = JSON.parse(probe.stdout);
    assert.equal(info.streams[0].codec_name, "pcm_s16le");
    assert.equal(info.streams[0].sample_rate, "48000");
    assert.equal(info.streams[0].channels, 2);
    assert.ok(Number(info.format.duration) >= 3.99);
  } finally {
    rmSync(tempDir, { recursive: true, force: true });
  }
});
