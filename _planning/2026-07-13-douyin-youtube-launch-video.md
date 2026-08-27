# Douyin and YouTube Shorts Launch Video Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce and verify a polished 50-second, 1080 x 1920 launch video that proves Omnireach can perform a logged-in Douyin search through the native Chrome bridge without OpenCLI in `PATH` and without opening a visible Chrome window or tab.

**Architecture:** Capture one fresh forced-native CLI run into a sanitized evidence fixture, then drive an editable HyperFrames composition entirely from that fixture and a time-coded script. Six independently built scenes share one portrait-safe visual frame, Mandarin narration, burned captions, and restrained generated interface audio. Render one cross-platform master plus a cover and platform-specific copy; do not upload during this plan.

**Tech Stack:** Omnireach 0.14.0-alpha CLI, native Chrome bridge, HyperFrames 0.7.54, HTML/CSS/JavaScript, Mandarin TTS, FFmpeg/ffprobe, Git, GitHub source capture.

---

## File Map

- Create `videos/omnireach-native-bridge/`: editable HyperFrames project.
- Create `videos/omnireach-native-bridge/data/evidence.json`: sanitized real E2E evidence.
- Create `videos/omnireach-native-bridge/STORYBOARD.md`: six-scene visual and timing contract.
- Create `videos/omnireach-native-bridge/SCRIPT.md`: narration and caption contract.
- Create `videos/omnireach-native-bridge/frame.md`: portrait visual-system contract.
- Create `videos/omnireach-native-bridge/public/assets/`: staged logo, capture, audio, and fixture assets.
- Create `videos/omnireach-native-bridge/src/frames/frame-{01..06}.html`: independently previewable scenes.
- Create `videos/omnireach-native-bridge/src/composition.html`: assembled seek-safe composition.
- Create `videos/omnireach-native-bridge/renders/omnireach-douyin-shorts.mp4`: final master.
- Create `videos/omnireach-native-bridge/renders/cover.png`: final cover frame.
- Create `videos/omnireach-native-bridge/snapshots/contact-sheet.jpg`: verification contact sheet.
- Create `docs/launch/2026-07-13-douyin-youtube-video.md`: Douyin and YouTube Shorts publishing copy.

### Task 1: Verify The Production Toolchain And Scaffold The Project

**Files:**
- Create: `videos/omnireach-native-bridge/`

- [ ] **Step 1: Record HyperFrames authentication status**

Run:

```bash
npx hyperframes auth status
```

Preserve the command output in the task log. Authentication may select a hosted media provider; an unauthenticated result must use the documented local media fallback and must not block production.

- [ ] **Step 2: Verify local media capabilities**

Run:

```bash
node /Users/e0_7/.agents/skills/media-use/scripts/resolve.mjs --doctor
```

Expected: at least one supported TTS path plus FFmpeg are available.

- [ ] **Step 3: Initialize the blank portrait composition**

Run:

```bash
npx hyperframes init "videos/omnireach-native-bridge" --non-interactive --example=blank
node /Users/e0_7/.agents/skills/media-use/scripts/resolve.mjs --adopt --project videos/omnireach-native-bridge
```

Expected: the project contains a runnable HyperFrames manifest and no unrelated demo frames.

- [ ] **Step 4: Verify the scaffold before customization**

Run:

```bash
cd videos/omnireach-native-bridge
npx hyperframes check
```

Expected: the blank project passes structural checks.

### Task 2: Capture Fresh Native-Bridge Evidence

**Files:**
- Create: `videos/omnireach-native-bridge/data/evidence.json`
- Create: `videos/omnireach-native-bridge/data/evidence.raw.json`

- [ ] **Step 1: Count visible Chrome windows and tabs before the run**

Run `osascript` against Google Chrome and record both visible window count and tab count. A non-running Chrome process is represented as zero, not an error.

- [ ] **Step 2: Capture bridge status from the published global CLI**

Run:

```bash
/Users/e0_7/.local/bin/omnireach bridge status --json
```

Expected: installed extension and connected native bridge status with no credential values printed.

- [ ] **Step 3: Run one forced-native Douyin search without OpenCLI in `PATH`**

Run:

```bash
env PATH=/usr/bin:/bin:/usr/sbin:/sbin \
  OMNIREACH_BROWSER_TRANSPORT=native \
  /Users/e0_7/.local/bin/omnireach search "gpt5.6" \
  --on douyin --limit 3 --timeout 45 --json
```

Expected: three real Douyin results, `adapter` equal to `native-chrome`, and an empty `errors` array.

- [ ] **Step 4: Count visible Chrome windows and tabs after the run**

Repeat the exact Step 1 script. The before and after values must match; the video claim uses `0 -> 0` only if those are the actual values.

- [ ] **Step 5: Sanitize and validate the production fixture**

Copy only the timestamp, exact public command, public result title/author/URL fields, adapter, error list, bridge version, and window/tab counts into `data/evidence.json`. Keep the complete command output in `data/evidence.raw.json` only after checking that it contains no token, browser profile path, cookie, extension credential, or private account identifier.

Run:

```bash
rg -n -i 'token|cookie|credential|authorization|profile|/Users/|localhost:[0-9]+' \
  videos/omnireach-native-bridge/data/evidence*.json
```

Expected: no secret or private-path matches. Public localhost transport metadata must be removed from the shareable fixture.

### Task 3: Capture The Product And Lock The Visual System

**Files:**
- Create: `videos/omnireach-native-bridge/capture/`
- Create: `videos/omnireach-native-bridge/frame.md`

- [ ] **Step 1: Capture the current public repository page**

Run:

```bash
cd videos/omnireach-native-bridge
npx hyperframes capture "https://github.com/Daily-AC/omnireach" -o ./capture
```

Expected: a fresh capture manifest and inspectable repository screenshot with no login-only UI or user data.

- [ ] **Step 2: Build the approved high-impact portrait frame**

Inspect the product-launch-video frame presets, select the closest dark high-impact system, and build `frame.md` through the workflow `scripts/build-frame.mjs`. Override it to the approved fixed palette: `#111315`, off-white, `#ffcc38`, `#50e878`, `#58d4e5`, and red only for pain/error states. Use zero gradients and keep all critical content inside portrait platform-safe margins.

- [ ] **Step 3: Check frame compliance**

Confirm `frame.md` specifies 1080 x 1920, 30 fps, stable terminal dimensions, letter spacing zero, no stock imagery, no fake browser chrome, no nested cards, and no unsupported performance claim.

### Task 4: Write The Time-Coded Storyboard And Script

**Files:**
- Create: `videos/omnireach-native-bridge/STORYBOARD.md`
- Create: `videos/omnireach-native-bridge/SCRIPT.md`

- [ ] **Step 1: Write six scene contracts totaling 50 seconds**

Use these exact scene windows:

```text
01 Hook             00.0-03.0
02 Scope            03.0-09.0
03 Native bridge    09.0-16.0
04 Real search      16.0-29.0
05 Proof stack      29.0-41.0
06 Install CTA      41.0-50.0
```

Each scene must define its semantic role, visible text, fixture fields, motion phases, safe-zone bounds, transition handles, and audio cues.

- [ ] **Step 2: Lock narration and burned captions**

Use the approved Mandarin script from the design spec, removing filler only to fit 50 seconds. Preserve these boundaries verbatim in meaning: read-only search does not need full Playwright every time; Omnireach does not replace clicks/forms/uploads/visual checks; login state is reused without showing passwords; OpenCLI is absent; the measured visible-window count is factual.

- [ ] **Step 3: Audit every claim against evidence**

Every result title, adapter name, error state, bridge version, and window/tab count in `STORYBOARD.md` and `SCRIPT.md` must be traceable to `data/evidence.json`.

### Task 5: Produce Mandarin Audio And Caption Timing

**Files:**
- Create: `videos/omnireach-native-bridge/public/assets/audio/narration.wav`
- Create: `videos/omnireach-native-bridge/public/assets/audio/ui-sfx.wav`
- Create: `videos/omnireach-native-bridge/public/assets/audio/audio_meta.json`
- Create: `videos/omnireach-native-bridge/public/assets/captions.json`

- [ ] **Step 1: Run the media opportunity pass**

Use `media-use` to resolve a neutral, energetic Mandarin TTS voice and subtle original interface sounds. Do not use copyrighted music or imitate a real person.

- [ ] **Step 2: Generate narration, SFX, and caption timing**

Use the product workflow `scripts/audio.mjs` so `audio_meta.json` remains the source of truth for timing. Keep narration clear above the interface sounds and insert deliberate pauses around the command and proof fields.

- [ ] **Step 3: Verify audio assets**

Run `ffprobe` on both audio files. Expected: valid non-empty streams, narration duration compatible with the 50-second composition, and no clipping in the mixed track.

### Task 6: Build Six Independently Previewable Frames

**Files:**
- Create: `videos/omnireach-native-bridge/src/frames/frame-01.html`
- Create: `videos/omnireach-native-bridge/src/frames/frame-02.html`
- Create: `videos/omnireach-native-bridge/src/frames/frame-03.html`
- Create: `videos/omnireach-native-bridge/src/frames/frame-04.html`
- Create: `videos/omnireach-native-bridge/src/frames/frame-05.html`
- Create: `videos/omnireach-native-bridge/src/frames/frame-06.html`

- [ ] **Step 1: Dispatch one isolated worker per frame**

After reading the product workflow's frame-worker and dispatch references, use one subagent per frame as required by the workflow. Run at most three frame workers concurrently. Each worker may edit only its assigned frame file and must consume the shared `frame.md`, storyboard, script, evidence fixture, and staged assets.

- [ ] **Step 2: Verify each frame independently**

Preview and snapshot the midpoint of each frame. Check that text fits, evidence remains legible at phone scale, motion is seek-safe, and no frame invents data absent from the fixture.

- [ ] **Step 3: Correct frame-level failures**

Fix clipping, overlapping text, unstable terminal dimensions, wrong data, or non-seek-safe animations in the owning frame before assembly.

### Task 7: Assemble, Caption, And Render The Master

**Files:**
- Create: `videos/omnireach-native-bridge/src/composition.html`
- Create: `videos/omnireach-native-bridge/renders/omnireach-douyin-shorts.mp4`
- Create: `videos/omnireach-native-bridge/renders/cover.png`
- Create: `videos/omnireach-native-bridge/snapshots/contact-sheet.jpg`

- [ ] **Step 1: Assemble frames and inject transitions**

Use the workflow assembler and transition scripts. Keep transitions brief and subordinate to evidence readability. Burn simplified-Chinese captions inside the platform-safe lower region without covering terminal rows or the CTA.

- [ ] **Step 2: Run structural and composition checks**

Run:

```bash
cd videos/omnireach-native-bridge
npx hyperframes lint
npx hyperframes check
npx hyperframes check
```

Expected: all three commands exit zero; the repeated check guards against generated-file drift.

- [ ] **Step 3: Render verification snapshots**

Render the hook, scope boundary, command, real results, proof stack, and CTA frames plus a contact sheet. Inspect the files visually at full size and at a phone-sized preview.

- [ ] **Step 4: Render the final master and cover**

Render the 1080 x 1920 H.264 MP4 with AAC audio at 30 fps and export a high-contrast cover PNG using the hook plus the native-bridge proof cue.

- [ ] **Step 5: Verify the encoded artifact**

Run:

```bash
ffprobe -v error -show_entries \
  format=duration:stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json videos/omnireach-native-bridge/renders/omnireach-douyin-shorts.mp4
```

Expected: duration 45-55 seconds, one 1080 x 1920 H.264 video stream at 30 fps, and one AAC audio stream.

- [ ] **Step 6: Watch the complete master**

Watch from first frame through the final CTA. Reject the render for any caption desynchronization, clipped text, blank frame, layout shift, unreadable evidence, audio dropout, or unsupported claim.

### Task 8: Write Platform Copy And Complete The Delivery Audit

**Files:**
- Create: `docs/launch/2026-07-13-douyin-youtube-video.md`

- [ ] **Step 1: Write Douyin publishing copy**

Include one concise title, one caption, relevant restrained hashtags, and a pinned comment asking viewers to install, run one search, and report a reproducible failure case. Keep GitHub Star secondary.

- [ ] **Step 2: Write YouTube Shorts publishing copy**

Include one searchable title, description with installation and repository links, tags, and a pinned comment with the same reproducibility challenge.

- [ ] **Step 3: Run the final privacy and placeholder audit**

Run:

```bash
rg -n -i 'todo|tbd|placeholder|lorem|token|cookie|credential|authorization|/Users/e0_7' \
  videos/omnireach-native-bridge docs/launch/2026-07-13-douyin-youtube-video.md
git diff --check
```

Expected: no placeholders, secrets, private paths, or whitespace errors in deliverables. Build tooling may contain its own documented TODOs only if they are outside rendered or published assets.

- [ ] **Step 4: Commit the complete reviewable unit**

Run:

```bash
git add videos/omnireach-native-bridge \
  docs/launch/2026-07-13-douyin-youtube-video.md
git commit -m "video: produce native Douyin bridge launch short"
```

Expected: one self-contained commit containing source, evidence, master, cover, and publishing copy. Uploading to Douyin or YouTube remains out of scope until the rendered master is reviewed.
