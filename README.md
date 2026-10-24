# SI MOB: a Minecraft mob from one sentence (Claude Code + Blockbench MCP headless)

Two small files from the SI NEWS video "Blockbench MCP Without Blockbench".

- `.claude/skills/si-mob/SKILL.md`: a Claude Code skill with a 7-step loop (Plan, Build, Paint, Animate, Check, Look, Ship).
- `si_paint.py`: paints a box-UV texture PNG from a small JSON (Python standard library only). The headless
  Blockbench MCP server embeds a PNG but does not paint pixels; this fills that gap.

It runs on top of the headless server of **Blockbench MCP** by jasonjgardner (GPL-3.0):
https://github.com/jasonjgardner/blockbench-mcp-plugin (we used v1.10.1). This repo does not include any of its code.

## Setup (Windows PowerShell, Node 23.6 or newer)
```
mkdir models
claude mcp add bbmodel --scope project -- cmd /c npx -y github:jasonjgardner/blockbench-mcp-plugin --root ./models
$env:MCP_TIMEOUT=180000
claude
```
Copy `.claude` and `si_paint.py` into the same folder. In Claude Code, `/mcp` should list bbmodel.

Prompt: `Use the si-mob skill: build a Minecraft capybara that walks, name it si_capybara.`
Then ask: `does it look right?`

Licence: MIT. Made by SI NEWS: https://www.youtube.com/channel/UC4m6veQiZdc_pAfxKQluRgA
