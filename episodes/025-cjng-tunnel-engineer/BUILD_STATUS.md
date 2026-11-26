# BUILD STATUS — CASE FILE 025 "The Tunnel Engineer" (built 2026-11-26)

## Files
- Long: /home/claude/coldwarrant-media/episodes/025-cjng-tunnel-engineer/long.mp4 — 447,317,678 bytes (426.6 MiB; ≤450 route), 13:04.9 (784.9 s), H.265 4427k + AAC 128k
- Short (trailer): .../025-cjng-tunnel-engineer/shorts/s1.mp4 — 27.2 s, lines 3–5 (cocaine, tunnel, named man, terror charge), hook "1,933 FT / UNDER A STORE" in second 0, ends "...The Jalisco cartel." + "FULL CASE FILE ON THE CHANNEL". Short LUFS -14.1. (Changed from META lines 1–4 = 35.5 s, over 35 s and not ending on the charge; META in episode_src.py/episode.py updated. First version kept in qa/shorts_v1.)
- Subtitles file: subs_en.srt is NOT produced by this pipeline; subs.ass burned into long.mp4.

## Chapter start times (description)
0:00 Cold open
0:56 The Store
3:56 The Tunnel
6:01 The First Four
7:18 The Engineer
10:09 The Terror Charge
11:45 What's Left
(title card at 0:52; end card at 12:53)

## Audio
- ebur128 long.mp4: integrated -14.0 LUFS, LRA 2.5 LU.
- Speech 709.9 s (11:50) + gaps 74 s = 13:05 total.
- Pause histogram (82 lines): 0.5:11%, 0.6:2%, 0.7:11%, 0.8:12%, 0.9:21%, 1.0:23%, 1.1:10%, 1.2:7%, 1.3:1%, 2.4:1% — max 23% (<30%) OK. Note: all gaps >=0.5 s, no short 0.25–0.35 in-thought gaps; rhythm is slow/even-ish but not a single value.

## Validation
- alloc: 0 problems; custom shot check: no shot past clip end -0.4, none >6.2 s (footage), no overlap, none in used_clips.json, none in black ranges. 4 graphic+clip lines (39, 51, 54, 79) had clips of 6.3–11 s: fixed by adding 2–3 extra pool shots in episode_src.py.
- video_raw blackdetect: only 19 x 0.13 s dark frames, all exactly at graphic starts (expected).
- Contact sheet every 8 s (5 sheets) reviewed: no gore/bodies, no black frames, graphics readable, subtitles in frame.
- Scrubbed 3 graphic intros (title card, quote, end) and cold-open cut at 17 s: smooth.
- Footage share 86% / own graphics 14% of runtime (target 25–35% graphics not met; script has only 21 graphics).

## Fixes made during QA
1. seg 007 (line 4, "prosecutors named the man...") showed a man being helped/held by a DEA-jacket agent (looks like an arrest under the defendant's name) -> re-rendered with clip 278918@128.0 (agent emerging from hatch); timing.json/episode.py patched.
2. End card said "CLOSED" (pipeline default) for an open case -> stamp='STILL OPEN' via g:end opt; end graphic re-rendered, last seg replaced.

## Problems / not perfect
- Cold open runs 0:00–0:51 (title card at 0:52), brief said <=40 s. Not padded/cut (script is fact-checked); trim lines 5–6 if you want it tighter (needs re-voice + rebuild).
- Promise: terror charge + tunnel + 2,000+ lb cocaine named in the first 45 s; "1,933 ft" and "$45M" appear only as chapter-1/2 graphics (~3:00 and ~2:00), not in first 60 s. The terror-charge chapter is only ~1.5 min (12%) of runtime.
- 100% of footage is FILE FOOTAGE of other tunnels (2010–2022), repeated agents/tunnel interiors; no case-own footage exists. All shots tagged lab=1.
- Brand "COLD WARRANT" bug overlaps the subtitle "Case file 025." at the title card (~0:53) — pipeline default, not touched.
- Hook "1,933 FT" in the Short is not spoken in the Short's lines (only shown).
- Short shows a (government) agent crawling from a hatch under the line that names the defendant; labelled FILE FOOTAGE · NOT THE BUY 4 LESS TUNNEL.
- Heavy queue shared with 026/027: encode waited ~1.5 h on the lock.

## Housekeeping
- used_clips.json: 140 entries for episode 025 appended and committed locally (commit "025 used clips"), not pushed.
- Thumbnails not run (coordinator). Videos not committed.
