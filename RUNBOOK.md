# COLD WARRANT — daily production runbook

One run = one long episode (10–14 min, English) + Short candidates (usually 5), of which only the best 1–2 by the scorecard are uploaded here and scheduled in Metricool for one US day (see "Shorts: cadence + hook rules").
Read this whole file before starting. Episode 001 (`episodes/001-ms13/`) is the reference for structure, pacing and style.

## 0. Context
- Channel bible: Projects doc `claude/cold-warrant-bible.md` (rules, brand, schedule). Read it first.
- Metricool brand "COLD WARRANT": blogId **7731358**. Publish timezone **America/New_York**.
- Schedule per US day: Shorts 09:00 and 15:00 ET (max 2; owner 2026-11-23 — 11:00/13:00/17:00 dropped, the two best slots kept); long episode 12:00 ET. (21:00 slot dropped 2026-11-06 — weakest in stats.)
- Do NOT set isAiGeneratedContent (owner's decision; we use only real public-domain footage, a generic TTS narrator and code-generated music — no realistic AI imagery).

## Shorts: cadence + hook rules — owner decision 2026-11-23
Source: yt-pilot `analysis/HOOK_RULES.md` (30 days, 10 channels, 546 Shorts). Template clones posted 3–6×/day decay week over week — our Shorts median by upload week fell 633 → 722 → 588.5 → 107 at ~4.6 Shorts/day. Overrides older Shorts-count notes below.
- **1–2 YouTube Shorts per day, never more.** Cut the usual candidates (META["shorts"]), score each, schedule only the best 1–2 that score ≥ 7/10 (09:00 = strongest, 15:00 = second). COLD WARRANT has no TikTok in Metricool, so the other candidates are not published (don't push them to the drop branch).
- Two Shorts on one day: ≥ 6 h apart (09:00 / 15:00) and different visual templates. Every run has a long video, so one of the two is a trailer for it (15:00, after the 12:00 long; ends "Full case on the channel.").
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
- VOICE (owner 2026-11-14, chose sample D): Kokoro blend `bm_george:0.5+am_onyx:0.5` — default in tts_ep.py; never am_michael (shared with 3 other channels). Pace: tts_ep.py multiplies every line speed by TTS_SCALE=1.15 (owner: "faster"); the cold-open sample with real pauses ran 40 s, same as the old voice.
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
- Rules, languages and voices: Projects doc `claude/dubbing.md`; voice engine `claude/dub_tts.py` → /home/claude/dub_tts.py. Languages: es, pt, hi, fr, it, de, ru (never Uzbek). The English channel voice never changes.
- Builder: `pipeline/dub_build.py` — `bed <ep>` (timing.json from vo/raw_NN.wav + music/FX/nat sound without English voice), `voice <ep> <lang>` (Edge TTS per line, offline fallback), `mix <ep> <lang>` (fits every line into its English slot, ducks music, −14 LUFS, exact video length). Needs <ep>/vo/raw_NN.wav (run pipeline/tts_ep.py if missing — deterministic) and <ep>/dub/<lang>/script.txt (one line per English line, same order).
- TEMPO (owner 2026-11-15 "change the tempo if needed"): our English runs at ×1.15, translations are longer, so dubs use Edge rate +10% (hi +8%) and atempo up to ×1.18 per line (≈1.3 max overall); a line may push ≤ 2.5 s into the next pause. If a line still does not fit, shorten the translation, never cut facts.
- Translation rules: own words, no new facts, numbers as words; English names in [[...]] for es/pt/fr/it/de; Russian and Hindi use their own established forms of names and places (Вашингтон, «Лицо со шрамом», वॉशिंगटन). Independent agent checks every line (numbers, names, meaning) before voicing.
- Texts (script/title/description) go to episodes/NNN/dub/<lang>/ on main; audio never on main. The owner uploads tracks in YouTube Studio → Languages → Add dub (Metricool cannot).
- DAILY DUB (owner 2026-11-17: "в запланированных настрой, чтобы сразу отправлял мне дубляж"): every daily run dubs its new long episode into all 7 languages right after the episode is scheduled, and sends the package to the owner the same run — dubs uploaded in the first 24 h get the most foreign-language reach. Proven workflow (episode 017, 7 languages in ~1.5 h):
  1. `mkdir -p /home/claude/dub/NNN/tr` and copy episode.py there; vo/raw_NN.wav from the episode build (or re-run tts_ep.py); `dub_build.py bed` in the background.
  2. Export English lines to tr/en.txt; write tr/BRIEF.md and tr/CHECK.md (templates: episodes/017-ryan-wedding/dub/BRIEF.md, CHECK.md — rules above + the episode's phonetic respellings restored to real spelling, e.g. "Meh-deh-yeen" → Medellín, + the list of names to bracket). One translation agent per language in parallel (background), then one independent CHECK agent per 1–2 languages that compares every line and fixes in place (153 lines checked in ~1 min each).
  3. Voice: at most 2–3 languages at once (Remy is shared by fr AND ru — never voice them at the same time). Mix ONE language at a time (memory).
  4. After each mix read the log line: `late>2.5s` must be empty. If not (Hindi usually is), list lines from dub/<lang>/fit_report.json where delay grows, shorten those translations without losing facts, delete their lines/NNN.* and re-voice only them with a higher rate (`voice <ep> hi 1.14`), then re-mix.
  5. Titles/descriptions per language (≤ 70 chars, allegation framing kept, chapters with the same timestamps, sources list, credits, "EXPEDIENTE/ДЕЛО NNN", 3 hashtags) → episodes/NNN/dub/<lang>/title.txt, description.txt (reference script: episodes/017-ryan-wedding/dub/gen_meta.py).
  6. Localized thumbnails: `node pipeline/thumb_loc.mjs episodes/NNN/dub/thumb_loc.json <thumb_A.jpg> <outdir>` (spec like episodes/017-ryan-wedding/dub/thumb_loc.json; set "band" ≈ 20 px above the top of the English text so no ghost letters show; "font":"Osw" for ru, "Teko" for hi). LOOK at a grid of all 7.
  7. Loudness check (≈ −14 LUFS) and duration = video duration for every MP3.
  8. Deliver as SEVEN separate zips (NNN_<code>_<Language>.zip, ~24 MB each: audio_<code>.mp3, title.txt, description.txt, thumb_<code>.jpg) via SendUserFile — one 166 MB zip arrived broken on the owner's Mac (error 94), never send one big archive.
  If Edge TTS is unreachable or a language fails twice, deliver the languages that are done and name the missing ones.

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
- Length: see "Fresh-case format" (15–20 min). Episode must stay ≥ 15:00 unless the case is thin (then ≥ 10:00 and say so in the report). Cold open (≤40 s, the most dramatic verified moment + the question) → `g:title` → 5–6 chapters (`g:chapter` with n, t, case) → close + `g:end`.
- Write numbers/years as words in spoken text (Kokoro), add digit forms to DISPLAY. Respell hard names for TTS and map them back in DISPLAY (check with `Kokoro(...).tokenizer.phonemize(word,"en-us")`).
- Shots: 2–3 per line, each 2.5–6 s. ~25–35% of screen time should be our own graphics (maps, stats, documents, timelines, lists) — this is what makes the channel original.
- Graphics available in `pipeline/graphics.mjs`: title{case,title,sub}, chapter{case,n,t}, stat{a,b,c}, quote{q,w}, doc{header,title,body,stamp,source}, list{kicker,title,items,footer}, phases{kicker,title,left,right,active,total,footer}, cards3{kicker,title,cards}, timeline{kicker,title,events}, map{map:{bounds|useUS,highlight,cities,arcs,labels,topPad},kicker,title,footer}, end{case,label}.
- Content rules: no blood, wounds, bodies or execution footage (if any frame shows them, cut it). Never use DVIDS videos titled "Lethal Kinetic Strike" or any footage of people being killed or injured. Gangs are never glamorized; always consequences, victims, courts. No gang music or recruitment videos.

## 5. Build
```bash
EP=/home/claude/coldwarrant-media/episodes/NNN-slug; CL=/home/claude/clips; P=/home/claude/coldwarrant-media/pipeline
# download clips: GET https://api.dvidshub.net/asset?api_key=KEY&id=video:ID -> files[] (720p) -> $CL/ID.mp4
# relay clips: tools/footage_client.py wait <RUN> $CL ... (requested earlier, see "Real footage via relay") -> $CL/<name>.mp4, used alongside DVIDS/agency images
python3 $P/tts_ep.py $EP   # voice bm_george:0.5+am_onyx:0.5, scale 1.15 (defaults)
python3 $P/make_gspec.py $EP
cd $P && node graphics.mjs $EP/gspec.json $EP/gfx
python3 $P/build_ep.py $EP $CL          # ~40–60 min on 2 cores — run in background
python3 $P/finish_ep.py $EP $CL
bash $P/encode.sh $EP $EP/long.mp4 450  # ≤ 450 MB for Drive hosting (Metricool YouTube limit 500 MB), see §7
python3 $P/shorts.py $EP $EP/shorts
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
1. Shorts = an action moment on real footage. Action/seizure Shorts: median ~1,000 views; history / definition / structure / "who/why" Shorts: median ~200 (n=12: "What Does MS-13…" 142, "MS-13 Had a Board…" 77, "Who Actually Smuggles Fentanyl?" 394, "Why Southern California Gangs Use the Number 13" 276…). Never make the second kind.
2. At-sea cocaine action beats land concealment: Coast Guard / boat / cargo-ship Shorts median 977 (n=15, 77–1,439); "N Pounds Hidden in a Truck/Trailer" Shorts median 178 (n=5, 11-11: 89–624). For land cases, lead the Short with the arrest/raid moment, not "hidden in a load of …".
3. Money / laundering / penalty Shorts lose: median 214 (n=4, 11-08: $3B penalty 138, $50M cash 313, $474M bank 290, 81 vehicles 104) vs 977 for the seizure Short of the same day. Pair finance cases with a seizure or arrest action Short and keep the money angle for the long video.
4. Put the day's strongest action+number Short at 09:00 ET: 09:00 median 1,232 (n=13) vs 15:00 759 (n=13), 17:00 549 (n=13), 11:00 430 (n=14), 13:00 198 (n=7). Recommendation for the owner (not applied): 13:00 is the weakest slot on 7 data points — consider moving it to 08:00 or 19:00 and re-check. (Superseded 2026-11-23: only 09:00 + 15:00 are used.)
5. Lead the Short title with the number or the action verb (top-5 Shorts 1,327–1,454 all do: "638 Gang Arrests…", "267 Arrests, One Gang…", "Coast Guard Jumps Onto a Moving Narco-Sub", "976 Gang Arrests…"). Never a question or definition title (5 videos, 76–394 views).
6. Retention is falling: Shorts average view duration was 11 s (median, n=47, Oct 29–Nov 7) and 5 s (n=20, Nov 8–11). The number and the action must be on screen in second 1 and the payoff must land by ~8 s; keep Shorts 20–40 s.
7. Long videos: all 13 long videos in the window got 1–27 views regardless of title formula (place/gang/program-first titles 3–27; number-first titles 1–21). The fresh one-case/one-person format (from ep. 015, 11-13) has no Metricool data yet — judge it next Monday; meanwhile never start a long title with a place, gang or program name.
8. Same case, different angle: the seizure/action angle beats the person/sentence angle on the same footage ("77 Pounds of Fentanyl in One Car" 1,257 vs "A Teacher, 77 Pounds…, 87 Months" 104; "Coast Guard Jumps Onto a Moving Narco-Sub" 1,439 vs "Caught Twice on a Narco-Sub" 77; "The Longest Smuggling Tunnel…" 1,232 vs "The 'Store' Hiding a Drug Tunnel" 81).

Changelog
- 2026-11-09: section created from 32 videos (5 long, 27 Shorts) published 2026-10-29 → 2026-11-04.
- 2026-11-16: rewritten from 80 videos (13 long, 67 Shorts) published 2026-10-29 → 2026-11-11 (Metricool returns nothing newer — reporting lag; episodes 012–016 are not in the data). New: rules 2 (sea > truck), 3 (money Shorts lose), 6 (AVD drop 11 s → 5 s), 7 (long videos flat). Recommendation (not applied): review the 13:00 slot.

## 6. QA (do not skip)
- Contact sheet of the long video every ~8 s: no gore, no unreadable overlaps, no black frames, subtitles inside frame.
- `ffmpeg -i long.mp4 -af ebur128 -f null -` → integrated ≈ −14 LUFS.
- Re-read script vs sources.md: every fact has a source.
- Thumbnail: view at 168×94 — the big word must still read; nothing in the bottom-right corner.

## 7. Upload to GitHub (public raw URLs for Metricool)
- Branch = weekday of the ET publish date: drop-mon … drop-sun. Orphan commit containing only that day's files (thumb + the 1–2 selected Shorts only; sX/sY = their ids), force-push:
```bash
cd /home/claude/coldwarrant-media && git checkout --orphan up && git rm -rqf . && cp $EP/thumb_A.jpg $EP/shorts/sX.mp4 $EP/shorts/sY.mp4 . && \
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
- Shorts (only the 1–2 selected, 09:00 + 15:00 ET): type "short", title = hook + " #shorts"-free short title, madeForKids false, category EDUCATION; text = 1–2 lines + "Full case file on the channel."
- Description template: 2–3 sentence summary · chapters (timestamps from timing.json chapter starts) · Sources (URLs) · Footage credit (every relay clip source: agency / network + URL) + "Appearance of U.S. government visual information does not imply or constitute endorsement." · CC photo credits.

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
