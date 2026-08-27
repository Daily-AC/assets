# Omnireach Overdrive Launch Video Design

Date: 2026-07-13
Status: Approved for autonomous implementation

## Context

The existing `omnireach-native-bridge` short proves the native Chrome bridge with a restrained,
minimal visual language. This second cut must preserve the same technical honesty while exploring
the opposite creative direction: fast, loud, layered, and deliberately theatrical.

The user asked for a separate cool version with freedom to show off and add music. This is an
autonomous production. It must not overwrite the existing Qwen3-TTS master.

## Goal

Produce one 32-38 second portrait launch video that makes a narrow promise:

> Omnireach can reuse an already logged-in Chrome session for read-only Douyin search without
> invoking OpenCLI and without creating a visible Chrome window or tab during the verified run.

The video should feel like a cybernetic system breaking out of a heavy browser-automation loop,
then prove the claim with the real command output.

## Audience And Destination

- Audience: Chinese-speaking developers using coding agents, MCP, Playwright, or browser research.
- Primary destination: Douyin and YouTube Shorts.
- Canvas: 1080 x 1920, 9:16 portrait, 30 fps.
- Language: simplified Chinese narration and burned captions.
- Duration: target 34 seconds; acceptable range 32-38 seconds.
- Mode: autonomous.

## Story Direction

Use a compressed PAS-to-demo arc:

1. A familiar pain appears as a swarm of fake Chrome windows.
2. The read-only boundary cuts through the heavy interaction stack.
3. Omnireach's native bridge becomes a luminous data tunnel.
4. One real Douyin command produces three real results.
5. Four verified facts lock into a proof reticle, followed by the install command.

The hook and promise land within five seconds. The rest of the video is evidence, not feature
inventory.

## Visual System

The base frame preset is `blockframe`, remixed into a cyberpunk neobrutalist system:

- canvas: near-black `#07090d`;
- primary ink: cold white `#f5f7ff`;
- cyan signal: `#31e8ff`;
- magenta signal: `#ff2fb3`;
- acid success: `#b6ff3b`;
- warning red: `#ff4a5f`;
- hot yellow: `#ffd84d`.

Use hard rectangular panels, 3-4 px borders, sharp offset shadows, scanline masks, perspective
grids, chromatic text offsets, glitch shutters, and fast camera pushes. Do not use gradient orbs,
stock footage, fake product screenshots, or rounded glass-card stacks. Fake browser windows are
allowed only as an abstract pain metaphor and must shatter before the product proof begins.

Text remains readable on a phone: hero phrases use two to five words, technical labels use a
monospace face, and all captions stay above the bottom 340 px platform keep-out band.

## Frames

### Frame 1: Ghost Window

- Duration: about 4.5 seconds.
- Shape: `ticker-takeover` adapted into a glitch hook.
- Visual: translucent browser-window outlines slam in from several directions while the question
  `Agent 搜个抖音 / 又弹 Chrome?` flickers between cyan and magenta channels.
- Signature move: the window swarm fractures into rectangular shards on the final word.

### Frame 2: Break The Loop

- Duration: about 5.5 seconds.
- Shape: `comparison-split` plus kinetic type.
- Visual: a dense `DRIVE / CLICK / FORM / UPLOAD` stack is weighed against a thin
  `SEARCH / FETCH / READ` rail. A luminous line cuts the read-only path free.
- Boundary: a small stable label states that interaction and visual checks still belong to
  Playwright.

### Frame 3: Native Tunnel

- Duration: about 6.5 seconds.
- Shape: `spatial-pan-stations` adapted to a vertical perspective tunnel.
- Visual: `LOGGED-IN CHROME`, `LOCALHOST BRIDGE`, and `OMNIREACH` form three stations. Data packets
  travel through the tunnel without exposing cookies, credentials, profile paths, or tokens.
- Proof label: `READ-ONLY NATIVE BRIDGE`.

### Frame 4: Live Hitstorm

- Duration: about 9 seconds.
- Shape: `cursor-ui-demo` plus `grid-card-assemble`.
- Visual: the real command types into a reconstructed terminal, then three result records from the
  sanitized E2E fixture cascade into stable HUD rows. `adapter: native-chrome` remains visible.
- Source of truth: `data/evidence.json` copied from the verified native-bridge production fixture.

### Frame 5: Proof Lock

- Duration: about 9 seconds.
- Shape: `logo-assemble-lockup` into `cta-morph-press`.
- Visual: four proof signals enter a targeting reticle: `NO OPENCLI`, `native-chrome`, `errors: []`,
  and `VISIBLE 0 -> 0`. The reticle collapses into the Omnireach wordmark and install command.
- CTA: `装完，直接搜。` with `github.com/Daily-AC/omnireach`.

## Narration

Use the already verified local model `mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-6bit`, voice
`Vivian`. Delivery is fast, confident, and slightly provocative, with short cue-shaped clauses.

Locked copy:

> Agent 搜个抖音，怎么又弹 Chrome？搜索和读取，不该每次拉起整套浏览器自动化。
> Omnireach 直接复用你已经登录的 Chrome，只走一条只读原生桥。真实运行，三条抖音
> 结果，adapter 是 native-chrome。PATH 里没有 OpenCLI，errors 为空，可见窗口和标签页
> 都是零到零。点击和表单仍交给 Playwright。搜索和读取，装完直接用。

## Music And Sound

Create an original, deterministic 132 BPM electronic track with no samples and no vocals. The
arrangement uses synthesized kick, snare, hats, sub-bass, gated arpeggio, risers, and impacts. It
must be generated locally from source code and mixed below narration with sidechain-style ducking.

Use short self-owned interface sounds for the window slam, fracture, tunnel launch, result hits,
proof locks, and CTA press. Avoid copyrighted music and external sample dependencies.

## Evidence And Claims

The production reuses the sanitized fixture from the first video because it already records one
real forced-native run with:

- OpenCLI absent from the restricted `PATH`;
- three returned Douyin records;
- `adapter: native-chrome`;
- `errors: []`;
- visible Chrome windows and tabs `0 -> 0`.

The video must not claim that Omnireach replaces Playwright for clicking, forms, uploads, visual
inspection, or arbitrary browser interaction.

## Deliverables

- `videos/omnireach-overdrive/`: independent editable HyperFrames project.
- `renders/omnireach-overdrive.mp4`: final 1080 x 1920 H.264/AAC master.
- `snapshots/contact-sheet.jpg`: visual verification sheet.
- Qwen3 narration, word timings, captions, original music source, and final music stem.
- Sanitized real evidence fixture and source composition.

## Verification

- Duration is 32-38 seconds; resolution is 1080 x 1920 at 30 fps.
- H.264 video and AAC stereo audio both decode from start to finish.
- Narration uses Qwen3-TTS, not Kokoro.
- Music is audible under narration without masking speech.
- Captions and technical proof stay inside safe margins with no overlap.
- Contact-sheet frames show nonblank, intentional compositions at every beat.
- Claims match the real fixture exactly.
- The rendered file contains no credentials, tokens, profile paths, cookies, or private account data.
- The existing `omnireach-native-bridge` source and render remain untouched.

