#!/usr/bin/env node

import { readFileSync, writeFileSync } from "node:fs";

const metaPath = new URL("../audio_meta.json", import.meta.url);
const meta = JSON.parse(readFileSync(metaPath, "utf8"));

for (const voice of meta.voices ?? []) {
  if (!voice.words?.length) throw new Error(`missing caption timing for frame ${voice.frame}`);
  for (const { start, end } of voice.words) {
    if (start < 0 || end <= start || end > voice.duration_s + 0.001) {
      throw new Error(`caption timing outside frame ${voice.frame}: ${start}-${end}`);
    }
  }
}

const sfxTiming = {
  "1:error.mp3": [0.9, 0.2],
  "1:whoosh-short.mp3": [3.1, 0.18],
  "2:click-soft.mp3": [1.8, 0.16],
  "2:whoosh-short.mp3": [5.0, 0.16],
  "3:whoosh.mp3": [1.4, 0.18],
  "3:chime.mp3": [4.8, 0.16],
  "4:typing.mp3": [1.2, 0.14],
  "4:click-soft.mp3": [4.4, 0.16],
  "5:pop.mp3": [1.5, 0.16],
  "5:ping.mp3": [11.7, 0.18],
  "6:key-press.mp3": [1.9, 0.16],
  "6:chime.mp3": [8.2, 0.16],
};

for (const effect of meta.sfx ?? []) {
  const name = String(effect.file).split("/").pop();
  const timing = sfxTiming[`${effect.frame}:${name}`];
  if (!timing) throw new Error(`missing SFX timing for frame ${effect.frame}: ${name}`);
  [effect.offset_s, effect.volume] = timing;
}

writeFileSync(metaPath, `${JSON.stringify(meta, null, 2)}\n`);
console.log(
  `validated ${meta.voices?.flatMap((voice) => voice.words ?? []).length ?? 0} caption phrases and retimed ${meta.sfx?.length ?? 0} SFX cues`,
);
