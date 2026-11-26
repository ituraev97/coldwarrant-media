# BUILD_STATUS - CASE FILE 026 (Sexton, disabling fire off Cartagena)

## Outputs
- long.mp4: /home/claude/coldwarrant-media/episodes/026-sexton-engines-shot-out/long.mp4 - 447.6 MB (route <=450 MB), 701.0 s (11:41), HEVC 1920x1080 + AAC
- Short s1 (trailer): .../026-sexton-engines-shot-out/shorts/s1.mp4 - 30.6 s, lines 3-7 (NOT 1-6: those run 37.5 s, over the 35 s cap). Hook "10,900 LB / 175 MILES OUT" from second 0, ends on "...has not said who fired... what the record supports", then CTA "FULL CASE FILE ON THE CHANNEL". -14.2 LUFS. shorts_meta.txt still says "lines 1-6": use the 30.6 s file, title/text unchanged.
- LUFS: long.mp4 and mix.wav -14.0 (LRA 2.4).

## Chapters (YouTube)
0:00 Cold open / 0:46 Case file 026 title / 0:50 I TWO BOATS / 2:48 II THE SMALLEST SHIP / 4:26 III DISABLING FIRE / 6:55 IV AFTER THE SHOOTING / 8:07 V SEVEN DAYS LATER / 9:33 VI THE PIPELINE / 11:33 end card

## Checks
- Speech 638.4 s + gaps = 11:41 (inside 11-14 min; no padding).
- Pause histogram (69 lines): 0.5:6 0.6:5 0.7:9 0.8:14 0.9:11 1.0:12 1.1:3 1.2:6 1.3:1 2.0:1 2.4:1 -> max single gap 20% (0.8 s): PASS. Speeds 0.95-1.04 per line.
- Shots: all <=6.2 s except the end card (7.1 s, graphic); none in used_clips.json; none in black ranges; none past clip end; no same-clip overlaps. 1029779 = 13% of screen time, non-1029779 footage 69%, own graphics 14%, stills 5%.
- Black frames: only 0.07-0.13 s at graphic starts (expected). Contact sheets every 8 s of raw and final: no gore, no overlaps, subs inside frame.
- Promise: aerial of the two stopped boats runs 0:00-0:30, 10,900 lb/$89.2M/10 detained by 0:30, title 0:46.

## Fixes made during build
- alloc: lines with a graphic + 1 footage shot ran 7-10 s/shot -> added shots (episode_src.py lines 10,13,14,31,48,58,60 and others). 1029779 was reused with overlapping moments in lines 38-68 -> swapped to other pools; widened 906544 to 70 s; added O3/O4 to the MP pool.
- Verticals 1000233/991450 are SQUARE 720x720 baked into 1280x720 (black bars, build vert=1 gave black fill): 11 segments re-rendered with square crop + blurred fill (script work/c026/fixvert.py; originals in seg_orig/).
- 6 shots shifted 0.4-0.75 s so source cuts do not flash at segment edges (fixcut.py).

## Imperfections / for the coordinator
- Cold open runs 46 s to the title card (limit 40 s); lines were fact-checked so not trimmed.
- No video of the firing exists: the promise is the aerial aftermath + the record; the narration says so.
- 82% of footage is Coast Guard material, much of it FILE FOOTAGE (badged); case-own video is only 1029779 (aerial) and 1030153 (offload). Several 974643 shots are empty sea with a wake (5:28-5:44, 6:48): low visual interest.
- Own graphics are 14% (runbook target 25-35%); the script has few graphic beats.
- Subtitles are small (channel style), inside the frame.
- 1030153 (17 s, 4 shots) is a fast-cut montage clip, several source cuts within ~11 s at 9:08-9:19.
- Thumbnails not made (coordinator). used_clips.json updated (+123 entries), committed locally, not pushed.
