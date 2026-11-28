# CASE FILE 029 — thumbnail plan (two angles; thumb_C = channel's old generator)
No U.S.-federal or public-domain photo of Peter Ojeda exists (the DOJ releases carry none; news mugshots are not usable). So NO face of Ojeda on any thumbnail; emotion goes into the scene and the stamps. Never show Rodriguez, Moreno or any informant's face.

## Angle A — "CONVICTED / TWICE" (document + stamp, template "evidence")
- Words (2): **CONVICTED** (yellow #FFD400) / **TWICE** (white). Tag top-left (red slanted): "ORDERS FROM A CELL".
- REAL element: crop of the DOJ verdict release (justice.gov, Jan. 13, 2016, PR 16-005) — headline "Mexican Mafia Member Who Oversaw Latino Street Gangs in Orange County for Decades Found Guilty", yellow highlight on "Found Guilty" and "Ojeda"; red rubber stamp rotated -8°: "GUILTY · 2016". Second small stamp "PLEA · 2006" is optional (both are true).
- Plate A (AI scene, FLUX): see plate_A below — empty cell block, red alarm light, a lit phone on a bunk (the emotion = alarm/threat).
- Emotion: cold red alarm light + hard shadow; no people.

## Angle B — "99 CHARGED" (real frame, versus the cell)
- Words (2): **99 CHARGED** (red #FF2A2A, giant) / **ONE MAN IN A CELL** is too long → use **99 CHARGED** only + small cream label "JULY 13, 2011".
- REAL frame: Orange County Register video of Operation Black Flag (relay clip bf1, B9TKOeNycP4, 0:00–1:30) — choose the sharpest frame of agents/officers at a door (NOT a face of a suspect; blur/crop any arrestee). Red circle ONLY if an object (door ram, line of vehicles) is fully visible and fills the circle; otherwise none. Colour pushed (saturate 1.75), ~45% of frame, text on the opposite side.
- Plate B (AI scene, FLUX) is used behind/next to the real frame as the dark split half: see plate_B.
- Emotion: shock/alarm — the dawn-raid frame plus the red number.

## FLUX plates (scenes only — no real person, no text in the picture)
- plate_A: "cinematic photo of an empty prison cell block corridor at night, one smartphone glowing on a metal bunk inside an open cell, red emergency light, long shadows, dramatic side light, dark background, high detail, film grain"
- plate_B: "cinematic photo of a row of dark unmarked SUVs and silhouettes of tactical officers from behind approaching a suburban stucco apartment complex at dawn, red and blue light on wet pavement, dramatic side light, high detail, film grain"
(plates.json for img_client: [{"name":"plate_A.png","prompt":"<plate_A>","w":1280,"h":720,"seed":1},{"name":"plate_B.png","prompt":"<plate_B>","w":1280,"h":720,"seed":2}])

## Checks before upload
Every word true and in the video (CONVICTED TWICE = 2006 plea + 2016 verdict, both in chapters II and V; 99 CHARGED = Black Flag, chapter IV). Bottom-right 220×90 empty. Look at 168×94. Tag "THE CASE · 2016", never "BREAKING".
