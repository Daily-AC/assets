# Omnireach Native Bridge Short-Video Publishing Copy

Final master: `videos/omnireach-native-bridge/renders/omnireach-douyin-shorts.mp4`

Repository: https://github.com/Daily-AC/omnireach

## Douyin

### Title

Agent 搜个抖音，别再弹 Chrome｜Omnireach 真实 E2E

### Caption

只读搜索不需要每次启动整套 Playwright。

这次是真实运行：受限 PATH 里没有 OpenCLI，返回 `adapter: native-chrome`，`errors: []`，
可见 Chrome 窗口和标签页都是 `0 -> 0`。

它不替代点击、表单、上传和视觉检查，只把搜索和读取做轻。

```bash
uv tool install omnireach
omnireach bridge install
```

装完搜一次。跑不通，把可复现的失败案例留在评论区。

#AI编程 #Agent #ClaudeCode #Codex #开源工具 #抖音搜索

### Pinned Comment

真跑挂了请留：系统版本、Chrome 版本、Omnireach 版本、完整 `errors[]`，以及
`omnireach doctor --json` 里和该源相关的部分。我按真实失败案例修。仓库在视频末尾；
觉得确实有用再 Star。

## YouTube Shorts

### Title

Agent 搜抖音不再弹 Chrome：Omnireach Native Bridge 实测 #Shorts

### Description

Omnireach reuses your existing logged-in Chrome session for read-only Douyin search through a
narrow native bridge. This real run excluded OpenCLI from `PATH`, returned
`adapter: native-chrome` with `errors: []`, and kept visible Chrome windows and tabs at `0 -> 0`.

It does not replace Playwright for clicks, forms, uploads, downloads, screenshots, or visual
verification. It makes supported search and read paths lighter.

Install:

```bash
uv tool install omnireach
omnireach bridge install
```

Repository: https://github.com/Daily-AC/omnireach

Run one real search. If it fails, leave a reproducible case with your OS, Chrome version,
Omnireach version, and complete `errors[]`.

### Tags

omnireach, AI agent, Claude Code, Codex, MCP, read-only agent search, browser automation,
Douyin search, Chrome extension, open source, developer tools

### Pinned Comment

Failure reports are more useful than generic feedback. Please include OS, Chrome, Omnireach,
the source/query, complete `errors[]`, and the relevant `omnireach doctor --json` section.
If the native bridge genuinely saves you time, the repository link is above and a Star helps
other developers find it.
