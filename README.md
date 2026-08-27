# videos

Launch and promo video projects. Each directory is a self-contained
frame-based video build: HTML compositions, storyboard, narration script,
voice/SFX assets, and the scripts that render them.

Rendered `.mp4` files are **not** committed. They ship as
[Release assets](../../releases) so the repository history stays free of
binaries that can be re-rendered from source.

## Projects

| Project | For | Format | Length | Narration |
|---|---|---|---|---|
| [`omnireach-overdrive`](omnireach-overdrive) | [OmniReach](https://github.com/Daily-AC/omnireach) | 1080×1920 | 36s | Qwen3-TTS (Vivian) |
| [`omnireach-native-bridge`](omnireach-native-bridge) | [OmniReach](https://github.com/Daily-AC/omnireach) | 1080×1920 | 51s | Qwen3-TTS (Vivian) |
| [`omnireach-douyin-promo`](omnireach-douyin-promo) | [OmniReach](https://github.com/Daily-AC/omnireach) | 1080×1920 | 30s | none (terminal demo) |
| [`cfx-promo`](cfx-promo) | cf·arena | 1920×1080 | 35s | none (terminal demo) |

`_planning/` holds the design and plan documents for the two OmniReach
narrated shorts.

## Layout

```
<project>/
  BRIEF.md | SCRIPT.md    brief, or per-line narration script with timings
  STORYBOARD.md           shot list
  frame.md                frame-by-frame build notes
  compositions/frames/    one HTML file per frame — the actual visual source
  assets/voice/           TTS output (committed: costs an API call to redo)
  assets/sfx/             sound effects
  assets/fonts/           fonts needed to render the frames
  scripts/                generation and render helpers
  renders/                output — gitignored, published as Release assets
```

Regenerating a narration track needs a Qwen3-TTS endpoint; see each
project's `qwen_voice_request.json` for the exact request used.

## What is not committed

`renders/`, `snapshots/`, `capture/`, `.media/audio/`, `node_modules/`, and
generated BGM `.wav` files. All are reproducible from the sources here.
