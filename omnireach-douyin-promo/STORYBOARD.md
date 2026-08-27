---
format: 1080x1920
duration: 30s
message: "OmniReach lets an AI agent search, parse, and safely download real web content from one terminal."
arc: Demo Loop
audience: Chinese developers and AI-agent power users
mode: autonomous
music: none
---

## Video direction

Use the remixed code-editorial system exactly: `#F6F8FA` canvas, `#1F2328` ink,
`#0969DA` as the single accent moment, and `#151618` only for terminal surfaces.
Mona Sans carries display and body; JetBrains Mono carries every command, status, and
artifact detail. The web terminal is the continuous world across Frames 2-4.

Motion uses smooth long-tail settles and one purposeful focal action at a time. With no
voiceover, on-screen cue order is the timing rail: reveal each phrase, command segment,
status row, and receipt field only when it becomes the current idea, with the proof
continuing through the back half of every frame. Frame 1 is the kinetic spike; Frame 4
allocates the deliberate long hold. During holds only the terminal caret may blink.

Keep primary content in the top 83% of the 9:16 canvas. Never use gradients, floating
decoration, breathing cards, looping motion, bounce eases, fake browser chrome, a visible
browser profile, or simultaneous independent drift. Avoid both failure modes: no
front-loaded slideshow, and no screensaver field of unrelated motion.

## Frame 1 - Can your agent reach it?

- status: animated
- src: compositions/frames/01-hook.html
- duration: 4.5s
- transition_in: cut
- scene: Search is not enough; the agent needs a trustworthy local artifact.
- type: hook
- narrativeRole: Create tension in outcome language and set up the proof-first demo.
- blueprint: kinetic-type-beats (Reproduce)
- asset_candidates: capture/assets/favicon.png
- focal: capture/assets/favicon.png
- roles: favicon.png = supporting brand mark
- poster: 3.2s

On-screen cues: `搜得到` / `读得懂` / `拿得下来吗？` / `让 Agent 真正触达网络`.

Scene 1 (0.0-0.8s): cream field; a mono `OMNIREACH / 018` index draws into the
upper-left while the blue spike mark settles once. Rule-of-thirds, sparse, 3 depth layers;
per-word staggered reveal (`dynamic-content-sequencing`) with a smooth settle.
Scene 2 (0.8-1.7s): `搜得到` kinetic beat-slams into the upper-middle at display scale;
the rest of the canvas stays empty. Centered focal, high contrast; kinetic beat-slam
(`kinetic-beat-slam`).
Scene 3 (1.7-2.7s): a cut-the-curve seam replaces it with `读得懂`, aligned on the same
baseline, then holds briefly. Centered focal; hard-cut word swap
(`discrete-text-sequence`).
Scene 4 (2.7-3.7s): `拿得下来吗？` arrives larger and occupies the top half; one blue
question mark is the frame's only accent. Centered, ~58% of the visible area; kinetic
beat-slam (`kinetic-beat-slam`).
Scene 5 (3.7-4.5s): the question compresses upward as `让 Agent 真正触达网络` resolves
beneath it and the favicon settles into a small lower-right brand position above the
keep-out band. Asymmetric 70/30; scale-swap (`scale-swap-transition`) then still hold.

## Frame 2 - One terminal, real sources

- status: animated
- src: compositions/frames/02-search.html
- duration: 8s
- transition_in: blur-crossfade
- scene: A polished web terminal types a real OmniReach search command and streams normalized results.
- type: product_intro
- narrativeRole: Land the promise by showing the uniform search contract working on a real source.
- blueprint: prompt-type-submit-generate (Reproduce, search skin)
- asset_candidates: capture/assets/demo-zero-config-wechat-search-uniform-j.gif
- focal: capture/assets/demo-zero-config-wechat-search-uniform-j.gif
- roles: demo-zero-config-wechat-search-uniform-j.gif = supporting proof thumbnail
- poster: 5.5s

The terminal types `omnireach search --on douyin --json "AI agent"`. A compact result
ledger resolves from `searching` to `3 sources normalized`, with source labels and clean
JSON fields. The benefit line is `一个终端。真实来源。统一 JSON。`.

Scene 1 (0.0-1.2s): a tall warm-navy terminal surface enters from below and settles in
the upper 72% of the canvas; the captured demo appears as a small proof thumbnail in its
status rail, not as the hero. Full-width vertical panel, 3 depth layers; window fly-in with
a fast upward settle that fully resolves before typing.
Scene 2 (1.2-4.0s): the prompt types `omnireach search --on douyin --json "AI agent"`
character by character; syntax blue and string teal provide one reading path. Locked
camera, dense code surface; type-on (`discrete-text-sequence`) with a bounded caret
(`context-sensitive-cursor`).
Scene 3 (4.0-5.3s): Enter lands; the prompt docks and a single `searching native source`
status line replaces the empty output region. The machine answers, not the cursor;
status swap (`discrete-text-sequence`) plus a finite loader rotation
(`svg-icon-enrichment`).
Scene 4 (5.3-7.1s): three normalized result rows arrive one by one in the back half, each
showing rank, source, title, and URL; the content window scrolls just enough to follow the
newest row. Tall list, dense but phone-legible; sequential blocks
(`dynamic-content-sequencing`) with capped row arrivals (`spring-pop-entrance`).
Scene 5 (7.1-8.0s): the loader dies and the footer resolves to `一个终端 · 真实来源 ·
统一 JSON`; the final row and footer hold still. Split hierarchy, terminal above statement;
state swap (`discrete-text-sequence`), no camera drift.

## Frame 3 - Bounded download, verified artifact

- status: animated
- src: compositions/frames/03-download.html
- duration: 10s
- transition_in: cut
- scene: The terminal executes the v0.18 bounded Douyin download and resolves into a verified MP4 receipt.
- type: feature_showcase
- narrativeRole: Prove the new release with truthful constraints, progress states, and a hash-verified artifact.
- blueprint: prompt-type-submit-generate (Adapt, terminal full-generate loop)
- asset_candidates: capture/assets/omnireach.gif
- focal: capture/assets/omnireach.gif
- roles: omnireach.gif = supporting brand tile in the terminal header
- poster: 7.2s

The terminal types `omnireach media download <douyin-url> --quality small
--max-size-mb 20 --json`. Status rows progress through `explicit browser auth`, `format
selected`, `size limit passed`, and `sha256 verified`. The receipt shows `MP4`,
`6,197,443 bytes`, and a shortened `4c2eb7ae...67516654` digest. No profile name,
cookie, signed URL, or third-party footage appears.

Adapt: keep the typed-command to machine-response signature; replace prose streaming with
a four-step verification ledger and a compact artifact receipt.
Scene 1 (0.0-1.3s): the existing terminal persists across the cut with a fresh prompt; the
omnireach GIF becomes a quiet header tile. Full-width vertical panel, locked camera;
a restrained handoff keeps the same terminal world continuous.
Scene 2 (1.3-4.0s): `omnireach media download <douyin-url> --quality small
--max-size-mb 20 --json` types in three readable chunks and wraps downward. Dense code
surface, top 62% of the visible area; type-on (`discrete-text-sequence`) plus anchored input
growth (`anchored-layout-expand`) and a bounded caret (`context-sensitive-cursor`).
Scene 3 (4.0-6.9s): the command submits; four status rows arrive and mutate in order:
`explicit browser auth`, `format selected`, `size limit passed`, `sha256 verified`.
Each pending dot becomes a green check as the next row arrives; asymmetric 70/30 with the
receipt space reserved below. Sequential status (`dynamic-content-sequencing`), check state
swaps (`discrete-text-sequence`), and checkmark draw (`svg-path-draw`).
Scene 4 (6.9-8.8s): the ledger shifts upward and a navy-elev artifact receipt expands from
its bottom edge: `MP4`, `6,197,443 bytes`, and `4c2eb7ae...67516654` arrive one field at a
time. Receipt dominates the lower half above the keep-out band; anchored expansion
(`anchored-layout-expand`) with sequential fields (`spring-pop-entrance`).
Scene 5 (8.8-10.0s): the status flips to `VERIFIED LOCAL ARTIFACT`; all loaders stop and
the receipt holds absolutely still. One blue verification edge is the accent; state swap
(`discrete-text-sequence`), no residual motion.

## Frame 4 - v0.18 is live

- status: animated
- src: compositions/frames/04-cta.html
- duration: 7.5s
- transition_in: crossfade
- scene: The release lockup turns the proof into a clear GitHub call to action.
- type: cta
- narrativeRole: Close on the shipped release and give the viewer one memorable place to act.
- blueprint: prompt-type-submit-generate (Reproduce, install-command CTA skin)
- asset_candidates: capture/assets/og-image.jpg, capture/assets/favicon.png
- focal: capture/assets/og-image.jpg
- roles: og-image.jpg = background dimmed to 35%; favicon.png = supporting brand mark
- poster: 5.2s

The release label `v0.18.0-alpha` lands first. Four compact tool names resolve beneath it:
`search`, `fetch`, `parse_media`, `download_media`. A terminal pill types
`github.com/Daily-AC/omnireach`, then holds with a cursor for the final two seconds.

Scene 1 (0.0-1.5s): the dimmed OG image wipes into the top half as `v0.18.0-alpha` lands
over cream, with the favicon fixed beside the version. Rule-of-thirds, editorial 60/40;
per-word reveal (`dynamic-content-sequencing`) and one blue section rule draw
(`svg-path-draw`).
Scene 2 (1.5-3.6s): four exact MCP tool labels arrive as two stacked pairs:
`omnireach_search`, `omnireach_fetch`, `omnireach_parse_media`,
`omnireach_download_media`. Dense mono list, top 65%; capped staggered arrivals
(`spring-pop-entrance`) with no bounce.
Scene 3 (3.6-5.5s): the tool list demotes upward and a `$` chip stretches into a wide
terminal pill; `github.com/Daily-AC/omnireach` types in full. Terminal pill spans ~84% of
the short edge; card morph (`card-morph-anchor`) then type-on
(`discrete-text-sequence`) with caret (`context-sensitive-cursor`).
Scene 4 (5.5-7.5s): `v0.18 已发布` resolves above the terminal pill and the composition
holds for two seconds; only the caret blinks. Centered CTA, clear bottom keep-out;
state reveal (`discrete-text-sequence`) then sanctioned static hold.
