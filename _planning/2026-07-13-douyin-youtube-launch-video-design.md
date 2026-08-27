# Douyin and YouTube Shorts Launch Video Design

Date: 2026-07-13
Status: Approved for implementation

## Context

Omnireach has eight GitHub stars and seven external stargazers. The repository converted two
new stars after the native Chrome bridge release, but GitHub traffic shows almost no tracked
external referrers. Previous distribution work produced launch copy and static assets, while
Show HN, Reddit, and V2EX publication did not complete. A short vertical video is the next
distribution asset because it can demonstrate the product instead of repeating repository
claims.

The user approved a faceless production: real terminal evidence, burned Chinese captions,
and Mandarin TTS. The selected visual direction is the high-impact hybrid option, and the
selected narrative is problem, proof, then challenge. The primary call to action is to install
and run one real search, not to ask directly for a star.

## Goal

Produce one polished 45-55 second 9:16 video that can be posted unchanged to Douyin and
YouTube Shorts. It must make a narrow, reproducible promise:

> For read-only Douyin search, Omnireach can reuse the current Chrome login without invoking
> OpenCLI and without leaving a visible Chrome window or tab behind.

The video should drive technically credible trials, comments containing failure cases, and
secondarily GitHub stars.

## Audience

The primary audience is Chinese-speaking developers using coding agents, Claude Code, Codex,
MCP tools, Playwright, or browser-backed research workflows. They recognize terminal output
and distrust vague AI-tool marketing. The video therefore leads with a familiar irritation,
then spends most of its runtime on inspectable evidence.

## Format

- Canvas: 1080 x 1920, 9:16 portrait.
- Duration: target 50 seconds; acceptable range 45-55 seconds.
- Frame rate: 30 fps.
- Delivery: H.264 MP4 with AAC audio.
- Captions: simplified Chinese, burned into the video, inside platform-safe vertical margins.
- Voice: neutral, energetic Mandarin TTS; no face and no imitation of a real person.
- Audio: subtle original or generated interface sounds only; no copyrighted music.
- Cross-posting: the same master is used for Douyin and YouTube Shorts.

## Visual Direction

Use the approved high-impact hybrid direction:

- near-black `#111315` background;
- off-white primary text;
- yellow `#ffcc38` for the hook;
- green `#50e878` for verified success;
- cyan `#58d4e5` for technical labels;
- red only for a failure or pain signal;
- no gradients, decorative blobs, fake browser chrome, or stock footage.

The typography alternates large kinetic Chinese headlines with a compact monospace terminal.
The first two seconds use oversized text. Evidence frames slow down and keep stable dimensions
so viewers can read the adapter, error, result, and window-count fields without layout shift.

Existing static launch assets establish the brand, but the video is rebuilt for 9:16 rather
than cropping the 3:4 cards. The actual product output is the primary visual asset.

## Narrative Timeline

### 0-3 seconds: Hook

Large kinetic headline:

> Agent 搜个抖音，别再弹 Chrome

A short alert sound and a deliberately abrupt terminal-window motif establish the pain.

### 3-9 seconds: Scope the problem

Explain that search and reading are read-only tasks and do not always need the full
Playwright interaction stack. Do not claim that Omnireach replaces Playwright. A small line
keeps the boundary explicit: clicks, forms, uploads, and visual checks still use Playwright.

### 9-16 seconds: Product reveal

Reveal `OMNIREACH` and the native bridge path. Show the current Chrome login on one side and
the localhost bridge on the other without displaying cookies, credentials, or profile data.
State that the extension does not request cookie, debugger, or all-URLs permissions.

### 16-29 seconds: Real command and results

Animate the real command:

```bash
omnireach search "gpt5.6" --on douyin --limit 3 --json
```

Use a fresh, real native search response captured during production. Show three result rows
with real titles and authors, then focus on one canonical Douyin URL. Long descriptions are
trimmed visually but not altered semantically.

### 29-41 seconds: Proof stack

Present the verified facts in sequence:

- OpenCLI is absent from `PATH`;
- `adapter: native-chrome`;
- `errors: []`;
- visible Chrome windows and tabs: `0 -> 0`.

These are evidence from one end-to-end run, not benchmark generalizations. The video must not
reuse the older Playwright timing numbers as if they measured the native Douyin bridge.

### 41-50 seconds: Challenge CTA

Show the install command and repository:

```bash
uv tool install omnireach
omnireach bridge install
```

Primary spoken and captioned CTA:

> 装完搜一次。跑不通，把失败案例留在评论区。

`github.com/Daily-AC/omnireach` and a restrained Star icon remain visible as secondary cues.

## Voice Script

The production script is:

> Agent 搜个抖音，怎么又把 Chrome 弹出来了？搜索和读取是只读任务，没必要每次都
> 启动整套 Playwright。Omnireach 直接连接你已经登录的 Chrome，只继承登录态，不读取
> 密码。输入这一条命令，GPT 5.6 的真实抖音结果就回来了。注意，这次 PATH 里没有
> OpenCLI，返回 adapter 是 native-chrome，errors 为空，可见 Chrome 窗口从零到零。
> 它不替代点击和表单，只把搜索和读取做轻。装完搜一次，跑不通就把失败案例留在
> 评论区。

The edit may adjust pauses or remove filler but must preserve every technical boundary.

## Evidence Capture

Before rendering, run a fresh forced-native search through the published global CLI with a
`PATH` that excludes OpenCLI. Capture:

- the complete JSON response;
- extension bridge status and version;
- visible Chrome window and tab counts before and after;
- the exact command and timestamp.

Store a sanitized production fixture beside the composition. It may contain public result
titles, authors, and URLs, but no token, local bridge credential, profile path, cookie, or
private browser data.

## Deliverables

- final 1080 x 1920 MP4;
- final-frame and cover PNG;
- editable HyperFrames composition and data fixture;
- Mandarin TTS track, caption timing, and any generated sound effects;
- Douyin title, caption, hashtags, and pinned-comment draft;
- YouTube Shorts title, description, tags, and pinned-comment draft.

The video is presented for review before any upload. Posting to either account is a separate
external action and requires action-time confirmation after the final file is approved.

## Verification

- Full video duration is within 45-55 seconds.
- Resolution is exactly 1080 x 1920 at 30 fps.
- Audio and video streams are present and synchronized.
- Captions fit inside platform-safe margins and remain legible on a phone-sized preview.
- No headline, terminal row, or CTA clips or overlaps.
- The first, command, result, proof, and CTA beats are checked as rendered frames.
- The final MP4 is watched from start to finish.
- Claims match the fresh production fixture.
- The deliverable contains no secret, private path, or browser-session data.

## Non-Goals

- Claim that Omnireach replaces Playwright for interaction.
- Compare performance using numbers not measured in the production run.
- Show the user's face, voice, account identifiers, browser profile, or credentials.
- Buy engagement, request reciprocal stars, or automate platform voting.
- Upload before the user reviews the finished video.
