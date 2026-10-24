---
name: si-mob
description: Build a textured, animated Minecraft Bedrock mob with the headless Blockbench MCP (bbmodel tools), then check it and look at it before saying it is done. Use when asked to make a Minecraft mob, entity or creature model.
---

# SI MOB (SI NEWS skill)

Work in this order and do not skip a check. File paths in bbmodel tool calls are relative to the server's model
folder (`--root`): write `fox.bbmodel`, never `models/fox.bbmodel`. `si_paint.py` runs in the project folder, so its
`out` is `models/<name>_tex.png` and `bbmodel_add_texture` gets `<name>_tex.png`.

1. **Plan**: list the parts (groups and cubes) with sizes in pixels, and a 64x64 box-UV layout: each cube gets a
   `uv_offset` that does not overlap another cube's area (a box-UV area is (2*d + 2*w) wide and (d + h) tall).
2. **Build**: `bbmodel_create` with format `bedrock`, then ONE `bbmodel_edit` batch with every group and cube,
   pivots (`origin`) at the joints (legs at the hip, head at the neck, tail at its base).
3. **Paint**: write a `paint.json` with one rect per box-UV area (main colour, plus a lighter belly/face and darker
   tips), run `python si_paint.py paint.json`, then `bbmodel_add_texture` and `assign_texture` to every cube.
4. **Animate**: `add_animation` (loop) and keyframes with `set_keyframe`: opposite legs swing in pairs, the tail and
   head follow half a beat later.
5. **Check**: `bbmodel_validate` and `bbmodel_validate_animations`. Fix every problem they report and run them again
   until they are clean.
6. **Look**: `bbmodel_contact_sheet` to a PNG and look at it. If a part floats, clips or the texture is wrong, fix it
   and render again.
7. **Ship**: `bbmodel_export_bedrock_geometry`, and `bbmodel_web_url` so the model opens in the Blockbench web app.
   Reply with what you built, what the checks said, and the file names.
