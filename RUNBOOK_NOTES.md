# COLD WARRANT — run notes archive (append-only; moved out of RUNBOOK.md 2026-11-23 — active rules are distilled in RUNBOOK.md "Lessons from past runs")

## Notes from run 004 (2026-11-02)
- Do the font step from §1 before `finish_ep.py`/`shorts.py`: without ~/.fonts TTFs, libass silently falls back to a generic font.
- `node graphics.mjs` needs absolute paths for spec and out dir.
- Run only ONE `encode.sh` at a time (two parallel 2-pass encodes share x265_2pass.log in the episode dir and corrupt each other). 2-pass takes ~2 h on 2 cores; a single-pass `-b:v 940k` with VBV (see run 004) takes ~35 min and lands ~76 MB.
- Don't put footage of unidentified 2011 arrestees under lines about a named or charged person — use neutral shots (officers, port, graphics).
- Map graphic: `useCounties: true` draws US county outlines (FIPS keys) for city-scale maps.

## Notes from run 005 (2026-11-03)
- Commit main (backlog, used_clips, episode files) BEFORE the §7 orphan step: `git rm -rqf .` deletes uncommitted edits to tracked files.
- Don't `pkill -f build_ep.py` / `pgrep -f ...` from a shell whose own command line contains the pattern — it kills the calling shell. Use `ps aux | grep "[b]uild_ep"`.
- `node graphics.mjs` re-renders every graphic (~5 min for ~37) — run it with nohup, not in a 2-min foreground call. Check map labels on the last frame before building (labels near the frame edge need `anchor:"end"`).
- Single-pass encode that worked: `-c:v libx265 -preset fast -b:v 860k -maxrate 1300k -bufsize 2600k` → 11:40 episode = 76 MB in ~35 min.
- Independent fact-check agent caught a real mismatch (footage-led narration vs. source text). Write narration from the source, then pick footage; footage descriptions on DVIDS are not always matched by press releases.
- Footage tags must describe what is on screen (e.g. National Guard at a port ≠ "Border Patrol").

## Notes from run 006 (2026-11-04)
- Some DVIDS clips have NO audio track (e.g. 456019, Shadowfire Tennessee). finish_ep.py now falls back to silence for those (fixed in main).
- Launch long jobs with `setsid nohup ... < /dev/null &` — a plain `nohup ... &` build was killed mid-run when the shell/container was interrupted, and build_ep.py does not resume (it re-renders every segment, ~25 min).
- Don't write `EP=... && setsid nohup cmd &` and then use `$EP` in the same command: the whole `&&` chain goes to the background, so `$EP` is empty in the foreground. Set variables with `;` first.
- On a detached HEAD after a fresh clone, push with `git push origin HEAD:main`, then `git checkout -B main <sha>` before the §7 orphan step.
- Fact-check agent flagged (and we fixed): quotes with an added subject, "according to the DEA" for what was an indictment allegation, ICE official titles, and arrest footage under lines about named defendants — tag those shots "ILLUSTRATIVE · NOT THE DEFENDANTS IN THIS CASE" or use graphics.

## Notes from run 007 (2026-11-05)
- CBP AMO DVIDS packages (e.g. 1007294) have short dip-to-black transitions between shots. Before picking start times, run `ffmpeg -i clip.mp4 -vf "scale=320:-2,blackdetect=d=0.05:pix_th=0.06" -an -f null -` on each source and keep every shot range clear of them. Also run blackdetect on video_raw.mp4 before encoding.
- Vertical (pillarboxed) DVIDS clips (829480, 952919) look bad full-frame; skip them or use `crop=` like 1026857.
- Any edit to a graphic's text changes its gfx key: re-run make_gspec.py and render the new keys BEFORE build_ep.py (it crashes mid-build otherwise).
- To fix one shot after a build, re-render only that `seg/NNN.mp4` with the same frame count, re-concat `seg/list.txt`, update timing.json `ss`, then re-run finish_ep.py (nat sound). Saves a 45-min rebuild.
- `ps | grep -E "[f]fmpeg" | xargs kill` also matches your own shell if "ffmpeg" appears anywhere in that command (heredocs included). Kill by explicit PID in a separate call.
- Keep shots ≤ 6 s: when a line gets longer after fact-check edits, add a third shot.
- Ep 006 long video posted with Metricool warning "Could not upload video thumbnail" (channel likely needs phone verification for custom thumbnails).

## Notes from run 008 (2026-11-06)
- Case numbering: when a backlog row is skipped, the next episode still gets the next CASE FILE number (backlog row 009 → CASE FILE 008, folder `episodes/008-project-wildfire`).
- DVIDS contact sheets: read the timestamps as h:mm:ss (2:48 = 168 s) — several picks were off by misreading. Check each pick against the clip duration before building.
- build_ep.py takes only ~12 min for a 12:47 episode now; single-pass x265 at `-b:v 800k -maxrate 1250k -bufsize 2500k` → 75 MB in ~30 min.
- Fact-check agent caught: comparing gang-only and total arrest counts in one sentence, "credited" vs. what the release says, judges' quotes attributed to the wrong judge type, and an unnamed arrestee labeled MS-13 from a DVIDS slate only (now: "ICE's video describes…", no face shots).
- Graphics start from a dark frame for ~4 frames — blackdetect flags these at every graphic start; that is expected, not a defect.

## Notes from run 009 (2026-11-07)
- §2 research now uses the free YouTube Data API script (Projects doc `claude/yt_research.py`) + Metricool + WebSearch — NOT vidIQ (owner rule 2026-11-06). youtube.com transcripts are blocked from the cloud (ProxyError): analyse hooks from titles/descriptions/thumbnails.
- `list` graphic: with 6 items, or with a `<br>` inside an item, the last line overlaps the footer. Keep ≤ 5 single-line items; check f0072.jpg of every list before building.
- Never rewrite video_raw.mp4 (segment fix + re-concat) while shorts.py or the encode is reading it — the Shorts came out corrupted; re-run them after the fix.
- A `while ps aux | grep -q "[g]raphics.mjs"` loop never ends when the same shell command line contains "graphics.mjs" (it matches itself). Run graphics with setsid nohup and poll in separate calls.
- Shorts must not contain graphics-only lines: put the key number in the footage line's `tag` (lower third) instead of a stat card when that line is inside a Short.
- 998143 (HITRON b-roll) has a dark fade ~210–217 s; 974720 has black at 16–18 s and 32–36 s and a night/fire shot at 28–31 s.

## Notes from run 010 (2026-11-08)
- Money/finance cases have little action footage on DVIDS. Best cash footage: 709501 (HSI Honolulu cash counting 122–127 s, cash pile 244–249 s, evidence bags 250–284 s; black at 285 s). Tag it "ILLUSTRATIVE … NOT THE … CASE". Shorts still need action: pair the case with a seizure (988986 cocaine bricks, 759057 81 vehicles) or raid b-roll (860902 HSI SRT Chicago).
- 988986 is only 15.7 s: lines over it must total < 15 s or shots repeat.
- Fact-check agent caught: quotes attributed to "the AP" that AP attributed to Garland / the U.S. attorney; linking named bankers to an unnamed network; "each deposit triggered a CTR" applied to the whole $474M; combined penalties that only add up with other regulators. Always check who said it inside a news story.
- Map graphic: a `labels` entry and a city label at the same spot overlap — move the country label ~3° away and use anchor:"end" on the city.

## Notes from run 011 (2026-11-09)
- fbi.gov refuses fetching from the cloud (WebFetch client_error; curl blocked as bot-check circumvention — don't try). Use DEA/DOJ releases, FBI-written DVIDS descriptions, and news stories that quote the FBI release; say so in sources.md.
- faster-whisper can be pip-installed but its models come from huggingface.co, which the proxy blocks — interview soundbites can't be transcribed here; don't quote interview clips you can't transcribe.
- FBI DVIDS helicopter footage (1022910) has a blue frame border: use `crop="iw*0.74:ih*0.74:iw*0.13:ih*0.13"`; it also contains a child photo at 36–44 s — never let a shot run past 35 s.
- Shot lengths = (line audio + gap) / number of shots. Validate every shot BEFORE building: start + length < clip end, no overlap with other shots of the same clip, no black windows (script in this run: check against blackdetect ranges). 1006212 (FBI KC Red Card) is mostly 3–7 s islands between black gaps; 973778 is pillarboxed after ~65 s.
- Dark night footage (1006212 at 112–116 s) is flagged by blackdetect on video_raw after grading — treat as black and replace.
- Thumbnail: Anton commas get hidden under the next line (".86" line-height). Put the number in its own block span with margin-bottom (see episodes/011 thumb.json).
- Fact-check agent caught: "the FBI made all those arrests" (partners did), truncated quotes that change meaning (Tapp "…ineffective at maintaining public safety"), a map mixing scopes (one surge vs. a summer total), "guns" for "illegally possessed weapons", and one-sided use of a critic's quote.

## Notes from run 012 (2026-11-10)
- Map/graphic element delays (`d`) must be ≤ ~2.0 s: graphics.mjs renders only the 2.4 s intro + hold frame, so labels with d=2.8–3.4 never appear (Philadelphia/Rotterdam were missing on the first render). Check the LAST frame of every map.
- Timeline items: keep `t` ≤ ~22 chars and `y` single-line ("FEB–MAY 2026" wrapped and overlapped the axis).
- 692217 (CBP press conference, 32 min, 700 MB at 720p) makes build_ep slow (~20 s per line overall). Don't put officials' faces from it under lines quoting other people (fact-check: McSwain's quote was from a July statement, not the June 21 conference).
- 891551 at ~245–260 s is an out-of-focus in-cab monitor — avoid.
- Fact-check agent caught: payment attributed to a named crewman that the affidavit doesn't support, a quote placed at the wrong event, "two officers" when one was a cadet, "court filings" for a leaked affidavit, "never accused" for MSC (→ "have not accused… not charged"), and a related pending case (Gogic, EDNY) that the ending must not ignore.
- Short line ranges must not include graphic-only lines: swap the graphic for footage in the script before building (rebuild costs ~20 min).

## Notes from run 013 (2026-11-11)
- Contact-sheet timestamps misread AGAIN (744730 "2:30" = 150 s, picked 170 → wrong shots). After the build, make a per-shot midpoint sheet labeled `L<line> <clip>@<start>` from timing.json segs and check every shot matches its line before encoding; fix single segments in place (same frame count) and re-concat.
- New shot option `vert=1` (build_ep.py): vertical phone footage (e.g. 769187, CBP Otay Mesa 2020 meth packages, 720×1280) is shown sharp in the centre over a blurred fill; shorts.py now fills the whole Short with that centre column during those segments.
- Only ONE build_ep.py at a time: a `timeout` foreground test run left a second build alive and both wrote the same segments. Check `ps -eo pid,lstart,cmd | grep "[b]uild_ep"` after launching.
- Fact-check agent caught: "four cases" when Otay Mesa had two, a paraphrase shown in quote marks (Mariscal), illustrative footage tagged as "cases in this file", a stale "this year", "Mexican national" vs "Mexican male", an invented "not in the desert between them", and missing presumption-of-innocence lines for charged drivers.

## Notes from run 014 (2026-11-12)
- New META option `mute_nat=[clip ids]` (finish_ep.py): those clips contribute no nat sound. Use it for interdiction videos where gunfire (warning shots / disabling fire) may be audible — 1008245 and 987448 in ep. 014.
- 987448 is 4:3 pillarboxed (use `pb=1`), not vertical. 1008245 scene cuts: 2.97, 7.97, 16.92, 21.92, 26.9, 36.8, 41.8, 46.85, 51.85, 66.87, 71.87, 81.88, 87.89, 100.47, 107.07, 117.75, 128.2, 132.2, 141.64 — 132 s is a close-up of a detainee's shirt logo, avoid.
- Validate shots BEFORE building with a script (start + length < clip end, no overlap with other shots of the same clip, no black windows): the first plan for 014 reused the same 10 s of the case video in five lines.
- Fact-check agent caught: IR footage credited to the helicopter that is IN the frame (it was filmed from another aircraft), Border Patrol figures pinned to a sector the article never names, a DVIDS "date" ≠ publication date, "on the day CBP announced it" for a story's "Friday", "recovered from the water" when the bales were partly still aboard, a San Diego patrol description trimmed to sound Caribbean, and a Coast Guard tactic narrated over the CBP case footage (implied where the rounds hit).
- cbp.gov blocks fetching from the cloud: use CBP-written DVIDS descriptions, verbatim reprints (pubt.io, World Border Congress, HSToday) and news that quotes the statement; say so in sources.md.

## Notes from run 015 (2026-11-13)
- Run scene-cut detection on video_raw.mp4 after the build and compare with segment edges: `ffmpeg -i video_raw.mp4 -vf "scale=320:-2,select='gt(scene,0.35)',showinfo" -an -f null -` → any cut within 0.08–0.7 s of a segment start/end is a flash (DVIDS produced features cut every 2–3 s). Ep. 015 had 13 such flashes; fixed by shifting `ss` and re-rendering single segments (a reusable helper lives in this run's notes: re-render seg/NNN.mp4 with the same frame count, then re-concat).
- Shot lengths come from the voice-over: validate the plan AFTER TTS (start + length < clip end − 0.4, no overlap with other shots, used_clips, blackdetect). A pre-TTS plan reused the same seconds of 955958 five times.
- tts_ep.py skips existing wavs by index: after moving or editing lines, remap old wavs by text and delete only changed lines (otherwise the wrong audio plays under a line).
- 956672 (USCG Stone offload feature) contains a burning go-fast at 28.7–31 s and burned-in captions at ~121–127 and ~133–147 s; 997205 is only 103 s long (cutter aerials 88–98 s) and has interviews at 25–31, 40–46, 55–60, 64 s.
- 955958/955959/955960/955961 (Stone drone/HITRON videos) are 4:3 pillarboxed → `pb=1`; 955961 is full-frame 16:9 after ~76.5 s (no pb).
- The map graphic fits bounds by width: labels near the Galápagos cluster overlap easily — check the last frame and move ocean labels into empty water.
- Fact-check agent caught: a quote placed before the event (Naylor said it afterward), "always the same" procedure (two boats stopped without shots), a one-person fact stated squad-wide, "first time in his career" vs "first case", "33–36" vs "33 or 36", "arrested" vs "suspects", "came home" to the offload port (homeport is Charleston), a tag that claimed Pacific Viper, and a Short title implying snipers fired in all 1,000 interdictions.

## Notes from run 016 (2026-11-15)
- New line/shot opt `lab=1`: finish_ep.py and shorts.py draw a persistent "FILE FOOTAGE" badge (top-right) over every footage shot of that line. Use it on all footage that is not of the case itself (fresh-case format, owner rule).
- Fresh DOJ sentencing cases often have NO case video: build from the DOJ/DEA defendant photo (compose a 1920×1080 still with PIL: framed photo + name + "SENTENCED · N MONTHS" stamp, used via META imgs) + labeled file footage + graphics. Thumbnail images of drugs next to the defendant must carry a baked-in "FILE IMAGE · NOT HIS CASE" label (fact-check rule), placed outside the bottom-right duration area.
- dea.gov and ofac.treasury.gov refuse curl from the cloud (proxy 403); the same DOJ release and photo live on justice.gov (/sites/default/files/YYYY-MM/<name>_photo.png, only ~166×222 px).
- Map arcs use keys `from`/`to` (not a/b) — a wrong key crashes graphics.mjs mid-run. graphics.mjs re-renders everything: render only missing keys with a filtered gspec (keys whose gfx/<key>/f0072.jpg is missing).
- stat graphic: a bare year like "1996" counts up and renders "1,996" — prefix "​" to disable the counter.
- `big=` overlay text > ~16 characters overflows 1920 px — keep line 1 short, put the rest in line 2.
- With few clips, write a shot allocator (allowed content ranges per clip + black + used_clips + overlaps) after TTS; the hand plan for 016 had 35 conflicts.
- Single-pass x265 `-b:v 640k -maxrate 1000k -bufsize 2000k` + AAC 128k → 16:14 episode = 88.7 MB in ~22 min.

## Notes from run 017 (2026-11-16)
- Fresh charged-not-convicted case (Ryan Wedding): "feds say / alleged" in title, thumbnail tag, every Short title, plus presumption-of-innocence lines in the cold open, the name cards and the ending. Fact-checker caught: "Cartel Boss" outside the attribution frame in the title, a pronoun that made the judge's arrest sound like Clark's, a reputed gang member stated as fact, a quote taken out of its question (Patel on why the plane landed at Ontario), fees attributed to "the indictment" that were only reported by CBC/CTV, and a Short hook "his No. 2" that read as the judge's deputy.
- New `episodes/017-ryan-wedding/alloc.py`: write the script with pool placeholders (F("POOL")), run TTS, then alloc.py resolves pools into concrete shots (one clip family per line so the tag matches, ≤ 6.2 s per shot, used_clips + blackdetect + overlap aware, Ken Burns stills as last fallback) → episode.py. Saves the 35-conflict hand plan of 016.
- DVIDS clips with traps: 1008216 (FBI drone b-roll) has SMPTE colour-bar flashes every 6–10 s (list in this run's black.txt); 859915 (HRT) has a burned-in caption at ~9–16 s and a civilian instructor interview from ~30 s; 994298 (SWAT summit) has a red caption card at ~33 s, casualty-drill shots and a rifle toward camera; 994973 (FBI Atlanta) 86–104 s are fire/ambulance vehicles and 9.6–10.3 s goes black after grading; 585171 191–205 s shows an I-9 immigration form; 955350 (FBI Top Ten board) 30–41 s shows other fugitives' faces.
- Hook frame: a `big=` overlay on a busy composed still is unreadable — bake the number into the opening still instead (img "hook").
- Re-render single segments with /home/claude/work/fixseg.py pattern (exec build_ep.py up to the render loop, call render(k, shot, same d), update timing.json segs) + concat; then finish_ep, encode, shorts — never run shorts.py while video_raw.mp4 is being rewritten.
- Single-pass x265 `-b:v 560k -maxrate 900k -bufsize 1800k` + AAC 112k → 17:48 episode = 87.5 MB.

## Notes from run 018 (2026-11-17)
- Fact-checker caught the biggest error so far: the $10M State Dept reward for Montejo Saenz was announced the SAME DAY as his arrest ("for information leading to the conviction"), so "$10 Million Fugitive" was false. Always check WHEN a reward was announced (release headline "Feds Announce Two $10 Million Rewards") — the true version ("$10M for a man they already arrested") made a better hook. Also caught: a paraphrase shown as a quote card, a wrong bail-presumption explanation (the government keeps the burden of persuasion), "founders" vs "leaders", "the court record" for a press release.
- justice.gov pages: curl gets an Akamai bot challenge (don't bypass) — use WebFetch for text; images under /sites/default/files/YYYY-MM/<name> download fine with curl.
- 935309 (HSI San Antonio SRT, Aug 2024) is near-black at 5–33 s and 63–68 s (mean luma < 10): use only 110–160 s. 877563 (Green Berets / Guatemalan K-9, 2023) is 4:3 pillarboxed → pb=1; usable 1–74, 100–174, 296–333 s. 962843 (Guatemalan sailors + NSWC interdiction exercise, Port San José, May 2025) is clean 1–76 s. 314347 (Bertholf IR chase 80 mi off Guatemala, 2009) has a title card 0–11 s, a flare/fire at ~96–106 s; pb=1.
- alloc.py (018): mixed lines (graphic + pool) now allowed — fixed shots keep their slot; pools reserved per line with priority ("BERT" first). Long graphics (> 10 s) get a second footage shot.
- Shorts must be footage-only: convert a stat/quote card inside a Short's line range into footage + `big=` overlay (≤ 16 chars, sub ≤ ~34 chars).
- The container restarted mid-encode (exit 137): x265 `-preset veryfast -b:v 600k -maxrate 950k -bufsize 1900k` + AAC 112k → 16:31 = 85.6 MB in ~17 min. Push Shorts + thumbs to the drop branch and schedule them while the long video encodes.

## Notes from run 019 (2026-11-18)
- Nothing in the 7-day window had a protagonist + federal photos + footage; widened to 14 days (USAO M.D. Ga. Nov. 6 release, life sentence). Félix Gallardo's death (Nov. 15) was rejected: the story centres on a murdered DEA agent (victim rule) and there is no U.S.-federal photo of him.
- DVIDS burned-in captions: 1006229 (FBI KC Red Card) has a text box until ~17.5 s (sheet shows 12 s — check frames, not only sheets); 1000368 has captions 12–23 s and 24–34 s and "CRUSH VIOLENT CRIME" 40–48 s; 899361 slate 0–11 s. 923153 (FBI ERT training, U.S. Army South 2024) shows Colombian police patches — tag as training. 1018364 faces are blurred by FBI.
- Fact-checker caught: an invented "quote" (paraphrase in quote marks — the DOJ release had the real words), "night" for a mid-afternoon stop, the wrong phone (girlfriend's) and an unclear Glock owner, conspiracy-wide quantities stated as the defendant's personal role, a grenade launcher pinned to the defendant's home, "same courthouse/Athens" not in the release, a mixture-weight dose calculation without the purity caveat, and an acquitted co-defendant made identifiable.
- Inserting footage into long graphic lines with a text-matching script broke META (the match hit a later dict) — edit those lines by hand or by exact anchors.
- Image (zoompan 7680) lines + parallel dub voicing/mixing slow build_ep to ~1 line / 20–40 s (132 lines ≈ 55 min). Dub voicing via Edge was fast (≈2 min/language); Hindi needed one shortening pass (late>2.5 s at 30 lines → 3 → 0).

## Notes from run 020 (2026-11-19)
- Fact-checker caught a PRODUCTION BUG: inserting new LINES with a text-anchor script landed two narration lines inside a cards3 `cards=[...]` list (silently dropped, broken cards). After every scripted insert, assert `len(LINES)` and that each entry is a 3-tuple.
- Also caught: "posted photos of himself" (release: "displayed multiple firearms in his social media profile pictures"), the ring-wide "200+ weapons" pinned on the three family members (title/thumbnail), a causal "the Eagle Pass stop set off everything" the release never states, Santa Muerte insinuation (use the DOJ caption: "a spiritual icon found among members of various Mexican drug cartels"), "two cartels" when one is unnamed, Galvan's shootout rifle as "one of the 24", "no parole" without the ~85% good-conduct caveat.
- ATF straw-purchase training video (DVIDS 350830, 2014, actors): NEVER under lines about a named person (it reads as the defendant) — only under generic lines about Form 4473 / straw purchases. Ran a fixseg pass (/home/claude/work/fixseg.py pattern: exec build_ep.py up to the render loop, re-render chosen segs with the same d, patch timing.json + episode.py, re-concat).
- DOJ seizure photos come out very dark after the still grade (saturation .6 + increase_contrast + GRADE): measure mean luma of a rendered still frame (aim ≥ 70) and gamma-lift the source (≈1.6 for dim indoor evidence photos) before building.
- Gun-trafficking footage on DVIDS: 960896 (CBP weapons display, Nogales May 2025; 52–58 s thermobaric "simulation device" boxes — skip), 960915 (CBP southbound-weapons press conference, Nogales, 30 min; wides 30–110 and 960–1830), 965069 (Laredo FO + HSI + ATF, June 2025; weapons wides 300–309, 650–674), 936098 (Bridge of the Americas; "BIENVENIDOS A MEXICO" lanes 135–178 — good neutral thumbnail frame), 891569 (CBP outbound inspections, Savannah 2023; black 276–278), 617217 (CBP + Guard vehicle inspections, Nogales 2018).
- thumb2_loc.mjs (new): thumb2.mjs with Oswald-Cyrillic / Teko-Devanagari fonts and a per-variant "font" key — localized thumbnails for non-"news" layouts are re-rendered natively from thumb2.json A (thumb_loc.mjs only fits the news layout).
- Build with parallel dub voicing/mixing: build_ep ~70 min for 149 lines (230 segs, 21 stills); finish_ep was OOM-killed (exit 137) while the Hindi mix ran — never run finish_ep and a dub mix at the same time.

## Notes from run 021 (2026-11-20, EVERGREEN SATURDAY — Aryan Brotherhood)
- First evergreen Saturday: no DOJ photos exist for the AB cases → the whole video is graphics + labeled file footage. Prison footage on DVIDS is scarce; what works (all labeled "NOT THIS CASE"): 140047 (JRCF Fort Leavenworth 2012 — empty cells 75–177, ext. 14–61, rec 192–233/248–310, visitation 323–356; title slates at 0–12, 61–75, 178–192, 234–248, 310–323), 505426 (ICE Prairieland 2017 — slates at 0–4, 28–30, 58–64, 118–136, 198–204, 302–306, 326–333, 355–359, 376+), 524999 (ICE Port Isabel 2017 — fences 216–227, phones 264–272; slates 20–26, 228–232, 284–290, 312+), 701993 (ICE Aurora 2019 — phones 68–76; slates 0–8, 190–192), 960481/960480 (Army corrections exercise, Sembach 2025 — soldiers play prisoners), 794755 (CDCR K-9 training 2021 — interviews at 8–12, 20–24, 40–46, 56–64, 76–84, 92–108), 673522 (Naval Brig Pearl Harbor — interview 12–20, 44–52, 60–80, 84–132; "BRIG DUTY" card 0–4). ICE detention centers must be tagged "(NOT A PRISON)".
- Contact sheets at 4 s miss short slates/interviews inside a shot. After the build ALWAYS run the interior-cut sheet (frames 0.25 s before/after every scene cut inside a segment) — it caught 8 slates/interviews the midpoint sheet missed.
- Translating the dub BEFORE the build (right after the fact-check) saved ~1 h: Edge voicing of 7 languages took ~5 min total today; mixes ~3 min each.
- The container restarted once mid-run (exit 137, uptime 0): background jobs die — re-check outputs (long.mp4 was complete; shorts had to be re-run).
- `dub_build.py bed` overwrites timing.json (without the build's per-seg "line" field) and nat.wav/fx.wav — back up timing.json first and run bed AFTER finish_ep.

## Notes from run 022 (2026-11-22, fresh case — "Chapo Isidro")
- Fresh capture in Mexico = no U.S. case footage. Unused Mexican-forces file footage that works (label "NOT THIS OPERATION"): 1015442 / 1016602 / 1016334 (Mexican Naval Infantry + U.S. Marines, RIMPAC 2026 — "MARINA"/"MÉXICO" patches; urban 116–163, 184–256; jungle 0–24, 44–104), 448156 (Diablo Express 2016: Mexican federal police Black Hawks 52–66, Lukeville convoy 76–111; slates 0–12, 68–75, 112–119), 1028572 (mirrored patrol with Mexican military, Tecate Sept 2026 — night, dark; slate 0–11; 160–186 night city), 974123 (FBI HQ exterior 2025, fades in at ~4–5 s), 1005660 (FBI Seattle Top Ten presser, static wide), 1020040 (HSI Omaha raid Aug 2026, faces blurred), 990363 (USCG San Diego offload Dec 2025). 992358 (Fuerzas Amigas) is mostly CBRN/mass-casualty drill with hazmat suits and mannequins — use only 0.5–23 (formation).
- 955350 (FBI Top Ten board) and 506089 (El Chapo NY arrival) are now fully used in used_clips — don't plan on them.
- White DOJ posters as full-frame Ken Burns stills: the lower-third tag and subtitles become unreadable on white. Fit posters to ~860 px height on a dark blurred bed, or darken top 260 px / bottom 340 px of full-bleed crops (episodes/022 hook2).
- shorts.py: new optional `note` per Short (persistent small line, e.g. "CHARGED, NOT CONVICTED"); Short line ranges are [first, last] contiguous — check every Short is ≥ 20 s after the build (3 of 5 were 15–18 s on the first cut).
- thumb2_loc.mjs: the "news" layout now honors `font` (Osw/Teko) for localized thumbnails; bake a localized FILE FOOTAGE label with DejaVuSansCondensed-Bold for Cyrillic.
- Fact-checker caught: 2019 indictment was a D.C. superseding (not San Diego), DOJ release month (May vs. the /2025-06/ image folder), homicide figures attributed to ICG instead of "official figures via CNN", "seized" hat (caption says "branded"), AP attributions (residents / authorities / a federal official), a misleading Short ("11th" Top Ten capture ever vs. under this administration).

## Notes from run 023 (2026-11-23, fresh case — La Nueva Familia Michoacana indictment)
- Relay worked: 17 clips requested, 15 delivered in ~25 min (2 failed downloads). Press-conference streams are static wides with a channel bug (NTD bottom-right, Forbes lower-third banner): shot opt `crop="iw*0.8:ih*0.8:iw*0.1:0"` removes both; add relay clips to META mute_nat (speech under narration). alloc.py (023) accepts `"lab": 0` in a clip's shot opts so the case's own footage gets no FILE FOOTAGE badge.
- Indictment PDFs often carry the best images: `pdfimages -list` → colour pages (jpx) are the photo pages; render with pdftoppm and crop (brothers' photos, gold-plated guns, RPG, engine cocaine). DEA fugitive photos (dea.gov) still refuse curl.
- Download EVERY clip a pool can fall back to (the LAB pool pulled 893769/994254/974123 that were not on disk → build crashed at line 33). /home/claude/work/build_resume.py (copy of build_ep.py with RESUME_BELOW=<seg idx>: keeps existing seg/NNN.mp4) resumed the build and later re-rendered single deleted segments in seconds.
- QA caught file footage of a white pickup/SUV under lines about the crash pickup and the fleeing driver — never put vehicles under lines about a specific vehicle in the case; also a Nogales port sign under the Highway 277 map. Scene-cut check found 11 flash cuts; fixed by shifting ss.
- Hook still: Ken Burns zoom + subtitles cover the bottom ~250 px — keep baked hook text above y≈900 and names under the photos clear of it.
- Single-pass H.264 (`libx264 -preset veryfast -b:v 3000k -maxrate 4500k`, AAC 160k) = 16:41 in ~25 min, 387 MB — fits the ≤ 450 MB Drive route; 2-pass x265 is no longer needed for Drive hosting.
- Fact-checker caught: Simmons' quotes attributed to Pasciucco, Bessent's 2025 quote placed as if about this indictment, "justice has found five" (implies guilt), Mexico's reward as "each", DOJ wording vs indictment wording (Barrett/AK), "first indicted"/"ever since", AP per-acre fee stated as fact, Short title implying all 33 guns were gold.

## 2026-11-28 run lessons
- finish_ep on >19 min episodes needs swap (8 GB swapfile) or it is OOM-killed.
- drive_upload names by basename: copy each long to a unique name (long029/030/031.mp4) first.
- IMG relay (FLUX plates) can take 50+ min and may never deliver; fall back to thumb2.mjs real-frame thumbs.
- DVIDS clips: check for slates/black gaps (blackdetect) and shift shots before building.
