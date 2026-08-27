---
format: 1920x1080
duration: 35s
message: "Codeforces training, from finding a problem to an accepted submission, in one CLI built for humans and coding agents"
arc: Demo Loop
audience: competitive programmers and friends who use coding agents
mode: autonomous
music: none
---

## Video direction

- Palette: warm cream is the field, warm ink is the terminal, seafoam carries secondary surfaces, and coral appears once per frame as the decisive accent. Type roles come only from `frame.md`: display for editorial claims, body for supporting copy, mono for commands and output.
- Motion grammar: each frame behaves as one directed shot with long-tail, smooth motion. Text and terminal states reveal at their semantic cue across the full shot; state swaps are discrete and cursorless, while camera movement is limited to one purposeful push or pull per frame. During holds, only a block caret or tiny status indicator may remain alive.
- Rhythm: Frames 1 and 2 build quickly, Frame 3 expands with measured momentum, Frame 4 carries the densest proof sequence, and Frame 5 deliberately holds the install command and URL for the final half. Every composition keeps important content in the top 83% of the canvas.
- Never: gradients, glows, heavy shadows, browser chrome, real cursors, decorative UI clutter, floating ambient objects, bouncy entrances, slideshow front-loading followed by dead time, or screensaver motion where elements drift independently.

## Frame 1 — Train, don't tab-hop

- scene: Editorial hook resolves into the cfx name above a held terminal surface
- voiceover: ""
- duration: 5s
- transition_in: cut
- status: animated
- src: compositions/frames/01-train-dont-tab-hop.html
- type: hook
- persuasion: Friction reduction
- beat: recognition to relief
- blueprint: kinetic-type-beats (Adapt)
- asset_candidates:

narrativeRole: Name the outcome before showing any commands.
keyMessage: Train on Codeforces without stitching together tabs, scripts, and copied samples.

Adapt: keep the escalating type-beat signature and final brand resolve; replace full-screen slogan cycling with three workflow-friction words that collapse into one terminal-first product lockup.
Scene 1 (0.0–1.1s): on the warm cream field, `FIND` lands in display type, then hard-cuts to `COPY`, then `SWITCH`; each word occupies the upper-center at hero scale while a thin coral rule advances beneath it — centered, sparse, 3 depth layers, hard-cut word swaps.
Scene 2 (1.1–2.6s): the three words split-slide toward opposite edges and clear as `Train, don't tab-hop.` reveals by phrase in the upper third; a warm-ink terminal surface rises from below and settles without bounce — asymmetric 60/40, display claim dominant, masked slide plus spring-pop entrance.
Scene 3 (2.6–4.1s): inside the terminal, `$ cfx` types character-by-character behind a coral block caret; the camera performs one slow push toward the prompt while the small label `CODEFORCES TRAINING CLI` draws in above the surface — layered-depth, terminal at least 55% of frame, type-on plus coordinate-target zoom.
Scene 4 (4.1–5.0s): the prompt enlarges and resolves into a compact `cfx` wordmark beside the line `built for humans + coding agents`; all movement settles and the lockup holds cleanly into the cut — rule-of-thirds lockup, scale-swap transition, deliberate still hold.

## Frame 2 — Find the right problem

- scene: A real filtered search command types in and structured problem results stream beneath it
- voiceover: ""
- duration: 7s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/02-find-the-right-problem.html
- type: product_intro
- persuasion: Show-don't-tell proof
- beat: curiosity to control
- blueprint: prompt-type-submit-generate (Adapt)
- asset_candidates:

narrativeRole: Introduce cfx by completing the first useful action.
keyMessage: Search by topic, rating, tags, contest, and solved state from one command.

Adapt: keep the typed-command-to-progressive-response signature; use a real cfx terminal query and real Codeforces result rows instead of a graphical search composer.
Scene 1 (0.0–0.8s): the transition lands on a large warm-ink terminal occupying the right two-thirds, with `01 / FIND THE RIGHT PROBLEM` seated upper-left and a coral prompt marker blinking once — asymmetric 70/30, terminal dominant, window settle.
Scene 2 (0.8–3.2s): `$ cfx problem search "shortest path" --min-rating 1400 --max-rating 1800 --tag graphs --unsolved` types rapidly across two wrapped lines; the command area expands downward at the wrap while the camera makes a single restrained push toward it — layered-depth, mono command hero, character typing plus anchored-layout expand.
Scene 3 (3.2–5.6s): the caret snaps off and result rows arrive one at a time, each pushing the prior row upward: `520B  Two Buttons  1400`, `1418C  Mortal Kombat Tower  1500`, `1365D  Solve The Maze  1700`; rating values stamp in coral only after each title lands — full-width terminal strip, structured hierarchy, dynamic-content sequencing with staggered row entrances.
Scene 4 (5.6–7.0s): a slim metadata rail adds `graphs · shortest paths · unsolved`, then the first row receives a seafoam selection bar; the completed result state holds long enough to read with only a quiet block caret at the next prompt — asymmetric result grid, press-state color swap, deliberate hold.

## Frame 3 — Start the whole round

- scene: One contest command expands into a complete A-D workspace with statements, samples, templates, and agent policy
- voiceover: ""
- duration: 8s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-start-the-whole-round.html
- type: feature_showcase
- persuasion: Feature-to-benefit translation
- beat: momentum and clarity
- blueprint: device-surface-showcase (Adapt)
- asset_candidates:

narrativeRole: Prove that discovery becomes a ready-to-solve local workspace.
keyMessage: One command creates the contest and every problem workspace atomically.

Adapt: keep the surface-expansion signature; treat the terminal as the device surface and let one contest command unfold into a tactile local workspace rather than presenting screenshots.
Scene 1 (0.0–1.4s): `02 / START THE WHOLE ROUND` anchors upper-left while a compact terminal slab enters from the right and types `$ cfx contest start 4`; a small `Codeforces Beta Round #4` label resolves above it — asymmetric 60/40, 3 depth layers, surface push-in plus character typing.
Scene 2 (1.4–3.3s): on submit, the terminal widens horizontally and four problem tiles emerge from its lower edge in sequence, labeled `A`, `B`, `C`, `D`; the camera pulls back just enough to reveal the full set — full-width strip, terminal-to-workspace hierarchy, card-morph anchor plus center-outward expansion.
Scene 3 (3.3–6.2s): each tile opens in place to expose the same working kit, one layer per beat: `statement.md`, `samples/`, `main.cpp`, `AGENTS.md`, `session.json`; a top rail counts `4 problems` and `7 samples` as the files populate — modular grid, dense but ordered, dynamic-content sequencing plus count-up.
Scene 4 (6.2–8.0s): the tiles align into a clean local tree headed `cf-contest-4/`; a coral brace links all four workspaces back to the original command, completing the surface-expansion signature before the frame settles — rule-of-thirds tree, 3 depth layers, SVG path draw and held completion state.

## Frame 4 — Agent, test, submit

- scene: The terminal advances through agent guidance, local sample checks, explicit submission, and an accepted verdict
- voiceover: ""
- duration: 9s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/04-agent-test-submit.html
- type: feature_showcase
- persuasion: Risk reversal through visible checks
- beat: trust to triumph
- blueprint: agent-progress-theater (Adapt)
- asset_candidates:

narrativeRole: Show the safety and proof loop that makes agent-assisted training credible.
keyMessage: The agent coaches, local tests prove the solution, and submission stays explicit.

Adapt: keep the staged progress-theater signature; replace a generic agent task list with cfx's explicit coach-test-submit-verdict loop, with no autonomous submission implied.
Scene 1 (0.0–1.5s): `03 / AGENT, TEST, SUBMIT` sits upper-left while a two-column terminal workspace settles in: the left rail lists `hint`, `review`, `test`, `submit`; the right pane opens on `AGENTS.md` and highlights `Coach first. Submission is explicit.` — asymmetric 30/70, terminal dominant, panel reveal plus selection highlight.
Scene 2 (1.5–3.6s): the active rail state steps from `hint` to `review`; concise agent log rows appear beneath the policy, then collapse into `$ cfx test` at the next prompt — layered-depth, clear active-state contrast, discrete-text sequence and action-log row entrances.
Scene 3 (3.6–5.4s): sample checks populate one by one as green-neutral seafoam rows, ending on `all samples passed`; a coral checkmark draws only after the final row completes — full-width result strip, check sequence, SVG path draw with status-heading tense flip.
Scene 4 (5.4–7.1s): `$ cfx submit --yes` types in full and pauses before Enter, making the explicit gate visible; on submit, the control compresses once and the pane swaps to `submitted` — centered prompt emphasis, character typing, press-release spring and scale-swap transition.
Scene 5 (7.1–9.0s): `$ cfx status --wait` appears at the next line; status phrases advance `waiting` then `judging`, resolving to a large `OK · Accepted` stamp while all four rail steps receive checks — asymmetric 60/40 climax, progressive status theater, coral verdict stamp and deliberate final hold.

## Frame 5 — Open source, one command away

- scene: The workflow clears to a large cfx lockup, install command, and GitHub URL
- voiceover: ""
- duration: 6s
- transition_in: squeeze
- status: animated
- src: compositions/frames/05-open-source.html
- type: cta
- persuasion: Frictionless next step
- beat: motivation to act
- blueprint: prompt-type-submit-generate (Adapt)
- asset_candidates:

narrativeRole: Turn interest into an immediately executable next step.
keyMessage: Install cfx or inspect the source at github.com/Daily-AC/cfx.

Adapt: keep the install-command end-card signature; promote the open-source repository and typed install command, with the caret as the only motion during the final hold.
Scene 1 (0.0–1.2s): the accepted stamp contracts into the coral dot of a large `cfx` lockup, while `Train. Test. Submit.` builds underneath in three compact display beats — centered hero, sparse 3 depth layers, scale-swap transition plus discrete word build.
Scene 2 (1.2–3.4s): the lockup demotes into the upper third as a `$` chip stretches into a wide warm-ink terminal pill; `go install github.com/Daily-AC/cfx/cmd/cfx@latest` types character-by-character across it — centered terminal CTA, card-morph anchor plus type-on.
Scene 3 (3.4–4.5s): `github.com/Daily-AC/cfx` fades in below with a thin seafoam repository rule and the small label `OPEN SOURCE · NO OPENCLI`; hierarchy stays locked while the typed command finishes — centered stacked lockup, quiet metadata fade-in.
Scene 4 (4.5–6.0s): the final card holds completely still for readability; only the coral block caret blinks at the end of the install command — deliberate end hold, no exit animation.
