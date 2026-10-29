# COLD WARRANT — daily production runbook

One run = one long episode (10–14 min, English) + 5 vertical Shorts, uploaded here and scheduled in Metricool for one US day.
Read this whole file before starting. Episode 001 (`episodes/001-ms13/`) is the reference for structure, pacing and style.

## 0. Context
- Channel bible: Projects doc `claude/cold-warrant-bible.md` (rules, brand, schedule). Read it first.
- Metricool brand "COLD WARRANT": blogId **7731358**. Publish timezone **America/New_York**.
- Schedule per US day: Shorts 09:00, 11:00, 15:00, 17:00, 21:00 ET; long episode 12:00 ET.
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
- 1,300–1,600 words → 10–12.5 min. Cold open (≤40 s, the most dramatic verified moment + the question) → `g:title` → 5–6 chapters (`g:chapter` with n, t, case) → close + `g:end`.
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
