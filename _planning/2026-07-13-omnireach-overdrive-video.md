# Omnireach Overdrive Launch Video Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a separate 34-second cyberpunk launch short that combines real native-Douyin evidence, Qwen3-TTS narration, original electronic music, and five high-energy HyperFrames scenes.

**Architecture:** A new `videos/omnireach-overdrive` project owns all source and generated assets. The composition reads a copied sanitized E2E fixture, generates narration and music deterministically, builds one HTML sub-composition per storyboard frame, then assembles captions, transitions, and audio into one portrait master. The existing minimal video is a read-only source for verified evidence, fonts, Qwen tooling, and self-owned sound effects.

**Tech Stack:** HyperFrames 0.7.54, HTML/CSS/GSAP, Node.js tests, Python audio synthesis, Qwen3-TTS through `mlx-audio`, FFmpeg/ffprobe, Git.

---

## File Map

- Create `videos/omnireach-overdrive/hyperframes.json`: HyperFrames project configuration.
- Create `videos/omnireach-overdrive/capture/extracted/`: no-capture product brief and asset inventory.
- Create `videos/omnireach-overdrive/frame.md`: blockframe-derived visual system.
- Create `videos/omnireach-overdrive/STORYBOARD.md`: five-frame timing and motion contract.
- Create `videos/omnireach-overdrive/SCRIPT.md`: locked Qwen3 narration.
- Create `videos/omnireach-overdrive/data/evidence.json`: sanitized real E2E evidence.
- Create `videos/omnireach-overdrive/scripts/generate-qwen-voice.py`: local Qwen3 synthesis entry point.
- Create `videos/omnireach-overdrive/scripts/run-qwen-voice.mjs`: validates input and orchestrates voice generation.
- Create `videos/omnireach-overdrive/scripts/generate-overdrive-bgm.py`: deterministic 132 BPM music generator.
- Create `videos/omnireach-overdrive/tests/`: request, evidence, and generated-audio contract tests.
- Create `videos/omnireach-overdrive/compositions/frames/01-ghost-window.html`: glitch hook.
- Create `videos/omnireach-overdrive/compositions/frames/02-break-the-loop.html`: read-versus-drive boundary.
- Create `videos/omnireach-overdrive/compositions/frames/03-native-tunnel.html`: native bridge tunnel.
- Create `videos/omnireach-overdrive/compositions/frames/04-live-hitstorm.html`: real terminal and result cascade.
- Create `videos/omnireach-overdrive/compositions/frames/05-proof-lock.html`: proof reticle and CTA.
- Generate `videos/omnireach-overdrive/index.html`: assembled composition.
- Generate `videos/omnireach-overdrive/renders/omnireach-overdrive.mp4`: final master.

### Task 1: Scaffold The Independent Production

**Files:**
- Create: `videos/omnireach-overdrive/`
- Copy: `videos/omnireach-native-bridge/data/evidence.json`
- Copy: `videos/omnireach-native-bridge/assets/fonts/*`

- [ ] **Step 1: Initialize the project**

Run:

```bash
npx hyperframes init videos/omnireach-overdrive --non-interactive --example=blank
```

Expected: `hyperframes.json`, `package.json`, `index.html`, and project instructions exist.

- [ ] **Step 2: Create the no-capture inventory**

Write product tokens with the approved colors and fonts, write the full brief to
`capture/extracted/visible-text.txt`, and list `data/evidence.json` as the only content asset in
`capture/extracted/asset-descriptions.md`.

- [ ] **Step 3: Verify evidence equality**

Run:

```bash
cmp videos/omnireach-native-bridge/data/evidence.json videos/omnireach-overdrive/data/evidence.json
```

Expected: exit code 0.

### Task 2: Lock Story, Design, And Audio Contracts

**Files:**
- Create: `videos/omnireach-overdrive/frame.md`
- Create: `videos/omnireach-overdrive/STORYBOARD.md`
- Create: `videos/omnireach-overdrive/SCRIPT.md`
- Create: `videos/omnireach-overdrive/qwen_voice_request.json`

- [ ] **Step 1: Build the blockframe preset**

Run:

```bash
node /Users/e0_7/.agents/skills/product-launch-video/scripts/build-frame.mjs \
  --preset blockframe --hyperframes videos/omnireach-overdrive
```

Expected: the command exits 0 and writes `frame.md` plus `.hyperframes/caption-skin.html`.

- [ ] **Step 2: Write the five-frame storyboard**

Use `format: 1080x1920`, `mode: autonomous`, the approved PAS-to-demo arc, and the exact frame
source paths from the file map. Each frame includes a time-coded shot sequence, a real blueprint,
motion-rule ids, asset candidates, caption keep-out, and one narrative role.

- [ ] **Step 3: Write and validate the Qwen request**

The request must identify the Qwen3 model, Vivian voice, Mandarin language, and one spoken line per
frame. Add a Node test that rejects an empty line, a duplicate frame id, or any non-Qwen provider.

Run:

```bash
npm test --prefix videos/omnireach-overdrive
```

Expected: all request and evidence contract tests pass.

### Task 3: Generate And Verify Original Audio

**Files:**
- Create: `videos/omnireach-overdrive/scripts/generate-overdrive-bgm.py`
- Generate: `videos/omnireach-overdrive/assets/voice/*.wav`
- Generate: `videos/omnireach-overdrive/assets/bgm/overdrive.wav`
- Generate: `videos/omnireach-overdrive/audio_meta.json`

- [ ] **Step 1: Generate Qwen3 narration**

Run:

```bash
npm run voice:qwen --prefix videos/omnireach-overdrive
```

Expected: five nonempty WAV files and word-timing metadata identify Qwen3-TTS and Vivian.

- [ ] **Step 2: Generate the music stem**

The generator writes 48 kHz stereo PCM with a 132 BPM four-on-the-floor rhythm, alternating
sub-bass notes, gated arpeggio, hats, snare, risers, and deterministic impacts. It uses no random
seed, downloaded sample, or network source.

Run:

```bash
python3 videos/omnireach-overdrive/scripts/generate-overdrive-bgm.py
```

Expected: `assets/bgm/overdrive.wav` exists and is at least 32 seconds long.

- [ ] **Step 3: Probe audio**

Run:

```bash
ffprobe -v error -show_entries stream=codec_name,sample_rate,channels \
  -show_entries format=duration -of json videos/omnireach-overdrive/assets/bgm/overdrive.wav
```

Expected: PCM audio, 48000 Hz, stereo, and 32-38 seconds.

### Task 4: Build The Five Frames

**Files:**
- Create: `videos/omnireach-overdrive/compositions/frames/*.html`

- [ ] **Step 1: Dispatch one frame worker per storyboard frame**

Each worker reads only `frame.md`, its assigned storyboard block, its blueprint, and cited motion
rules. It writes only its assigned HTML file and registers a paused GSAP timeline in
`window.__timelines`.

- [ ] **Step 2: Validate every sub-composition**

Run after each worker returns:

```bash
npx hyperframes lint --project videos/omnireach-overdrive
```

Expected: no composition contract errors.

- [ ] **Step 3: Mark all frames animated**

Update only the five `status` fields in `STORYBOARD.md` from `outline` to `animated` after their
HTML files exist and lint cleanly.

### Task 5: Assemble, Render, And Inspect The Master

**Files:**
- Generate: `videos/omnireach-overdrive/caption_groups.json`
- Generate: `videos/omnireach-overdrive/index.html`
- Generate: `videos/omnireach-overdrive/snapshots/contact-sheet.jpg`
- Generate: `videos/omnireach-overdrive/renders/omnireach-overdrive.mp4`

- [ ] **Step 1: Build captions and assemble**

Run:

```bash
node /Users/e0_7/.agents/skills/product-launch-video/scripts/captions.mjs build \
  --storyboard videos/omnireach-overdrive/STORYBOARD.md \
  --audio-meta videos/omnireach-overdrive/audio_meta.json \
  --hyperframes videos/omnireach-overdrive \
  --out videos/omnireach-overdrive/caption_groups.json
node /Users/e0_7/.agents/skills/product-launch-video/scripts/assemble-index.mjs \
  --storyboard videos/omnireach-overdrive/STORYBOARD.md \
  --hyperframes videos/omnireach-overdrive
```

Expected: captions and `index.html` exist.

- [ ] **Step 2: Inject and verify transitions**

Run:

```bash
node /Users/e0_7/.agents/skills/product-launch-video/scripts/transitions.mjs inject \
  --storyboard videos/omnireach-overdrive/STORYBOARD.md \
  --hyperframes videos/omnireach-overdrive
node /Users/e0_7/.agents/skills/product-launch-video/scripts/transitions.mjs verify \
  --storyboard videos/omnireach-overdrive/STORYBOARD.md \
  --index videos/omnireach-overdrive/index.html
```

Expected: all non-cut transitions verify.

- [ ] **Step 3: Run visual checks and snapshot**

Run inside the project:

```bash
npx hyperframes lint
npx hyperframes check
npx hyperframes snapshot --at 2.2,7.2,13.2,21.8,30.5
```

Expected: checks pass and the contact sheet shows five nonblank, correctly framed scenes.

- [ ] **Step 4: Render and validate the master**

Run:

```bash
npx hyperframes render --skill=product-launch-video --quality high \
  --output renders/omnireach-overdrive.mp4
ffprobe -v error -show_streams -show_format -of json \
  videos/omnireach-overdrive/renders/omnireach-overdrive.mp4
ffmpeg -v error -i videos/omnireach-overdrive/renders/omnireach-overdrive.mp4 -f null -
```

Expected: 1080 x 1920 H.264 at 30 fps, AAC stereo, 32-38 seconds, and a clean full decode.

- [ ] **Step 5: Run repository regression tests and commit**

Run:

```bash
pytest -q
git status --short
```

Expected: all repository tests pass and only the new production source plus documentation is
staged for the final commit.

