# CASE FILE 029 — independent fact-check (2026-11-28)
Method: re-opened the cited pages (justice.gov pages via WebFetch; MyNewsLA, KPCC/LAist, Corrections1 and Ning Register reprints, AP via Knoxville Daily Sun, New Santa Ana, ABC7, CBS LA, L.A. Taco, Medium) and checked every spoken line and every on-screen graphic/tag in episode_src.py (episode.py regenerated with pre.py; 140 lines, all 3-tuples, 2,8xx spoken words).

## Issues found and fixed
1. L5 "dozens of gangs" -> "about two dozen" (McNally: about 24 gangs).
2. L14 "significant control" (DOJ April 2026 release says "immense control") -> "immense control"; L15 wording aligned to release.
3. L17 "Ojeda, who was free at the time" -- no source states his 1992 status (Register says he left state prison 1987, paroled 2000). Removed; "rival" -> "warring" gangs (Register wording); graphic body updated.
4. L23 + graphic: "first federal racketeering case ever" -> Register says "first RICO indictment" against the Mexican Mafia; now attributed to the Register, "federal" dropped.
5. L26 "federal agents came for him" -> "authorities" (Santa Ana Gang Task Force: local, state, federal).
6. L27 "grand jury in Santa Ana" -- release does not say where; now "A federal grand jury".
7. L40 "Moreno testified that Ojeda asked him..." -- source does not clearly attribute this to testimony; now "Prosecutors said Ojeda asked him...".
8. L41 "treated like a brother" -> McNally's words "like a brother to him"; L42 attributed to prosecutors.
9. L44/L46/graphic "secretaries" -- word is in the 2022 DOJ release only, not in any trial coverage. Replaced with "go-betweens" (DOJ verdict release: "messenger"). L115 claim "same word McNally had used" removed.
10. L45 kites "on their own bodies" -> McNally: hidden in the rectum; now "inside their own bodies", attributed to the prosecutor.
11. L51 Moreno "was charged with conspiracy to commit attempted murder" -- Register: a prison rule violation, and he was released that morning. Corrected.
12. L55 + graphics: "rumor" conflated with the 1991 conviction; Register says only that a rumor spread about something in his past. Reworded; added that the conviction was later overturned in part (Register); removed "Latino" from victims (Register does not state it); timeline label changed.
13. L64 "dozens of people" -> 34 arrested that morning (AP: 26 federal + 8 state).
14. L66 "Orange County prosecutors charge the rest" -> "bring state charges against others" (57 federal of 99 = 42, but DOJ says 40 county).
15. L77 "begins with a sentence that holds the whole case" -> quote on screen is McNally's "This is a case about power and control"; line now says that.
16. L76 graphic "trial of about two and a half months" -> "about two months" (DOJ verdict release: evidence began about two months earlier; 2.5 days was the deliberation).
17. L90 + graphic: plea-withdrawn claim is her attorney's account (MyNewsLA June 6, 2016), not the report's finding. Attributed to her lawyer.
18. L110 "CBS reported they had filled the leadership void" is guilt-implying about charged men -> "in prosecutors' account".
19. L114 "had threatened to talk to law enforcement" -> DOJ: "purportedly claimed he would speak" -> "reportedly said he would talk".
20. L119 graphic header credited USAO July 2026; the verdict is from CBS LA (July 22, 2026) -> header "FEDERAL JURY · JULY 2026".
21. L122-130 "Operation Gangster's Paradise": the DOJ release does not name an operation (FBI Director/KABC and others say "Gangsta's Paradise"). Spoken line now "News reports call it Operation Gangsta's Paradise"; on-screen tags changed to "MEXICAN MAFIA ARRESTS · APRIL 23, 2026"; "Before dawn" -> "That morning" (release says "this morning"). Also fixed in titles.md tags and youtube_description.txt sources.
22. Graphic 1960s card: "About 30 members" attributed to Register -> to Leo Duarte via the Register.
23. titles.md: Selna quote "running the gang from prison" was a paraphrase in quote marks; alternative pinned comment said the 15 years were "because of" special cunning (judge cited age and humanitarian reasons for leniency). Fixed.
24. short.md "Four years later" -> "Four and a half years later" (July 2011 -> Jan. 2016).
25. youtube_description.txt: allegation caveat now covers 2018, 2022 and 2026 cases.

## Verified (no change)
Ojeda biography (born 1942, 11th grade, 1965/1970/1977, paroled 2000; Register); 2005 indictment (June 8/15, 63, La Habra, 3 counts, 16/19 defendants, Yang and Rimmer quotes); 2006 plea, 14 years; Lewisburg; Moreno/Aguilar/Navarro details; Chino riot (~200 injured, 55 hospitalized, $5.2M); Theo Lacy orders and hard-candy list (Register, indictment); Moriel (July 2009-Sept. 2010, four trials, 79 convictions, DA release); Black Flag (99, 500+, 5 indictments, 57, 28; Birotte and Hutchens quotes verbatim); Smokin' Aces (129, 67 weapons, "crucial", Ojeda not charged); trial quotes (McNally, Wilke, Kenney); verdict (Jan. 13, 2016, ~2.5 days, Decker quote verbatim); sentencing (15 years, 17 asked, Selna quotes, Ojeda "I understand that"/"Somewhere in California"); Rodriguez 78 months (88 planned), apology quote verbatim, 9th Cir. Aug. 20, 2020 (Thomas dissent in part); death June 7, 2018, age 76; 59 + 40; Martinez July 30, 2018 (42, 15-to-life, Rackauckas quote); 2022 indictment (33 counts, 31, leaders, 2 murders/6 attempted, structure 3/5/1/2, Wilkison and Johnson quotes); Oct. 2023 convictions; July 2026 Cordova/Valenzuela (CBS); April 23, 2026 (25 arrested, 40 defendants/66 counts, Cardenas 48, seizures, Anaheim motel murder, Essayli quote verbatim); Oct. 30, 2026 charges (ages, Christmas 2016, mandatory life/death-eligible, presumed innocent).

## Residual notes (not errors)
- "2,000+ MILES" Santa Ana to Lewisburg is a computed figure (about 2,300 miles great-circle), not in a source.
- CBS gives Oct. 22 sentencing for Cordova/Valenzuela; DOJ Oct. 30 release says March 25, 2027; script uses the later official date.
- youtube_description chapter timestamps are 0:00 placeholders; fill after the render.
- Thumbnails: no real face; words CONVICTED / TWICE, 99 CHARGED, dates verified; Plate A/B are labeled AI scenes with no real person.

VERDICT: PASS
