# COLD WARRANT — daily production runbook

One run = one long episode (10–14 min, English) + 5 vertical Shorts, uploaded here and scheduled in Metricool for one US day.
Read this whole file before starting. Episode 001 (`episodes/001-ms13/`) is the reference for structure, pacing and style.

## 0. Context
- Channel bible: Projects doc `claude/cold-warrant-bible.md` (rules, brand, schedule). Read it first.
- Metricool brand "COLD WARRANT": blogId **7731358**. Publish timezone **America/New_York**.
- Schedule per US day: Shorts 09:00, 11:00, 13:00, 15:00, 17:00 ET; long episode 12:00 ET. (21:00 slot dropped 2026-11-06 — weakest in stats.)
- Do NOT set isAiGeneratedContent (owner's decision; we use only real public-domain footage, a generic TTS narrator and code-generated music — no realistic AI imagery).

## 1. Setup (fresh container)
```bash
# repo (needs add_repo owner=ituraev97 repo=coldwarrant-media access=push first)
git clone --depth 1 https://github.com/ituraev97/coldwarrant-media /home/claude/coldwarrant-media
cd /home/claude/coldwarrant-media/pipeline && npm i
pip install --break-system-packages kokoro-onnx soundfile scipy fonttools brotli
mkdir -p /home/claude/tts && cd /home/claude/tts && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
# fonts for subtitle burn-in (libass needs TTF)
cd /home/claude/coldwarrant-media/pipeline/node_modules/@fontsource && mkdir -p ~/.fonts && python3 -c "
from fontTools.ttLib import TTFont; import os
for s,d in [('anton/files/anton-latin-400-normal.woff2','Anton-Regular.ttf'),('oswald/files/oswald-latin-700-normal.woff2','Oswald-Bold.ttf'),('oswald/files/oswald-latin-500-normal.woff2','Oswald-Medium.ttf'),('ibm-plex-mono/files/ibm-plex-mono-latin-600-normal.woff2','IBMPlexMono-SemiBold.ttf')]:
  f=TTFont(s); f.flavor=None; f.save(os.path.expanduser('~/.fonts/'+d))" && fc-cache -f
```
Playwright + Chromium and ffmpeg (libx265) are preinstalled.

## 2. Pick the case
- FIRST (owner rule 2026-11-06): search & competitor research — vidIQ keyword_research (research + rising) and outliers (long + short) for the top backlog candidates; WebSearch fallback if vidIQ is not connected. Save `research/YYYY-MM-DD.md` (keywords, outliers, chosen case + why, 3 title candidates). The case, the long title (number + action + main keyword), description lines 1–2, tags and Shorts titles all come from this research. New cases with demand may be added to backlog.md if they pass the footage rule.
- Target date = tomorrow's date in America/New_York at run time. First call Metricool getScheduledPosts for blogId 7731358 around that date: if a YouTube long video is already scheduled for it, do not produce anything — just report.
- Take the first `todo` row in `backlog.md`. Before committing to it, check footage: DVIDS search API (`https://api.dvidshub.net/search?api_key=KEY&q=...&type[]=video`) must give at least 6 relevant public-domain videos (ICE/HSI, FBI, DEA, CBP, Coast Guard, DOJ). If not, mark the row `skip (footage)` and take the next.
- Never reuse a clip time range listed in `used_clips.json` (each clip id + start second used before). Different moments of the same clip are fine, but prefer new clips.

## 3. Research (facts decide everything)
- Primary sources first: justice.gov press releases, ice.gov, fbi.gov, court records; then AP/Reuters/NBC/LA Times/InSight Crime; Wikipedia only as a map to primary sources.
- Every number, date, name and quote in the script must come from a page you actually opened. Save them in `episodes/NNN-slug/sources.md` (claim → URL).
- Names: only people convicted, or officials. Charged-but-not-convicted → say "charged", "alleged", and add the presumption-of-innocence line.
- No fabricated scenes, no invented dialogue, no reenactments presented as real.

## 4. Script → `episodes/NNN-slug/episode.py`
- Copy the structure of `episodes/001-ms13/episode.py`: `LINES = [(spoken_text, shots, opts), ...]`, `DISPLAY` (spoken → on-screen spelling), `META` (case, label, title, imgs, credit, shorts).
- 1,600–1,900 words → 10–12 min at narration speed 1.06 (TTS_SPEED). Episode must stay ≥ 10:00. Cold open (≤40 s, the most dramatic verified moment + the question) → `g:title` → 5–6 chapters (`g:chapter` with n, t, case) → close + `g:end`.
- Write numbers/years as words in spoken text (Kokoro), add digit forms to DISPLAY. Respell hard names for TTS and map them back in DISPLAY (check with `Kokoro(...).tokenizer.phonemize(word,"en-us")`).
- Shots: 2–3 per line, each 2.5–6 s. ~25–35% of screen time should be our own graphics (maps, stats, documents, timelines, lists) — this is what makes the channel original.
- Graphics available in `pipeline/graphics.mjs`: title{case,title,sub}, chapter{case,n,t}, stat{a,b,c}, quote{q,w}, doc{header,title,body,stamp,source}, list{kicker,title,items,footer}, phases{kicker,title,left,right,active,total,footer}, cards3{kicker,title,cards}, timeline{kicker,title,events}, map{map:{bounds|useUS,highlight,cities,arcs,labels,topPad},kicker,title,footer}, end{case,label}.
- Content rules: no blood, wounds, bodies or execution footage (if any frame shows them, cut it). Never use DVIDS videos titled "Lethal Kinetic Strike" or any footage of people being killed or injured. Gangs are never glamorized; always consequences, victims, courts. No gang music or recruitment videos.

## 5. Build
```bash
EP=/home/claude/coldwarrant-media/episodes/NNN-slug; CL=/home/claude/clips; P=/home/claude/coldwarrant-media/pipeline
# download clips: GET https://api.dvidshub.net/asset?api_key=KEY&id=video:ID -> files[] (720p) -> $CL/ID.mp4
python3 $P/tts_ep.py $EP am_michael
python3 $P/make_gspec.py $EP
cd $P && node graphics.mjs $EP/gspec.json $EP/gfx
python3 $P/build_ep.py $EP $CL          # ~40–60 min on 2 cores — run in background
python3 $P/finish_ep.py $EP $CL
bash $P/encode.sh $EP $EP/long.mp4 95   # must stay < 100 MB (GitHub file limit)
python3 $P/shorts.py $EP $EP/shorts
cd $P && node thumb.mjs $EP/thumb.json $EP   # thumb_A (main) + thumb_C (alternative for Test & Compare)
```

## Motion & pacing rules (owner feedback after ep. 001 — mandatory)
- No artificial zoom/drift/shake on video footage. Use the camera's own motion only. (Per-frame scale/crop rounds to whole pixels and makes the picture twitch.)
- Graphics: animate in, then hold perfectly still until the cut. Never start a zoom or pan after the intro animation ends.
- Ken Burns only on still photos, and only via zoompan on a 4×-supersampled canvas (already in build_ep.py).
- Narration speed 1.06 (default in tts_ep.py). Do not go back to 0.94 — it felt slow.
- Before upload, scrub the transitions from intro→hold on 3 graphics and 3 footage cuts at full size: anything that jumps or wobbles is a blocker.

## Shorts selection rule (owner, 2026-11-06 — based on channel stats)
- Every Short = an ACTION moment on real footage (boarding, interdiction, raid, tunnel/seizure reveal, pursuit) + a concrete NUMBER in title and hook (arrests, tons, pounds, officers, years, dollars).
- Winners so far (~1,100–1,400 views each): "267 Arrests, One Gang", "Coast Guard Jumps Onto a Moving Narco-Sub", "12,000 Pounds of Cocaine in One Semi-Sub", "32 Tons of Marijuana Under the Border".
- Losers (11–135 views): explainers about names, history or structure — "What Does MS-13 Actually Mean?", "MS-13 Had a Board of Directors", "62 Killed in One Day — How El Salvador Responded". Don't make these.
- Title = number + action, ≤ 70 chars. Choose META["shorts"] line ranges whose footage shows that action.
- LENGTH (owner, 2026-11-06, vidIQ niche data): YouTube Shorts = 20–35 s (2–4 lines). Start on the action shot, number spoken and on screen in the first second; no graphics-only lines inside a Short. Niche breakouts are 9–31 s pure action (Coast Guard boarding 0:09–0:31 → 165K–2.4M views); our 40–50 s Shorts held viewers only 6–20 s.
- TikTok (only if the brand has TikTok connected in Metricool — COLD WARRANT has none as of 2026-11-06): separate cuts of 61–90 s (TikTok rewards videos over 1 minute). Do NOT trim those to YouTube length.

## Long-video packaging (vidIQ niche data, 2026-11-06)
- Our long videos got 3–12 views each; Shorts brought 17.5K views but only 3 views came from "related video". Long titles must use the same number + action formula as winning Shorts, front-loaded: e.g. "976 Gang Arrests in Six Weeks: Project Wildfire", "DEA … — 41 Arrested & 11 Tons Seized" (niche breakouts 12K–36K views on 1K-sub channels), or a person-hook: "The Customs Officer Who Weighed One Pallet — and Stopped $210M in Cocaine" (only if true and sourced).
- Search demand worth targeting with real, sourced cases: "how every cartel boss died / was caught" (~26K searches/mo, competition 48), "sinaloa cartel history" (~4K, competition 27), "chapo guzman" (+155%), "mafia vs cartel" (low competition).
- Competitor channels like FBISecretUS / Operation Crime Files win with this packaging but appear to use invented cases — copy the packaging, never the fabrication.

## Performance rules
Weekly review (Mondays, Metricool YTVP02/17/06/08, last 28 days). Each rule is backed by ≥ 3 of our videos. Do not change schedules, AI-label settings or the owner's content rules here — only recommend.
1. Shorts = an action moment on real footage. Action Shorts: median 1,206 views (n=17: boardings, seizures, raids, tunnel reveals, undercover buys); history / definition / structure / quote Shorts: median 194 (n=10). Never make the second kind.
2. Lead the Short title with the number or the action verb ("267 Arrests…", "12,000 Pounds…", "Coast Guard Jumps…", "Undercover, They Bought 90 Guns", "1,300 Officers vs…") — all top-5 Shorts (1,271–1,433) open this way.
3. Never title a Short as a question or a definition ("What Does…", "Who Actually…", "How Deportations Spread…", "…Wasn't Born in…", "…Had a Board of Directors"): 5 videos, 76–358 views.
4. Put the day's strongest action+number Short in the 09:00 ET slot: all 5 Shorts that ran at 09:00 got 1,206–1,433 views (slot median 1,250 vs 425–756 for 11/15/17).
5. Long titles must not start with a place, gang name or program name: 5/5 such long videos ("MS-13: …", "Rancho San Pedro: …", "Narco-Subs: …", "Fentanyl at San Ysidro: …", "The Longest Smuggling Tunnel … : 36 Years…") got 3–12 views. Use the searched question / number + action / "How a Cartel…" formulas (§2 research).
6. Shorts retention: average view duration of all 27 Shorts is 6–20 s (winners 12–19 s). Keep Shorts 20–35 s with the number on screen and spoken in second 1; the payoff must land before ~15 s.
7. Same case, different angle: a seizure angle beats the person/sentence angle on the same footage ("77 Pounds of Fentanyl in One Car" 1,250 vs "A Teacher, 77 Pounds…, 87 Months" 84; "Coast Guard Jumps Onto a Moving Narco-Sub" 1,431 vs "Caught Twice on a Narco-Sub" 77; "The Longest Smuggling Tunnel…" 1,225 vs "The 'Store' Hiding a Drug Tunnel" 80). Lead with the seizure/action, never with the defendant.

Changelog
- 2026-11-09: section created from 32 videos (5 long, 27 Shorts) published 2026-10-29 → 2026-11-04 (Metricool returns nothing newer yet — reporting lag; episodes 006–010 and the template-tagged Shorts of 11-07/11-08 are not in the data). Recommendation for the owner (not applied): the 13:00 slot has only one data point (76 views, an explainer) — re-check next Monday.

## 6. QA (do not skip)
- Contact sheet of the long video every ~8 s: no gore, no unreadable overlaps, no black frames, subtitles inside frame.
- `ffmpeg -i long.mp4 -af ebur128 -f null -` → integrated ≈ −14 LUFS.
- Re-read script vs sources.md: every fact has a source.
- Thumbnail: view at 168×94 — the big word must still read; nothing in the bottom-right corner.

## 7. Upload to GitHub (public raw URLs for Metricool)
- Branch = weekday of the ET publish date: drop-mon … drop-sun. Orphan commit containing only that day's files, force-push:
```bash
cd /home/claude/coldwarrant-media && git checkout --orphan up && git rm -rqf . && cp $EP/long.mp4 $EP/thumb_A.jpg $EP/shorts/s*.mp4 . && \
git add long.mp4 thumb_A.jpg s*.mp4 && git -c user.name="COLD WARRANT bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -f origin up:drop-XXX && git checkout -q main && git branch -D up
```
- URL: `https://raw.githubusercontent.com/ituraev97/coldwarrant-media/drop-XXX/<file>`; check with `curl -sI` (200).

## 8. Schedule in Metricool
- createScheduledPost, blogId 7731358, providers [{"network":"youtube"}], publicationDate {dateTime, timezone:"America/New_York"}.
- Long: youtubeData {title, type:"video", privacy:"public", tags, category:"EDUCATION", madeForKids:false}; text = description; media [long.mp4 URL]; videoThumbnailUrl = thumb_A URL.
- Shorts: type "short", title = hook + " #shorts"-free short title, madeForKids false, category EDUCATION; text = 1–2 lines + "Full case file on the channel."
- Description template: 2–3 sentence summary · chapters (timestamps from timing.json chapter starts) · Sources (URLs) · Footage credit + "Appearance of U.S. government visual information does not imply or constitute endorsement." · CC photo credits.

## 9. Close the run
- Commit to `main`: episodes/NNN-slug/{episode.py,sources.md,thumb.json}, updated `backlog.md` (status `done YYYY-MM-DD`), `used_clips.json`. (Push main normally; never commit video files to main.)
- Message the owner (in Russian): episode title, publish times (ET and Tashkent), 1–2 line summary, that thumb_C is attached for YouTube Test & Compare, anything that needs his attention.

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
