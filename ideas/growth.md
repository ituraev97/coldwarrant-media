# GROWTH RULES — all channels (owner 2026-11-28)
Source: YouTube Help Center / Creator Insider (Todd Beaupré, Sep 2026) / YPP policy + our own YouTube Analytics (28 days).

## What our numbers say
- 85–97% of our views come from the **Shorts feed**; long videos get almost nothing from Home/Suggested. The fastest growth lever is turning Shorts viewers into long-video viewers and packaging long videos better.
- New channels get tested on non-subscribers in the first hour; if nobody clicks AND watches, impressions stop. One weak video does not hurt the channel — repeated ignored videos do.

## Every long video
1. The promise of the title/thumbnail is paid off in the first 30 s (show it, don't tease it). No slow intros, no logo stings longer than 2 s.
2. Length follows the story: for channels under 10k subs aim for **10–15 min**; 30–50 min episodes are not watched (retention 14% at the halfway point on NMTK).
3. Original script with a clear thesis + analysis + sources. Vary structure and visuals between episodes — YouTube's "inauthentic content" policy (Jul 2025) demonetizes whole channels for "templated, mass-produced" videos with minimal variation. No still image on screen > 6 s; use maps, diagrams, timelines, real footage.
4. Title ≤ 70 chars, the plain topic keywords (who/what) in the first 5 words; title and thumbnail complement each other, never repeat the same words.
5. Make 2–3 thumbnail variants for Test & Compare (YouTube picks the winner by WATCH-TIME share, not CTR).
6. Description: 2-line summary, chapters, sources. Tags barely matter.
7. Realistic AI reconstructions of real people/events → tick "altered or synthetic content". Plain AI narration needs no label. Never generate a real person's face with AI.

## Every Short
- Standalone: number / famous name / paradox in second 0, payoff at the end, 20–40 s. A steady daily flow matters more than volume (Shorts older than ~30 days fade).
- Cut Shorts FROM the long video and name the long topic, so the Shorts → long path exists ("related video" link is set in Studio).

## Thumbnails (all channels)
- ONE focal point a phone viewer gets in 0.5 s: a human face with a strong emotion, or one iconic object. Max 3 big words. High contrast, warm/saturated colours beat dark empty scenes.
- Not the same template every time (inauthentic-content risk) — rotate 3–4 layouts.
- Never AI-generated faces of real people; real photos only (government releases, archive), AI may only relight/extend.

## Voice (all channels) — owner 2026-11-28: work HARD on intonation, pace and pronunciation; every channel has its OWN voice
Engine: Chatterbox **Turbo** on the office PC / relay since 2026-11-28 (≈4.5× faster than the old Chatterbox, same quality). Never ElevenLabs for the English channels.

**Own voice per channel (never borrow another channel's voice):** use exactly the voice listed under "This channel's voice" below. Chatterbox voices are named reference clips (relay spec `"voice": "<name>"`); Kokoro fallbacks are channel-specific blends — the first (largest) voice of a blend is reserved for that channel. A new channel gets a new voice that is checked against all existing ones.

**Intonation (read the script aloud in your head before voicing):**
- Tag every paragraph with a tone: ~25% "hype" (reveals, numbers, verdicts, twists), ~15% "calm" (context, aftermath, sad facts), rest "normal". Never a whole video in one tone.
- Write for the ear: short sentences, vary sentence length, questions where the viewer would ask one, the key word at the END of the sentence. Commas where a speaker breathes; no semicolons/parentheses/colons in narration.
- Turbo understands a few sound tags — `[sigh]` `[chuckle]` `[gasp]` `[clear throat]` — at most one per minute, only where a human narrator would really do it.
- After voicing, LISTEN-CHECK by measurement: pitch variation ≥ 4 semitones, loudness range ≥ 6 LU; a flat take is re-voiced with more hype/calm contrast, not shipped.

**Pace:** long narration 150–165 wpm, Shorts 160–180 wpm. Never speed long narration up with atempo to fit a duration — cut words. No silence > 0.6 s inside narration except one deliberate beat before a reveal. Sentence gaps 0.3–0.45 s.

**Pronunciation:**
- Numbers, dates, money and units are written OUT in words in the TTS text ("twenty twenty-four", "fifty billion dollars", "forty percent").
- Every name, place, brand or foreign/rare word gets a phonetic respelling in the TTS text the first time it is unclear, e.g. `Jaquan` → `Jay-kwahn`, `Huwaitat` → `Hoo-why-tat`, `Riyadh` → `Ree-yahd`; keep the real spelling in subtitles/titles. Keep a per-channel list in `voice_lexicon.md` (word → respelling) and reuse it every episode.
- Acronyms: letters with hyphens when spelled (`F-B-I`), as a word only if people say it as a word (NASA).
- Check the Whisper QA report: any line with similarity < 0.86 or a misread name is re-voiced before rendering.

## This channel
- MONETIZATION PUSH (owner 2026-11-28): subscribers are done (4,110 ≥ 1,000); the ONLY missing YPP requirement is 4,000 public long-form watch hours in 12 months — we have 6. Shorts watch time does NOT count. Every decision now optimises LONG-FORM watch time.
- Every long: cut 3–4 Shorts from it the SAME day, each Short is a teaser that ends on an open question the long answers, and the Short title names the case. The owner's Claude links each Short to its long (Studio 'Related video'); list the Short↔long pairs in shorts_link.json as before.
- Long cadence: 1 long per day when a PROVEN topic exists (radar breakout ≤72 h in ideas/next.md, or one of our Shorts > 500 views without a long yet); otherwise 1 every 2 days. Proven topics first, always.
- Series: give every long a series label in the description first line (CARTELS · COAST GUARD · GANGS · MONEY · TUNNELS) so playlists/end screens chain episodes; end the long on a one-line teaser of the next case in the same series.
- Auto-dubbing is ON for this channel (20 languages) — non-English viewers now count toward watch hours; keep titles/thumbnails localised (dub text + thumb_loc per RUNBOOK 'Dubbing v2').
- Thumbnails: put a PERSON on every long thumbnail (the defendant's DOJ/agency photo, agents in action from DVIDS, or a gang's known emblem/name) — our dark empty scenery plates lose to competitors who show a face or a named gang (Hells Angels, Mexican Mafia).
- Name the gang/cartel/agency the audience knows in title + thumbnail (≤3 words).
- Longs only on stories where a competitor breakout or our Short already proved the topic (see ideas/next.md).

## Voice
- This channel's voice: Chatterbox Turbo, relay voice "cw" (=cw_a); Kokoro fallback ONLY this blend: bm_fable:0.4+am_michael:0.3+bm_george:0.3 (owner choice 2026-11-27). Do not use any other channel's voice.
- Voice audit 2026-11-28: lively (pitch 6.9–7.3, 157–169 wpm) — keep the current narrator.
