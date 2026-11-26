# BUILD_STATUS 027 (2026-11-26)
- long.mp4: /home/claude/coldwarrant-media/episodes/027-colonel-crespo/long.mp4, 447.5 MB (<=450), 666.2 s (11:06)
- short: shorts/s1.mp4, 34.8 s (lines 2-6, hook "30-YEAR MINIMUM / ONE OF THREE COUNTS" from 0 s, ends on "What does the indictment actually say? And what does it leave out?" + "Full story on the channel."). Built with local shorts027.py (copy of pipeline/shorts.py: CTA text + trim pads only).
- Chapters: title 0:42.6 | I The Meeting 0:46.5 | II The Charges 2:18.8 | III Santa Cruz to New York 4:06.4 | IV A Country Without the DEA 6:15.6 | V The First One 7:33.8 | VI What Happens Next 9:55.9 | end 11:01.7
- LUFS: mix.wav -14.0 integrated (loudnorm); encoded file not re-measured (ebur128 on long.mp4 timed out under load).
- Pause histogram: 59 lines, most common gap 1.0 s = 20% (<30%) OK. Speech 609 s (10.2 min), 11.1 min with gaps: inside 10-13.
- Shots: all validated (<=6.2 s footage, no black/used/overlap/end issues). Alloc post-TTS: extra pool shots added to graphic lines 10,25,27,33,39,44,58 and 2 stills to line 23.
- Black blips 0.13 s at graphic starts only (expected).
## Imperfections
- Only ONE DOJ photo exists: cold open and ch. I/II/V/VI repeat the same tilted face image (Ken Burns); lines 1, 4 single stills 7 s.
- 100% of footage is 4 file clips (CBP P-3 403639 ~60%, boats, JIATF 968690 incl. one code-screen shot); tagged NOT BOLIVIA. Repetitive; real footage/docs share = graphics+stills 30%.
- DOJ photo subtitle tag line low contrast on pale background; first-frame photo slightly tilted (source).
- Graphics-only lines 14, 50 hold 8.4 s. Short starts mid-cold-open ("Behind him, they say...").
- Chain-QA: full-size transition scrub limited to 5 frames; contact sheets made from video_raw (every 8 s) not long.mp4.
