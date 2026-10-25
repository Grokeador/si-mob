---
name: si-boss
description: Build a Minecraft BOSS (big mob with attack animations) with the headless Blockbench MCP (bbmodel tools), using the si-mob steps plus boss checks the validators cannot see (lean direction, arms through the body, attack reach, every pose re-checked after a fix). Use when asked for a Minecraft boss, a big enemy or a mob with attacks.
---

# SI BOSS (SI NEWS skill, built on SI MOB)

Do every SI MOB step (Plan > Build > Paint > Animate > Check > Look > Ship) and add these boss rules. Our first boss
passed `bbmodel_validate` and `bbmodel_validate_animations` with 0 errors and was still wrong: it leaned backwards in
the attack, swung its arms through its own back, and its fists stopped in the air. Those checks only look for floating,
sinking and detached parts, so a boss needs its own checks.

1. **Silhouette first**: a boss must read as a boss from the three-quarter view: shoulders at least 1.5x as wide as
   the hips, a head smaller than the chest, long arms. Arm length (shoulder pivot to the bottom of the fist) must be at
   least the shoulder height minus the hip height, so a slam can reach the ground with a forward lean. Write these
   numbers in the plan.
2. **Find the sign before animating**: make one test clip that rotates only the torso +25 on X at 0.5 s, render it
   with `bbmodel_render` view `right` at that time, and write down whether +X leans the chest forward or backward.
   Use that sign for every lean. Delete the test clip after.
3. **Every attack has three key poses**: wind-up (the warning, at least 0.6 s so a player can see it coming), hit,
   recover. Write their times in the plan.
4. **Reach check**: at the hit time call `bbmodel_sample_pose` and compute the lowest point of each fist from the arm
   pivot, its rotation and the arm length. A ground slam passes only if a fist is within 2 px of the ground. If it
   fails, lean the torso more or bend the legs, never stretch the arm cubes.
5. **Body check**: render `right` and `three-quarter` at each key pose. An arm must never pass through the torso or
   the head from any view. If it does, swing it in front of the body.
6. **Re-check everything after any fix**: after changing ANY keyframe, render ALL key poses of ALL clips again, not
   only the one you fixed, then run both validators again.
7. **Impact**: put a locator at the fists and a `dust` particle effect (`bbmodel_particle_effect`, preset dust) keyed at
   the hit time with `set_particle_keyframe`.
8. **Names**: `_l` bones are on the model's own left (the viewer's right in the `front` view). Fix mirrored names.
9. **Ship**: export the Bedrock geometry, make the web URL, and save one `three-quarter` showcase render per key pose
   as `<name>_<clip>_<pose>.png`. Reply with what you built, every check result with numbers, and the file names.
