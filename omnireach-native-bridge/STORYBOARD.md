---
format: 1080x1920
message: "Omnireach can reuse a logged-in Chrome session for read-only Douyin search without OpenCLI or a visible Chrome tab."
arc: "PAS + demo loop: pain → boundary → mechanism → real search → proof → challenge CTA"
audience: "Chinese-speaking developers who use coding agents, MCP, browser automation, or Playwright"
mode: autonomous
language: zh-CN
fps: 30
captions: burned simplified Chinese
music: none
evidence: data/evidence.json
---

# Omnireach Native Bridge Launch Short

## Video direction

- **Palette:** near-black is the continuous ground; off-white is primary copy; hook yellow is
  reserved for the pain and main CTA; success green appears only on verified facts; technical cyan
  labels transport and adapter fields; error red appears only on the opening pain state. No gradient,
  glow, blurred depth, decorative blob, stock image, or fake browser chrome.
- **Type:** PingFang SC display/body and SFMono-Regular command/data. Letter spacing is always zero.
  One dominant display moment per scene; the terminal keeps fixed dimensions and fixed row heights.
- **Motion grammar:** paused, seek-safe GSAP timelines; `fromTo` entrances; smooth long-tail settles;
  each line or evidence row arrives on its spoken cue, especially across the back half. No bounce,
  infinite loop, random value, wall clock, CSS animation, lazy breathing, or late camera drift.
- **Rhythm:** Frames 1 and 3 are short declarative hits. Frame 2 slows down for the product boundary.
  Frame 4 is the longest readable surface. Frame 5 reveals one proof row at a time and then holds.
  Frame 6 holds the install command long enough to pause and copy.
- **Safe area:** keep critical content inside x=72–1008, y=120–1580. The bottom caption band remains
  clear. The repository URL may sit just above the caption band, never underneath it.
- **Failure modes banned:** no front-loaded slideshow, no independent screensaver motion, no invented
  benchmark, no account identifier, no cookie/credential/profile path, and no claim that Omnireach
  replaces Playwright for interaction.

## Frame 1 — Stop Popping Chrome

- scene: Oversized Chinese hook replaces a red Chrome pain word with a yellow no-popup promise.
- voiceover: "Agent 搜个抖音，怎么又弹 Chrome？"
- duration: 3.9s
- poster: 2.8s
- transition_in: cut
- status: animated
- src: compositions/frames/01-stop-popping-chrome.html
- type: hook
- persuasion: Pain validation
- beat: frustration → curiosity
- blueprint: kinetic-type-beats (Adapt)
- asset_candidates:
- sfx: error, whoosh-short

narrativeRole: Name the exact interruption the viewer already hates and make the no-popup outcome the first promise.
keyMessage: Read-only search should not steal focus by opening Chrome.

Adapt: keep the fixed-center token-swap signature, but use two stacked Chinese lines and flat color
changes instead of playful scale overshoot.

Scene 1 (0.0–0.9s): on a near-black full-bleed clip, `AGENT 搜个抖音` lands in off-white via a
**per-word staggered reveal** (`dynamic-content-sequencing`); centered upper-third, sparse, one
display hierarchy.

Scene 2 (0.9–3.1s): the lower line hard-cuts to `怎么又弹 CHROME？`; `CHROME` is error red and a
thin red rule draws beneath it via **highlight sweep** (`css-marker-patterns`). The fixed anchor and
instant token state are the signature **hard-cut word-swap** (`discrete-text-sequence`).

Scene 3 (3.1–3.9s): the red word snaps away and the yellow payoff `别再弹。` replaces it in the same
slot; a short velocity-matched horizontal cut carries the change, then the line holds dead still.

## Frame 2 — Clear Boundary

- scene: A balanced split assigns read-only work to Omnireach and interactive work to Playwright.
- voiceover: "搜索和读取只是只读任务，没必要每次启动整套 Playwright。点击、表单、上传和视觉检查，仍然交给它。"
- duration: 10.4s
- poster: 7.8s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/02-clear-boundary.html
- type: feature_showcase
- persuasion: Negative contrast + risk reversal
- beat: clarity + trust
- blueprint: comparison-split (Adapt)
- asset_candidates:
- sfx: click-soft, whoosh-short

narrativeRole: Prevent the central objection by stating precisely where the lightweight path ends.
keyMessage: Omnireach lightens read-only search; Playwright still owns interaction and visual verification.

Adapt: keep the mirrored opposite-wing split as the signature, but use sharp flat panels with no
tilt shadow, glow, pill, or idle float.

Scene 1 (0.0–1.8s): mono kicker `不是替代，是分工` slides into the upper third; `不是替代` is
off-white and `是分工` is hook yellow. Centered header, broadside restraint.

Scene 2 (1.8–5.0s): the left flat panel enters from the left and settles in the top half of the
comparison region; technical cyan label `READ ONLY`, display copy `搜索 / 读取`, and small green
route `OMNIREACH` reveal one cue at a time via **opposite-wing entry** (`split-tilt-cards`, tilt
removed by adaptation).

Scene 3 (5.0–9.8s): the right panel enters from the right below it; label `INTERACTION`, then
`点击 / 表单 / 上传 / 视觉检查`, then `PLAYWRIGHT` reveal sequentially. The panels share equal
weight in a vertical 50/50 portrait split.

Scene 4 (9.8–10.4s): a 1px yellow divider locks between the two responsibilities; both panels hold
still for the boundary read.

## Frame 3 — Native Bridge

- scene: OMNIREACH assembles around a three-node path from logged-in Chrome to native-chrome.
- voiceover: "Omnireach 直接连接你已经登录的 Chrome，只继承登录态，不读取密码。"
- duration: 6.7s
- poster: 5.8s
- transition_in: squeeze
- status: animated
- src: compositions/frames/03-native-bridge.html
- type: product_intro
- persuasion: Friction reduction + trust by mechanism
- beat: relief + intrigue
- blueprint: logo-assemble-lockup (Adapt)
- asset_candidates:
- sfx: whoosh, chime

narrativeRole: Explain the mechanism simply enough that the no-popup claim feels credible rather than magical.
keyMessage: The native bridge reuses the existing logged-in Chrome session through a narrow local path.

Adapt: keep the segment-by-segment wordmark build and self-drawing connector as the signature; replace
the logo mark with a text wordmark and the orbit system with a flat three-node transport path.

Scene 1 (0.0–1.4s): `OMNI` and `REACH` assemble as two large text blocks in the upper third via
**segment-by-segment build** (`discrete-text-sequence`); yellow separator rule draws between them.

Scene 2 (1.4–4.8s): three sharp nodes reveal down the center, one per spoken cue: `CHROME LOGIN`
in off-white, `LOCAL BRIDGE · v0.1.1` in technical cyan, `NATIVE-CHROME` in success green. A single
vertical SVG hairline **self-draws** through them (`svg-path-draw`).

Scene 3 (4.8–6.6s): a compact permission ledger reveals `cookies: no`, `debugger: no`,
`<all_urls>: no` one row at a time, sourced from the extension manifest; asymmetric 70/30 with the
transport path dominant.

Scene 4 (6.6–6.7s): wordmark, path, and permission ledger hold; no camera motion or ambient loop.

## Frame 4 — Real Douyin Search

- scene: A fixed portrait terminal types the real command and resolves into three real Douyin rows.
- voiceover: "输入这一条命令，GPT 5.6 的真实抖音结果就回来了。"
- duration: 7.4s
- poster: 5.1s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/04-real-douyin-search.html
- type: feature_showcase
- persuasion: Show-don't-tell proof
- beat: anticipation → payoff
- blueprint: device-surface-showcase (Adapt)
- asset_candidates:
- data_source: data/evidence.json
- sfx: typing, click-soft

narrativeRole: Put the real product result on screen before asking the viewer to trust any technical claim.
keyMessage: One CLI command returns current, normalized Douyin search results.

Adapt: keep the persistent surface and discrete screen-state progression; the surface is a terminal,
not a browser/device mockup, and the camera stays static for readability.

Scene 1 (0.0–1.2s): a fixed 872×1080 terminal surface establishes inside the safe area, sharp 1px
border, no window controls. Header reads `REAL E2E · 2026-07-12`; only the prompt is visible.

Scene 2 (1.2–3.2s): the exact public command types across two wrapped mono lines via **type-on with
caret** (`discrete-text-sequence` + `context-sensitive-cursor`); the terminal dimensions and rows do
not move.

Scene 3 (3.2–4.4s): compact state line `searching douyin…` is replaced in place by
`3 results · errors []` using a **discrete state swap** (`discrete-text-sequence`).

Scene 4 (4.4–7.4s): three rows reveal sequentially from `data/evidence.json`: rank, trimmed real
title, author, likes, and canonical URL suffix. The first row receives a green 1px leading rule;
the final surface holds without scrolling.

## Frame 5 — Proof Stack

- scene: Four evidence rows assemble from the same E2E run and hold as a verified stack.
- voiceover: "这次 PATH 里没有 OpenCLI。返回 adapter 是 native-chrome，errors 为空，可见 Chrome 窗口和标签页，都是零到零。"
- duration: 13.0s
- poster: 9.5s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-proof-stack.html
- type: benefit_highlight
- persuasion: Reproducible technical proof
- beat: skepticism → confidence
- blueprint: grid-card-assemble (Adapt)
- asset_candidates:
- data_source: data/evidence.json
- sfx: pop, ping

narrativeRole: Convert the visual demo into four falsifiable facts from the same run.
keyMessage: The successful native run excludes OpenCLI and leaves visible Chrome state unchanged.

Adapt: keep the accumulating list signature; use hairline evidence rows rather than cards, no floating
grid, no camera move, and no invented count-up.

Scene 1 (0.0–1.5s): headline `同一次真实运行` reveals in the upper third; small mono stamp shows
`omnireach 0.14.0-alpha · bridge 0.1.1`.

Scene 2 (1.5–3.7s): row 01 slides a short distance into its fixed slot: cyan key `OPENCLI / PATH`,
green value `ABSENT`, and exact restricted PATH note.

Scene 3 (3.7–6.1s): row 02 assembles beneath it: cyan key `ADAPTER`, green mono value
`native-chrome`.

Scene 4 (6.1–8.4s): row 03 assembles: cyan key `ERRORS`, green mono value `[]`.

Scene 5 (8.4–11.7s): row 04 assembles last: cyan key `VISIBLE CHROME`, large green value
`WINDOWS 0→0` and `TABS 0→0`; the values are literal fixture fields, not animated counters.

Scene 6 (11.7–13.0s): all four rows hold. A 1px green verification rule completes left-to-right
under the stack via **SVG self-draw** (`svg-path-draw`).

## Frame 6 — Install And Challenge

- scene: The install commands snap in, then resolve to a challenge CTA and repository URL.
- voiceover: "它不替代点击和表单，只把搜索和读取做轻。装完搜一次，跑不通，就把失败案例留在评论区。"
- duration: 9.9s
- poster: 7.2s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/06-install-and-challenge.html
- type: cta
- persuasion: Risk reversal + challenge
- beat: motivation + urgency-to-act
- blueprint: kinetic-type-beats (Adapt)
- asset_candidates:
- sfx: key-press, chime

narrativeRole: Turn credibility into one concrete trial and invite useful failure reports rather than passive applause.
keyMessage: Install, run one real search, and report a reproducible failure if it breaks.

Adapt: keep the beat-by-beat CTA stack and final held lockup; use executable commands instead of a
button or logo animation.

Scene 1 (0.0–1.9s): boundary reminder `不替代交互` hard-cuts to `只把搜索 / 读取做轻`; off-white
copy with one yellow phrase, centered upper-third.

Scene 2 (1.9–4.8s): two fixed-width terminal command rows reveal one at a time via **type-on with
caret** (`discrete-text-sequence`): `uv tool install omnireach`, then `omnireach bridge install`.

Scene 3 (4.8–8.2s): yellow challenge line builds in three cues via **per-word staggered reveal**
(`dynamic-content-sequencing`): `装完搜一次。` then `跑不通，` then `把失败案例留在评论区。`

Scene 4 (8.2–9.9s): `github.com/Daily-AC/omnireach` resolves beneath the challenge with a small
off-white star outline; the URL and commands hold dead static through the final frame.
