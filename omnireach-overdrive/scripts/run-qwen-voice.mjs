#!/usr/bin/env node

import { execFileSync, spawnSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const projectDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const uvToolsDir = execFileSync("uv", ["tool", "dir"], { encoding: "utf8" }).trim();
const python = path.join(uvToolsDir, "mlx-audio", "bin", "python");
const script = path.join(projectDir, "scripts", "generate-qwen-voice.py");
const result = spawnSync(python, [script], { cwd: projectDir, stdio: "inherit" });

if (result.error) throw result.error;
process.exit(result.status ?? 1);
