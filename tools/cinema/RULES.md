# Doc Cinema — rules for long documentaries (owner 2026-11-28)

Our own adaptation of cinematic principles for 10–20 minute faceless documentaries. Tools live next to this file:
`sound_design.py` (sound), `look.py` (picture), `library/` (real recorded sounds + music, CC0 / CC BY, see CREDITS.md).
Goal: nobody should feel "this was made by an AI". Apply inside each channel's own style and rules — the channel runbook wins on facts, legal and brand.

## 1. Sound = half of the video (five layers, never silence)
1. **Atmosphere** runs under the WHOLE video, two layers (general bed + one living detail), cut below 100 Hz, 12–18 dB under the voice. Change it at place changes (starts 0.2–0.5 s before the picture, 1–3 s crossfade). Desert/ocean/city/room/industrial/cabin beds are in `library/`.
2. **Actions**: paper, stamps, camera shutters, typewriter, radio — exactly on the frame the thing appears.
3. **Movement**: a whoosh whose PEAK lands on every chapter card / big transition.
4. **Accents**: max 1–2 per 5 minutes — riser into the key reveal, 0.2–0.5 s near-silence, impact ON the reveal frame. Loud works only next to quiet.
5. **Music** in every video: one continuous bed (no hard stops), lifted at chapters, ducked ~8 dB under the voice and 6–10 dB under impacts, ends on a phrase or fades over 2–3 s.
- Only REAL recordings (library or Openverse with CC0/CC BY). Never synthesize drones/hits in code — that is the most obvious "AI" tell. Repeats are varied (pitch ±3–6 %, gain ±1–2 dB).
- Levels: master −14 LUFS, true peak −1 dBTP; voice always on top; the main impact is the loudest SFX.
- **Event log**: while building the edit, write `events.json` (time, type: open/chapter/reveal/number/doc/stamp/photo/glitch/cut + ambience) — `sound_design.py` places everything from it frame-accurately and writes stems + `sound_qa.json`.
- QA without ears (done by the script): loudness, clipping, silences > 1 s, every reveal/chapter/number has an audible peak, waveform + spectrum PNG. Fix and re-run once. Put CC BY credits (`credits.txt`) in the description.

## 2. Picture: no default settings left on screen
- **Nothing sits still > 6 s.** Stills get a camera move with weight (`look.py move`): ease-in/ease-out, never linear, tiny hand-held drift. Every move has a reason: reveal, follow, emphasise.
- **Lens thinking**: wide for places (maps, satellite, sites), tight for details (a number in a document, a face in a photo). Push in to the detail the narrator names.
- **Three layers** where possible (foreground element / subject / background), subject on a third or deliberately centred.
- **Palette 60/30/10**: dominant tone, secondary, one accent colour reserved for the hero element (the number, the route line, the defendant). Frames must read as three tones in greyscale.
- **Finish** the master with `look.py finish`: grain 2–4 %, vignette 10–20 % in corners, gentle contrast/warmth, 1 px chromatic edge. Glow only from real light sources.
- **Transitions with intent** (`look.py join`): whip = fast scene change, dip to black = time jump, wipe = map/timeline, glitch = digital evidence, dissolve = same place/time passing. Hard cuts on the beat are fine — never random effects.
- **Motion graphics** (numbers, maps, timelines) animate with springs/ease, stagger 1–4 frames between elements, overshoot slightly and settle.
- One **slow-motion / freeze** moment per video on the key reveal (footage slowed, or a still frozen with a punch-in), sound drops low under it.

## 3. 3D hero inserts (optional, ≤ 20 s, flagship videos only)
For the ONE moment that deserves it (a structure cross-section, a reconstruction): three.js (MIT) rendered frame by frame on a GPU machine (owner's Mac or the office PC at night — never the Oracle server or a cloud sandbox). Principles: one named key light at 30–60°, warm/cool contrast, environment map, soft shadows with contact darkening, bevels on every edge, varied roughness, nothing moves linearly (anticipation → action → settle), camera with weight, motion blur + depth of field from sub-frames, light grain. Budget it: an insert must not cost more than the rest of the episode.

## 5. Motion & on-screen graphics (adapted from motion-director, MIT © sharbelxyz)
- **Frame 0 is the hook and the thumbnail frame**: a result, the hero image or one bold line — never black, never a logo fading in.
- **Nothing holds still > ~3–4 s** (`critique.py` measures it). If a hold must be longer, give it its own beat (a highlight, a number, a push to a detail).
- **One idea per frame.** A list of N points = N pictures, not one card with N rows.
- **An instrument, not a sentence**: to say "fast" show a counter stopping; "a lot", a list that fills; "time", a clock.
- **Numbers travel**: count from what the viewer knows to the new value, fill within the beat, STOP, stamp. Every figure on screen has a source — if it cannot be sourced, it does not render.
- **Arrive slow, leave clean**: entrances ease out on a long tail, exits 40–50 % shorter and accelerate out; camera eases both ways; linear only for rotation/progress. A landed line is dead still (no floating/pulsing).
- **Overlap** the next element at 30–50 % of the previous one; stagger letters 1 frame, words 60–120 ms, list items 40–80 ms.
- **Don't zoom for the sake of it**: a push removes edges (often the very text). Crop to the region and hold; push only to track a named element.
- **Transitions have a cause** (through an object, a carry, a whip, a colour flood, a dip for a time jump); 3–5 kinds per video; at most a third of seams are hard cuts.
- **Cut on the beat, change the layout on the bar**: chapter cards and reveals land on strong musical beats (`sound_design.py --beat-align` shifts the music so its accents hit the reveals).
- **Reading time**: 0.5 s + 0.3 s per word; type ≥ 2.6 % of the short side (28 px at 1080), titles 4–9 % of frame height; no em/en dashes in on-screen copy; one accent word per line in the accent colour.
- **Shorts safe zone (1080×1920)**: nothing in the top 168 px, no copy below y = 1330, nothing under the right-hand button rail.
- **Real material over drawn mockups**: real documents, footage, satellite images, photos made physical in the frame; a drawn UI/diagram is the most obviously generated thing — build only what was never recorded.

## 6. Sound timing (from motion-director's beat-grid idea)
- A sound is a visible event, never just a beat: every SFX belongs to something that changes on screen.
- The PEAK lands on the frame (light arrives before sound: early feels wrong sooner than late).
- Effects sit 3–6 dB over the bed, measured; one big hit per video section.
- The bed carries mids: < 55 % of its energy below 150 Hz, or it disappears on phone speakers (`critique.py` checks).
- One sound family per role through a video (consistent whoosh/pop), with only slight pitch/gain variation.

## 7. Before upload
`python3 critique.py final.mp4 --events events.json` → must print ОК (frame 0, frozen stretches, black gaps, loudness/true peak, mids, event accents). Fix fails, re-render once.

## 4. Review loop (cheap, every video)
Before publishing: contact sheet of 12 frames across the video → check (1) no frame is a static still with no motion, (2) the hero element is the brightest/most saturated thing, (3) text readable on a phone, (4) `sound_qa.json` clean. Fix the two worst things, re-render once. Don't polish backgrounds while the hero is weak.
