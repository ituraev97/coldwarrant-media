# COLD WARRANT — daily production runbook

Run notes go to RUNBOOK_NOTES.md (append there, never here). Promote a note into a rule section only if it must apply to every future run.

The run fires daily but is a LONG run only every 2nd day (see "Long-video cadence" — do its OFF check FIRST, before reading further). A LONG run = publish the episode voiced since the previous long run + write and order the voice for the next one (see "Voice = Chatterbox via TTS relay"). An episode = one long video (English) + Short candidates (usually 5–6), of which the best 4 by the scorecard are uploaded here and scheduled in Metricool over two US days (see "Shorts: cadence + hook rules").
On a LONG run read this whole file before starting. Episode 001 (`episodes/001-ms13/`) is the reference for structure, pacing and style.

## Long-video cadence — owner decision 2026-11-23 (overrides every "one long per run/day" line)
**ONE long video every 2 days.** Dates below are America/New_York; D = tomorrow (ET) at run time.
1. **OFF check (first thing, every run):** Metricool getScheduledPosts, blogId 7731358, from today to D+1. If D already has its Shorts scheduled AND today or D has a long video → **OFF run**: do nothing else (no repo clone, no setup, no research, no voice status) and end with one line: `OFF run — D: <n> Shorts scheduled, last long <date>, next LONG run <date>.`
2. Otherwise → **LONG run**, long date = D (if D already has a long video, take the earliest date ≥ D without one and say so).
3. A LONG run does the "Voice = Chatterbox via TTS relay" run order: step 1 publishes the episode voiced since the previous long run (long at 12:00 ET on D), steps 2–3 write the next episode and order its voice — with a 2-day gap the voice is always ready by the next LONG run. Its "never leave tomorrow empty" rule (step 4) means: never leave the long date D without a long video.
4. Shorts: the LONG run schedules the Shorts for BOTH days — D 09:00 + 15:00 ET and D+1 09:00 + 15:00 ET (max 2/day per "Shorts: cadence + hook rules"). COLD WARRANT cuts its Shorts from the long, so pick the best 4 candidates by the scorecard (≥ 7/10): best → D 09:00, trailer for the long → D 15:00, 3rd/4th → D+1 09:00/15:00 (different templates and opening words on each day). Fewer than 4 score ≥ 7 → schedule only those and say so.
5. Dubs: only for long videos, i.e. every LONG run (unchanged rules, see "Dubbing").
6. OFF days have no other work (no long, no new Shorts); the Monday weekly review ("Performance rules") moves to the first LONG run on or after Monday.

## 0. Context
- Channel bible: Projects doc `claude/cold-warrant-bible.md` (rules, brand, schedule). Read it first.
- Metricool brand "COLD WARRANT": blogId **7731358**. Publish timezone **America/New_York**.
- Schedule per US day: Shorts 09:00 and 15:00 ET (max 2; owner 2026-11-23 — 11:00/13:00/17:00 dropped, the two best slots kept); long episode 12:00 ET. (21:00 slot dropped 2026-11-06 — weakest in stats.)
- Do NOT set isAiGeneratedContent (owner's decision; we use only real public-domain footage, a generic TTS narrator and code-generated music — no realistic AI imagery).

## Shorts: cadence + hook rules — owner decision 2026-11-23
Source: yt-pilot `analysis/HOOK_RULES.md` (30 days, 10 channels, 546 Shorts). Template clones posted 3–6×/day decay week over week — our Shorts median by upload week fell 633 → 722 → 588.5 → 107 at ~4.6 Shorts/day. Overrides older Shorts-count notes below.
- **1–2 YouTube Shorts per day, never more.** Cut the usual candidates (META["shorts"]), score each, schedule only the best 1–2 per day that score ≥ 7/10 (09:00 = strongest, 15:00 = second; a LONG run picks 4 for two days, see "Long-video cadence"). COLD WARRANT has no TikTok in Metricool, so the other candidates are not published (don't push them to the drop branch).
- Two Shorts on one day: ≥ 6 h apart (09:00 / 15:00) and different visual templates. On a long-video day one of the two is a trailer for it (see "Long-video cadence" for the 4 Shorts over 2 days) (15:00, after the 12:00 long; ends "Full case on the channel.").
- Scorecard (≥ 7/10 to publish): Hook 0–4 (hard number / famous name / paradox in the first second, on screen AND spoken) · Payoff 0–3 (the hook's promise paid in the last 2–3 s) · Freshness 0–2 (new story or angle, not yesterday's template) · Clarity 0–1 (works with sound off). Write the scores in the run report.
- Hook rules: second 0 = the most surprising sentence on action footage — no logo, title card or slow "In 2017…" start; on-screen hook ≤ 7 words, large, upper third. Title ≤ 60 chars: [number] + [stakes/action] or [famous name] + [unexpected fact]; "Why/How did…?" only with a number + action (question/definition titles lose here, see Performance rule 5).
- Banned openers/titles: quizzes ("Name this X in 3 seconds"), plain recaps without a number or a famous name, "Here's what happened…", "Did you know…", explainers ("What Does MS-13 Actually Mean?").
- Length 20–40 s, hard cap 50 s. End on the payoff and cut (outro ≤ 1 s; a loopable last line is a plus).
- Rotate ≥ 3 visual templates (footage-led action, document/number-led, map/timeline-led); never the same template two days running. If a Short's AVD in Metricool is < 5 s after 48 h, that hook style is dead — don't repeat it.
- Our evidence: winners = number + agency/operation or vivid sea action — "638 Gang Arrests in 179 Cities: Project Southbound" (1456), "267 Arrests, One Gang…" (1455), "Coast Guard Jumps Onto a Moving Narco-Sub" (1446). Losers = explainer titles with no number ("What Does 'MS-13' Actually Mean?" 147, "MS-13 Had a Board of Directors" 77) and money/penalty or "hidden in a truck" angles (Performance rules 2–3).
- Weekly (Mondays, with "Performance rules"): read the last 7 days of Shorts (views + AVD), list top 3 / bottom 3, add one line "what won" to the Changelog — repeat winners' hook pattern, drop losers'.

## Real footage via relay — owner decision 2026-11-23
The cloud cannot reach youtube.com. A relay on the owner's server downloads clips (YouTube or any yt-dlp URL) and hands them over through Google Drive folder "FOOTAGE RELAY". Client: `tools/footage_client.py` (stdlib only; see its docstring).
- Drive creds: Projects doc `claude/google-drive-oauth.md` → /tmp/drive_creds.json (never into git).
- Find candidate videos with the YouTube Data API (claude/yt_research.py / the same API key).
- Right after the script is drafted: `python3 tools/footage_client.py request <RUN> clips.json --creds /tmp/drive_creds.json`, keep working, then `python3 tools/footage_client.py wait <RUN> <dir> --creds /tmp/drive_creds.json --timeout 1800`. No answer in 30 min → continue with DVIDS/agency sources and say so in the report.
- clips.json = `[{"name","src":"<youtube id or URL>","start":"M:SS","end":"M:SS"}]`, ≤ 40 clips, ≤ 90 s each.
- Priority 1: official US government video — DOJ/DEA/FBI/ICE/ATF/HSI press conferences and raid footage, police-released bodycam, court-released video (public domain / public record). Priority 2: news reports about the exact case (short clips with our commentary, fair use).
- Never: movies, TV dramas, music videos, other YouTubers' faces/commentary, victims' faces, minors, gore.
- Real footage = 30–50% of runtime; ≤ ~12 s of one external clip at a time; mostly muted under narration, original audio only for short key quotes (≤ 15 s, speaker named).
- On-screen source label during each clip ("SOURCE: DOJ, 2024" / "SOURCE: <network>"); list all footage sources in the description.

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

## Voice = Chatterbox via TTS relay — owner decision 2026-11-23 (overrides the Kokoro VOICE/speed lines in "Narration rhythm" and §5 for the English narration; dubs stay on their own engine)
Why: the long videos are the weak spot (median 8.5 views while Shorts get ~500) and the Kokoro narrator is the most obvious "AI" tell. Chatterbox with the channel's own deep male voice (`cw`) runs on the owner's server, ~3–6 h per episode, so each run works on TWO episodes: it publishes the one voiced since the previous run, then writes the next one and orders its voice.
Tools: `tools/cw_voice.py` (wraps `tools/tts_client.py`; read both docstrings). Creds = the same `/tmp/drive_creds.json` as the footage relay.

**Run order (replaces the single-episode flow of §2–§9; LONG runs only — see "Long-video cadence"):**
1. **Publish the voiced episode first.** Find the `backlog.md` row with status `voicing NNN` (oldest first) and run `python3 tools/cw_voice.py status NNN --creds /tmp/drive_creds.json`.
   - `ready` → `python3 tools/cw_voice.py fetch NNN $EP` (writes $EP/vo/raw_NN.wav), get the relay footage again (`footage_client.py wait NNN $CL`, clips stay 7 days) and the DVIDS clips, then §5 build as usual — `tts_ep.py` skips every existing raw file (if it prints that it voiced lines, the text changed after the request: mixed voices — re-order or say so in the report). Then §6 QA, §7, §8 (target date = earliest ET date ≥ tomorrow without a long video), dubs, §9 → row `done YYYY-MM-DD`.
   - `pending` → the server is still working: go to step 2 and say so in the report.
   - `failed`, or `pending` for more than 30 h → build that episode now with Kokoro (old flow) so no day is missed; row `done (kokoro)`.
2. **Write the next episode** (§2 case + research, §3, §4 episode.py, independent fact check of every line). The LINES text is final after that — never edit a spoken line after ordering the voice.
3. **Order its voice:** `python3 tools/cw_voice.py request NNN $EP --creds /tmp/drive_creds.json --hint "<names, gangs, cities, agencies in this case, comma-separated>"`, order the footage (`footage_client.py request NNN clips.json`), commit episode.py + sources.md, set the row to `voicing NNN`, push. Do NOT build it in this run.
4. **Never leave tomorrow empty:** if step 1 published nothing and Metricool has no long video for tomorrow (ET), build the step-2 episode right away with Kokoro (skip step 3), row `done (kokoro)`.

**Writing for Chatterbox (replaces the Kokoro respelling rule in §4):**
- Spoken text uses REAL spellings ("Medellín", "Sinaloa", "Guzmán") — no phonetic respellings ("Meh-deh-yeen"): Chatterbox reads names well and the server checks every sentence with speech recognition against the text, so respellings fail the check. Put unusual names in `--hint`. Numbers and years still as words.
- Pace: per-line opts `speed` still work (relative to 1.04; the server turns them into tempo on top of 1.08). Keep the gap rules — they are applied by build_ep.py exactly as before.
- Delivery follows punctuation: a "!" raises the energy (use only on real reveals), "?" lifts the end, commas give short breaths. Short sentences sound most human.

## Fresh-case format (owner decision 2026-11-14 — overrides older case-picking notes)
- Source of topics = official newsrooms of the LAST 7 DAYS (14 max): justice.gov/news + USAO pages, fbi.gov/news, dea.gov, ice.gov/news, cbp.gov/newsroom, news.uscg.mil. backlog.md is a fallback only.
- "One case, one person": a protagonist (prefer sentenced/convicted; freshly charged only with "charged/alleged" + presumption-of-innocence line), told chronologically: who they were → the scheme → the detail that exposed it → takedown → court → what it means.
- Long video 15–20 min (2,800–3,400 words at the channel pace — see "Narration rhythm"; check total speech seconds after TTS).
- Why: Studio → Trends for our audience shows fresh DOJ/FBI cases with a person (California Reports "FBI ARRESTS 11 Over $17.4M" 147K in 10 min; "He Outran the Air Force With $1 Billion of Cocaine" 177K; "Killer Cop…" 55K). Our operation-statistics long videos got 1–23 views.
- Visuals: relay clips of the case (see "Real footage via relay") + agency press-release images/documents/press-conference video + DVIDS clips of the same agency or kind of operation. Anything not of this exact event gets an on-screen "FILE FOOTAGE" label and is never presented as the event. Faces only from U.S. government releases (federal agencies, police-released bodycam, court-released video) or relay news clips of the exact case; never social photos, minors or victims.
- Footage rule for fresh cases: ≥ 6 usable clips of the agency/operation type (not necessarily of the event itself).
- Title in Trends style: person/action + big number + twist, ≤ 70 chars, every word true and sourced. Thumbnail: federal-agency photo of the person or the seizure + 2–3 big words + red circle/arrow on the key detail.
- Shorts: never two Shorts in a day with the same opening word or pattern (identical "N Arrests in …" titles lost reach on 8–9 Nov). Text ends with "Full case on the channel."
- Research/analytics: YouTube Data API (claude/yt_research.py, --days 7) + Metricool + WebSearch. No vidIQ.

## Narration rhythm & anti-"AI voice" rules (owner 2026-11-14 — mandatory)
Measured on ep. 015: 46% of all pauses were the same ~0.45 s (every line got the default gap) and every line had the same speed — a metronome rhythm that viewers hear as "AI voice".
- Split long sentences into separate LINES at natural breath points (a reveal, a number, a colon) so the pause lands where a narrator would breathe.
- Vary the gap per line with opts `gap`: 0.25–0.35 inside one thought, 0.5–0.7 between sentences, 0.9–1.3 before a reveal, after a key number and before each chapter card. Never more than 3 consecutive lines with the same gap.
- VOICE: Chatterbox `cw` (owner 2026-11-23, see "Voice = Chatterbox via TTS relay"). Kokoro fallback only (owner 2026-11-14, sample D): Kokoro blend `bm_george:0.5+am_onyx:0.5` — default in tts_ep.py; never am_michael (shared with 3 other channels). Pace: tts_ep.py multiplies every line speed by TTS_SCALE=1.15 (owner: "faster"); the cold-open sample with real pauses ran 40 s, same as the old voice.
- Vary speed per line with opts `speed` (relative, × 1.15 in tts_ep.py): 1.06–1.10 for background/context, 0.96–1.00 for the reveal line and the line after a big number, 0.94 for the last line of the cold open. Default 1.04.
- Script style — cut the AI tells: no staccato triads as a habit ("Four boats. One helicopter. One rule." — at most once per episode, in the cold open), no slogan endings ("The boats keep coming. So does the helicopter."), no "This is the story of…", "Little did they know", "But here's the thing", "In a world where", "What happened next…". Vary sentence openers (not 20%+ starting with "The"). Prefer concrete verbs, quotes from court documents and agency statements, and plain connective speech ("So", "By then", "That's when") the way a human narrator talks.
- Listen-check before build: render the cold open + one chapter, check the pause histogram (no single gap value > 30% of pauses) and fix.

## Thumbnails v2 & click/retention rules (owner 2026-11-14: "aggressive, maximally bright")
- Generator: `node pipeline/thumb2.mjs <ep>/thumb2.json <ep>` → thumb_A/B/C.jpg (A = main, B and C for YouTube Test & Compare). The old thumb.mjs is retired.
- Recipe (see the reference spec in the header of thumb2.mjs): full-bleed real frame or federal-agency photo, colour pushed hard (the CSS filter does saturate 1.75 / contrast 1.28), subject big and sharp — pick the sharpest frame where the subject fills ≥ 25% of the crop; huge Anton text with a thick black stroke: line 1 = the number or the verb in yellow #FFD400 or red #FF2A2A, line 2 = white/yellow; ≤ 3–4 words total; red circle ONLY when it frames a clearly meaningful object that is fully visible and fills the circle (the drug boat, the bundle of drugs, the hidden compartment, the defendant's face). Owner 2026-11-14: circles placed on empty water, a vest or a random spot look stupid — when in doubt, NO circle. After rendering, zoom on the circle and confirm what is inside it before upload. Text goes to the side opposite the subject ("side":"right" when the subject is on the left). Logo small in a corner, bottom-right 220×90 always empty (duration badge).
- Three different angles per video: A = number + noun ("4 BOATS / 15 MINUTES"), B = action or verbatim quote ("SHOOT / THE ENGINES"), C = haul/money ("11,000 LB / OF COCAINE"). Add an inset (federal-agency mugshot or seizure photo, white frame, red label like SENTENCED / 20 YEARS) when the case has one. "NEW" tag only if the press release is ≤ 7 days old.
- Every word must be true and in the video; no gore, no weapon pointed at the camera, no fake "BREAKING" or invented images. LOOK at all three at full size and at 168×94 before upload.
- First 5 seconds of the long video = the thumbnail's promise: open on the same shot/number, no logo sting or title card before 0:30 (the g:title card comes after the cold open).
- Pinned question: send Metricool `firstCommentText` on the long video with one sharp question about the case ("Was 20 years enough?"); if Metricool rejects it for YouTube, schedule without it and say so.
- Description: first line = title promise + main keywords, then chapters, sources; end with 3 hashtags (#truecrime #fbi + one case keyword).

## Dubbing (other-language audio tracks) — owner 2026-11-15
- Rules, languages, voices: Projects doc `claude/dubbing.md`; voice engine `claude/dub_tts.py` → /home/claude/dub_tts.py. Languages: es, pt, hi, fr, it, de, ru (never Uzbek). The English channel voice never changes.
- Builder `pipeline/dub_build.py`: `bed <ep>` (timing.json from vo/raw_NN.wav + music/FX/nat without English voice), `voice <ep> <lang> [rate]` (Edge TTS per line, offline fallback), `mix <ep> <lang>` (fits every line into its English slot, ducks music, −14 LUFS, exact video length). Needs <ep>/vo/raw_NN.wav (tts_ep.py is deterministic if missing) and <ep>/dub/<lang>/script.txt (one line per English line, same order).
- Tempo (owner 2026-11-15): translations run longer, so dubs use Edge rate +10% (hi +8%) and atempo ≤ ×1.18 per line (≈1.3 max overall); a line may push ≤ 2.5 s into the next pause. Still too long → shorten the translation, never cut facts.
- Translation: own words, no new facts, numbers as words; English names in [[...]] for es/pt/fr/it/de; ru and hi use their own established forms (Вашингтон, «Лицо со шрамом», वॉशिंगटन). An independent agent checks every line (numbers, names, meaning) before voicing.
- Texts (script/title/description) go to episodes/NNN/dub/<lang>/ on main; audio never on main. The owner uploads tracks in YouTube Studio → Languages → Add dub (Metricool cannot).
- EVERY LONG RUN DUBS (owner 2026-11-17): dub the run's new long episode into all 7 languages right after it is scheduled and send the package the same run — dubs in the first 24 h get the most foreign reach. Workflow (ep. 017: 7 languages in ~1.5 h):
  1. `mkdir -p /home/claude/dub/NNN/tr`, copy episode.py there; vo/raw_NN.wav from the build. Back up timing.json, then `dub_build.py bed` AFTER finish_ep (it overwrites timing.json, nat.wav, fx.wav) — background job, see "Waiting for long jobs" (regex `bed parts done|Traceback`).
  2. Translate right after the fact check (before the build — saves ~1 h): export English lines to tr/en.txt; write tr/BRIEF.md + tr/CHECK.md (templates: episodes/017-ryan-wedding/dub/; rules above + names to bracket + any respellings restored to real spelling). One translation agent per language in parallel, then one independent CHECK agent per 1–2 languages that fixes in place.
  3. Voice ≤ 2–3 languages at once (Remy is shared by fr AND ru — never at the same time); regex ` voiced [0-9]+ lines|Traceback`. Mix ONE language at a time, never while finish_ep runs (OOM); regex `late>2\.5s:|Traceback`.
  4. The mix summary line must show `late>2.5s: []`. If not (usually hi): take the lines from dub/<lang>/fit_report.json where delay grows, shorten them without losing facts, delete their lines/NNN.*, re-voice only them faster (`voice <ep> hi 1.14`), re-mix.
  5. Per language title.txt + description.txt in episodes/NNN/dub/<lang>/ (≤ 70 chars, allegation framing kept, same chapter timestamps, sources, credits, "EXPEDIENTE/ДЕЛО NNN", 3 hashtags; reference episodes/017-ryan-wedding/dub/gen_meta.py).
  6. Localized thumbnails: `node pipeline/thumb_loc.mjs episodes/NNN/dub/thumb_loc.json <thumb_A.jpg> <outdir>` for the news layout (spec like episodes/017-ryan-wedding/dub/thumb_loc.json; "band" ≈ 20 px above the English text; "font":"Osw" for ru, "Teko" for hi); other layouts → `thumb2_loc.mjs` from thumb2.json A. LOOK at a grid of all 7.
  7. Every MP3: ≈ −14 LUFS and duration = video duration.
  8. Deliver SEVEN separate zips (NNN_<code>_<Language>.zip ≈ 24 MB: audio_<code>.mp3, title.txt, description.txt, thumb_<code>.jpg) via SendUserFile — never one big archive (a 166 MB zip arrived broken).
  Edge TTS unreachable or a language fails twice → deliver the done languages and name the missing ones.

## Waiting for long jobs (token rule, owner 2026-11-23)
Every job longer than ~2 min (graphics.mjs, build_ep.py, finish_ep.py, encode.sh, shorts.py, dub bed/voice/mix) runs detached with a log and a pid file, and is waited on ONLY with `tools/waitfor.sh` (one call waits up to 9 min, prints DONE / EXITED / WAITING + the last 3 log lines):
```bash
L=/home/claude/logs; W=/home/claude/coldwarrant-media/tools/waitfor.sh; mkdir -p $L     # set variables with ';' before launching, never in an && chain with &
setsid nohup python3 /home/claude/coldwarrant-media/pipeline/build_ep.py $EP $CL > $L/build.log 2>&1 < /dev/null & echo $! > $L/build.pid
bash $W $L/build.log "^done |Traceback" 540 $(cat $L/build.pid)   # repeat while it prints WAITING
```
Regexes (done line | Python crash; ffmpeg "error" lines can be non-fatal, so they are not matched — a fatal one ends the process → EXITED): build_ep `^done |Traceback` · finish_ep `audio \+ subs done|Traceback` · encode.sh `\.mp4$` (its final `ls -la`) · shorts.py `Traceback` + the pid · graphics.mjs `Error` + the pid · dub bed `bed parts done|Traceback` · dub voice ` voiced [0-9]+ lines|Traceback` · dub mix `late>2\.5s:|Traceback` (one log per language and step). EXITED = the process ended: check the expected output file exists before going on.
- Never cat/tail/grep a big log in a loop and never sleep-poll; print only summaries (counts, durations, the final status line). On a Traceback, or EXITED without the done line/output, read only `tail -n 20` of the log once.
- After a container restart (exit 137, uptime ≈ 0) background jobs are dead: check outputs and relaunch only what is missing.

## 2. Pick the case
- FIRST (owner rule 2026-11-06): search & competitor research — YouTube Data API (claude/yt_research.py) + Metricool + WebSearch, no vidIQ (see "Fresh-case format"); youtube.com transcripts are blocked from the cloud, so analyse hooks from titles/descriptions/thumbnails. Save `research/YYYY-MM-DD.md` (keywords, outliers, chosen case + why, 3 title candidates). The case, the long title (number + action + main keyword), description lines 1–2, tags and Shorts titles all come from this research. New cases with demand may be added to backlog.md if they pass the footage rule.
- Target date = the long date D from "Long-video cadence" (the OFF check there runs first).
- Case source = "Fresh-case format" (newsrooms of the last 7–14 days); `backlog.md` is the fallback (first `todo` row). Before committing to a case, check footage: DVIDS search API (`https://api.dvidshub.net/search?api_key=KEY&q=...&type[]=video`) must give at least 6 relevant public-domain videos (ICE/HSI, FBI, DEA, CBP, Coast Guard, DOJ). If not, mark the row `skip (footage)` and take the next.
- Never reuse a clip time range listed in `used_clips.json` (each clip id + start second used before). Different moments of the same clip are fine, but prefer new clips.

## 3. Research (facts decide everything)
- Primary sources first: justice.gov press releases, ice.gov, fbi.gov, court records; then AP/Reuters/NBC/LA Times/InSight Crime; Wikipedia only as a map to primary sources.
- Every number, date, name and quote in the script must come from a page you actually opened. Save them in `episodes/NNN-slug/sources.md` (claim → URL).
- Names: only people convicted, or officials. Charged-but-not-convicted → say "charged", "alleged", and add the presumption-of-innocence line.
- No fabricated scenes, no invented dialogue, no reenactments presented as real.

## 4. Script → `episodes/NNN-slug/episode.py`
- Copy the structure of `episodes/001-ms13/episode.py`: `LINES = [(spoken_text, shots, opts), ...]`, `DISPLAY` (spoken → on-screen spelling), `META` (case, label, title, imgs, credit, shorts).
- Length: see "Fresh-case format" (15–20 min). Episode must stay ≥ 15:00 unless the case is thin (then ≥ 10:00 and say so in the report). Cold open (≤40 s, the most dramatic verified moment + the question) → `g:title` → 5–6 chapters (`g:chapter` with n, t, case) → close + `g:end`.
- Write numbers/years as words in spoken text (Kokoro), add digit forms to DISPLAY. Respell hard names for TTS and map them back in DISPLAY (check with `Kokoro(...).tokenizer.phonemize(word,"en-us")`).
- Shots: 2–3 per line, each 2.5–6 s. ~25–35% of screen time should be our own graphics (maps, stats, documents, timelines, lists) — this is what makes the channel original.
- Graphics available in `pipeline/graphics.mjs`: title{case,title,sub}, chapter{case,n,t}, stat{a,b,c}, quote{q,w}, doc{header,title,body,stamp,source}, list{kicker,title,items,footer}, phases{kicker,title,left,right,active,total,footer}, cards3{kicker,title,cards}, timeline{kicker,title,events}, map{map:{bounds|useUS,highlight,cities,arcs,labels,topPad},kicker,title,footer}, end{case,label}.
- Content rules: no blood, wounds, bodies or execution footage (if any frame shows them, cut it). Never use DVIDS videos titled "Lethal Kinetic Strike" or any footage of people being killed or injured. Gangs are never glamorized; always consequences, victims, courts. No gang music or recruitment videos.

## 5. Build
```bash
EP=/home/claude/coldwarrant-media/episodes/NNN-slug; CL=/home/claude/clips; P=/home/claude/coldwarrant-media/pipeline; L=/home/claude/logs; W=/home/claude/coldwarrant-media/tools/waitfor.sh; mkdir -p $L
# download clips: GET https://api.dvidshub.net/asset?api_key=KEY&id=video:ID -> files[] (720p) -> $CL/ID.mp4
# relay clips: tools/footage_client.py wait <RUN> $CL ... (requested earlier, see "Real footage via relay") -> $CL/<name>.mp4, used alongside DVIDS/agency images
python3 tools/cw_voice.py fetch NNN $EP --creds /tmp/drive_creds.json   # Chatterbox voice ordered in the previous run (see voice section)
python3 $P/tts_ep.py $EP   # only fills missing lines (Kokoro fallback: bm_george:0.5+am_onyx:0.5, scale 1.15)
python3 $P/make_gspec.py $EP
# every step below that takes minutes: setsid nohup ... > $L/<step>.log 2>&1 < /dev/null & echo $! > $L/<step>.pid,
# then wait ONLY with: bash $W $L/<step>.log "<regex>" 540 $(cat $L/<step>.pid)  (see "Waiting for long jobs")
cd $P && node graphics.mjs $EP/gspec.json $EP/gfx     # ~5 min; absolute paths; background + waitfor
python3 $P/build_ep.py $EP $CL          # ~40–60 min on 2 cores — background + waitfor "^done |Traceback"
python3 $P/finish_ep.py $EP $CL         # background + waitfor "audio \+ subs done|Traceback"
bash $P/encode.sh $EP $EP/long.mp4 450  # ≤ 450 MB for Drive hosting (Metricool YouTube limit 500 MB), see §7; background + waitfor "\.mp4$"
python3 $P/shorts.py $EP $EP/shorts     # background + waitfor "Traceback" + pid; never while video_raw.mp4 is being rewritten
cd $P && node thumb2.mjs $EP/thumb2.json $EP   # thumb_A (main) + thumb_B + thumb_C (Test & Compare) — see "Thumbnails v2"
```

## Motion & pacing rules (owner feedback after ep. 001 — mandatory)
- No artificial zoom/drift/shake on video footage. Use the camera's own motion only. (Per-frame scale/crop rounds to whole pixels and makes the picture twitch.)
- Graphics: animate in, then hold perfectly still until the cut. Never start a zoom or pan after the intro animation ends.
- Ken Burns only on still photos, and only via zoompan on a 4×-supersampled canvas (already in build_ep.py).
- Narration pace: see "Narration rhythm" (blend voice, per-line speed × 1.15). Do not slow it down.
- Before upload, scrub the transitions from intro→hold on 3 graphics and 3 footage cuts at full size: anything that jumps or wobbles is a blocker.

## Shorts selection rule (owner, 2026-11-06 — based on channel stats)
- Every Short = an ACTION moment on real footage (boarding, interdiction, raid, tunnel/seizure reveal, pursuit) + a concrete NUMBER in title and hook (arrests, tons, pounds, officers, years, dollars).
- Winners so far (~1,100–1,400 views each): "267 Arrests, One Gang", "Coast Guard Jumps Onto a Moving Narco-Sub", "12,000 Pounds of Cocaine in One Semi-Sub", "32 Tons of Marijuana Under the Border".
- Losers (11–135 views): explainers about names, history or structure — "What Does MS-13 Actually Mean?", "MS-13 Had a Board of Directors", "62 Killed in One Day — How El Salvador Responded". Don't make these.
- Title = number + action, ≤ 70 chars. Choose META["shorts"] line ranges whose footage shows that action.
- LENGTH (owner, 2026-11-06, vidIQ niche data; 20–40 s per owner 2026-11-23): YouTube Shorts = 20–40 s (2–4 lines), hard cap 50 s. Start on the action shot, number spoken and on screen in the first second; no graphics-only lines inside a Short. Niche breakouts are 9–31 s pure action (Coast Guard boarding 0:09–0:31 → 165K–2.4M views); our 40–50 s Shorts held viewers only 6–20 s.
- TikTok (only if the brand has TikTok connected in Metricool — COLD WARRANT has none as of 2026-11-06): separate cuts of 61–90 s (TikTok rewards videos over 1 minute). Do NOT trim those to YouTube length.

## Long-video packaging (vidIQ niche data, 2026-11-06)
- Our long videos got 3–12 views each; Shorts brought 17.5K views but only 3 views came from "related video". Long titles must use the same number + action formula as winning Shorts, front-loaded: e.g. "976 Gang Arrests in Six Weeks: Project Wildfire", "DEA … — 41 Arrested & 11 Tons Seized" (niche breakouts 12K–36K views on 1K-sub channels), or a person-hook: "The Customs Officer Who Weighed One Pallet — and Stopped $210M in Cocaine" (only if true and sourced).
- Search demand worth targeting with real, sourced cases: "how every cartel boss died / was caught" (~26K searches/mo, competition 48), "sinaloa cartel history" (~4K, competition 27), "chapo guzman" (+155%), "mafia vs cartel" (low competition).
- Competitor channels like FBISecretUS / Operation Crime Files win with this packaging but appear to use invented cases — copy the packaging, never the fabrication.

## Performance rules
Weekly review (Mondays, Metricool YTVP02/17/06/08, last 28 days). Each rule is backed by ≥ 3 of our videos. Do not change schedules, AI-label settings, the voice or the owner's content rules here — only recommend.
1. Shorts = an action moment on real footage. Action/seizure Shorts median ~1,000 views (Oct 29–Nov 14); history / definition / structure / "who/why" Shorts median ~200 (n=12: "What Does MS-13…" 147, "MS-13 Had a Board…" 77, "Who Actually Smuggles Fentanyl?" 394, "Why Southern California Gangs Use the Number 13" 287…). Never make the second kind.
2. At-sea cocaine action is our best Short material: Coast Guard / boat / semi-sub / cargo-ship / cocaine Shorts median 743 (n=34); land concealment "N Pounds Hidden in a Truck/Trailer" median 209 (n=5); gun-trafficking Shorts (11-19) 27–112 (n=5). For land cases, lead with the arrest/raid moment or the vivid concealment ("Meth Hidden in Cabbages" 998).
3. Court / sentence / "Feds say" angles lose on Shorts: since the fresh-case switch (11-15…11-19) Shorts median fell to 177 (n=25) from 841 (n=41, 11-06…11-14). "— Then N Years in Prison" titles: 30, 42, 89 (n=3); "Feds Say/Allege/Prosecutors Say" titles median 312 (n=9). The fresh-case winners had a famous name + a shock fact ("El Mencho Said He Killed Him…" 1,037; "Armed at Cartel Cash Pickups: El Mencho's Brother…" 585) or a vivid seizure. Pick the 1–2 Shorts of a fresh case from its action/seizure footage or its famous-name twist, never the sentence or the indictment wording.
4. Money / laundering / penalty Shorts lose: median 214 (n=4, 11-08: $3B penalty 138, $50M cash 315, $474M bank 301, 81 vehicles 103) vs 980 for the seizure Short of the same day. Keep the money angle for the long video.
5. 09:00 ET is the strongest slot: since 11-06 median 841 (n=13) vs 15:00 479 (n=13), 11:00 363, 17:00 312, 13:00 225. Put the day's best scorecard Short at 09:00 (matches the 2026-11-23 cadence: 09:00 + 15:00 only).
6. Lead the Short title with the number or the action verb (top-5 Shorts 1,329–1,456 all do: "638 Gang Arrests…", "267 Arrests, One Gang…", "Coast Guard Jumps Onto a Moving Narco-Sub", "The Drug Boat Built for One Trip", "976 Gang Arrests…"). Never a question or definition title (5 videos, 77–394 views).
7. Retention keeps falling: Shorts median AVD 13 s (top-5), 7 s overall (n=100), 5 s in the fresh-case era (n=25). Number + action on screen in second 1, payoff by ~8 s, 20–40 s total, cut right after the payoff.
8. Long videos are flat whatever the format: 20 long videos, median 8.5 views; the five fresh one-case/one-person longs (11-15…11-19) got 1–10 views (AVD 1–123 s; best "El Mencho's Brother 'Tony Montana'…" 10 views / 123 s AVD, a famous name). Metricool has no data yet for the evergreen Saturday (11-20) or for 11-21/22 — compare next Monday. Recommendation for the owner: long videos get almost no impressions — one long video every 2 days (APPLIED 2026-11-23, see "Long-video cadence"); still open: pinning each day's 09:00 Short to its long video (related-video link) to feed it traffic.

Changelog
- 2026-11-09: section created from 32 videos (5 long, 27 Shorts) published 2026-10-29 → 2026-11-04.
- 2026-11-16: rewritten from 80 videos (13 long, 67 Shorts) published 2026-10-29 → 2026-11-11 (Metricool returns nothing newer — reporting lag; episodes 012–016 are not in the data). New: rules 2 (sea > truck), 3 (money Shorts lose), 6 (AVD drop 11 s → 5 s), 7 (long videos flat). Recommendation (not applied): review the 13:00 slot.
- 2026-11-23: rewritten from 120 videos (20 long, 100 Shorts) published 2026-10-29 → 2026-11-19 (data stops at 11-19). New: rule 3 (court/sentence/"Feds say" Shorts lose — fresh-case-era Shorts median 177 vs 841), gun-trafficking Shorts weak (rule 2), slot medians since 11-06 (rule 5). What won this week (Shorts, 11-13…11-19): top 3 = "El Mencho Said He Killed Him…" 1,037, "3 Drug Boats at Once…" 1,055 (11-14), "Meth Hidden in Cabbages…" 998 — famous name + shock fact or vivid sea/concealment action; bottom 3 = "Caught Heading Into Mexico With 8 Handguns…" 27, "Two Apartments, 26 Kilos… Then 30 Years" 30, "13 Agencies, 12 Search Warrants…" 39 — sentence/procedure angles. Repeat the winners' pattern.

## 6. QA (do not skip)
- Contact sheet of the long video every ~8 s: no gore, no unreadable overlaps, no black frames, subtitles inside frame.
- `ffmpeg -i long.mp4 -af ebur128 -f null -` → integrated ≈ −14 LUFS.
- Re-read script vs sources.md: every fact has a source.
- Thumbnail: view at 168×94 — the big word must still read; nothing in the bottom-right corner.

## 7. Upload to GitHub (public raw URLs for Metricool)
- Branch = weekday of the ET long date D: drop-mon … drop-sun. Orphan commit containing only this run's files (thumb + the 4 selected Shorts for D and D+1; sX/sY… = their ids), force-push:
```bash
cd /home/claude/coldwarrant-media && git checkout --orphan up && git rm -rqf . && cp $EP/thumb_A.jpg $EP/shorts/sX.mp4 $EP/shorts/sY.mp4 $EP/shorts/sZ.mp4 $EP/shorts/sW.mp4 . && \
git add thumb_A.jpg s*.mp4 && git -c user.name="COLD WARRANT bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -f origin up:drop-XXX && git checkout -q main && git branch -D up
```
- URL: `https://raw.githubusercontent.com/ituraev97/coldwarrant-media/drop-XXX/<file>`; check with `curl -sI` (200).
- LONG VIDEO (owner 2026-11-23): not on GitHub — host on Google Drive folder "COLD WARRANT": `python3 tools/drive_upload.py $EP/long.mp4 --folder "COLD WARRANT" --creds /tmp/drive_creds.json` → its `direct` URL is the Metricool media for the long video. (Only in the ≤ 95 MB fallback add long.mp4 to the orphan commit.) Shorts and thumbnails stay on GitHub.
- If Metricool rejects the long video as too big: re-encode to ≤ 300 MB (`encode.sh ... 300`) and re-upload to Drive; if still rejected, ≤ 95 MB on GitHub as before.

## 8. Schedule in Metricool
- createScheduledPost, blogId 7731358, providers [{"network":"youtube"}], publicationDate {dateTime, timezone:"America/New_York"}.
- Long: youtubeData {title, type:"video", privacy:"public", tags, category:"EDUCATION", madeForKids:false}; text = description; media [long.mp4 Drive `direct` URL]; videoThumbnailUrl = thumb_A URL.
- After scheduling: `python3 tools/drive_upload.py --folder "COLD WARRANT" --creds /tmp/drive_creds.json --cleanup-days 7` (deletes Drive files older than 7 days in that folder).
- Shorts (the 4 selected per "Long-video cadence": D 09:00 + 15:00 and D+1 09:00 + 15:00 ET): type "short", title = hook + " #shorts"-free short title, madeForKids false, category EDUCATION; text = 1–2 lines + "Full case file on the channel."
- Description template: 2–3 sentence summary · chapters (timestamps from timing.json chapter starts) · Sources (URLs) · Footage credit (every relay clip source: agency / network + URL) + "Appearance of U.S. government visual information does not imply or constitute endorsement." · CC photo credits.

## 9. Close the run
- Commit to `main`: episodes/NNN-slug/{episode.py,sources.md,thumb.json}, updated `backlog.md` (status `done YYYY-MM-DD`), `used_clips.json`. (Push main normally; never commit video files to main.)
- Message the owner (in Russian): episode title, publish times (ET and Tashkent), 1–2 line summary, that thumb_C is attached for YouTube Test & Compare, anything that needs his attention.

## Lessons from past runs (distilled 2026-11-23)
Still-active rules from runs 004–023; the full diaries (incl. per-clip trap lists) are in RUNBOOK_NOTES.md.
- Before using a DVIDS clip id, `grep <id> RUNBOOK_NOTES.md` for its known black/slate/caption/interview/face/pillarbox ranges.
- Commit and push main (backlog, used_clips, episode files) BEFORE the §7 orphan step — `git rm -rqf .` deletes uncommitted edits. On a detached HEAD: `git push origin HEAD:main`, then `git checkout -B main <sha>`.
- Run ONE build_ep.py, ONE encode.sh at a time; never finish_ep and a dub mix together (OOM); never shorts.py or the encode while video_raw.mp4 is being rewritten.
- Kill jobs only by the PID from their pid file; never `pkill -f`/`pgrep -f`/`ps | grep pattern | xargs kill` from a shell whose command line contains the pattern.
- Write the narration from the sources, then pick footage; footage tags must describe what is actually on screen (DVIDS descriptions are not proof).
- Never put arrest/raid faces, vehicles or actor training videos (e.g. ATF straw-purchase) under lines about a named person or a specific vehicle of the case — tag "ILLUSTRATIVE · NOT THE DEFENDANTS IN THIS CASE" or use graphics. ICE detention centers are tagged "(NOT A PRISON)".
- Use `lab=1` (FILE FOOTAGE badge) on all footage not of the case, `"lab": 0` for the case's own clips; `mute_nat=[ids]` for clips with possible gunfire and for relay speech clips under narration.
- Vertical clips → `vert=1`; 4:3 pillarboxed → `pb=1`; framed/branded streams → `crop=` (e.g. `iw*0.8:ih*0.8:iw*0.1:0` removes channel bugs).
- Read contact-sheet timestamps as h:mm:ss and check every pick against the clip duration.
- After TTS, validate every shot with a script (alloc.py pattern, episodes/017–023): start + length < clip end − 0.4, ≤ 6.2 s per shot, no overlap with other shots of the same clip, not in used_clips.json, outside blackdetect/slate ranges. Download EVERY clip a pool can fall back to.
- Run blackdetect (`scale=320:-2,blackdetect=d=0.05:pix_th=0.06`) on each source and on video_raw.mp4; ~4 dark frames at each graphic start are expected.
- After the build: per-shot midpoint sheet (`L<line> <clip>@<start>`) + interior-cut sheet (0.25 s around each scene cut inside a segment) + scene-cut flash check (`select='gt(scene,0.35)'`; a cut 0.08–0.7 s from a segment edge = flash → shift `ss`).
- Fix single shots without a full rebuild: re-render seg/NNN.mp4 with the same frame count (fixseg.py / build_resume.py pattern), re-concat seg/list.txt, patch timing.json, re-run finish_ep.
- Any graphic text edit changes its gfx key: re-run make_gspec.py and render only the missing keys (filtered gspec) BEFORE build_ep.py.
- Graphics limits: list ≤ 5 single-line items; element delays `d` ≤ 2.0 s; timeline `t` ≤ 22 chars, `y` single-line; map arcs use `from`/`to`; prefix a bare year in stat with a zero-width space; `big=` ≤ 16 chars (sub ≤ ~34); check the LAST frame of every map/list for overlaps.
- Shorts are footage-only: turn a stat/quote card inside a Short's line range into footage + `big=`/`tag` before building; Short ranges are contiguous — check every Short is ≥ 20 s after the build.
- After any scripted edit of LINES, assert `len(LINES)` and that every entry is a 3-tuple; edit long graphic lines by exact anchors.
- tts_ep.py skips wavs by index: after moving/editing lines, remap old wavs by text and delete only the changed ones.
- Stills: measure mean luma of a rendered still (aim ≥ 70, gamma-lift dark DOJ photos ≈ 1.6); fit white posters on a dark blurred bed; bake hook numbers into the opening still and keep baked text above y ≈ 900. Thumbnail drug images next to a defendant carry "FILE IMAGE · NOT HIS CASE".
- No case video (fresh sentencing/capture): compose stills from DOJ/indictment photos (`pdfimages -list` → colour pages) + labeled file footage + graphics.
- Blocked from the cloud — do not try to bypass: fbi.gov, cbp.gov, dea.gov, ofac (use DOJ/USAO copies, agency-written DVIDS descriptions, verbatim reprints, news quoting the release; note it in sources.md); justice.gov text via WebFetch, its images via curl; huggingface (no transcription — never quote clips you cannot transcribe).
- Fact check (independent agent, every line): who exactly said it (inside news stories too), when it was said/announced (e.g. reward dates), verbatim quotes only (never a paraphrase in quote marks), scope (ring-wide vs one defendant, partners vs one agency), attribution type (indictment vs release vs news), guilt-implying wording and Short titles that overgeneralize.
- When a backlog row is skipped, the next episode still gets the next CASE FILE number.
- If time is short: push Shorts + thumbs to the drop branch and schedule them while the long video encodes; single-pass H.264 (`libx264 -preset veryfast -b:v 3000k -maxrate 4500k`, AAC 160k ≈ 390 MB for 17 min) fits the Drive route.
