# PACKAGE_REPORT — CASE FILE 030 (episode B)
Title (chosen): He Called Himself the Dead End Boss Man — Now It's 25 Years (59 chars)
Protagonist: Kendrick Jamal "Peanut" Young, 39, Four Deuce Oakland Crips, Dallas — pleaded guilty Sept 2025; 300 months, Judge Godbey, N.D. Tex., Nov 23 2026.

## Numbers
- Spoken words: 2,511 (scripted at 155 wpm = 16.2 min speech; with ~139 line gaps est. 18 min). Cold open 87 words (~35-38 s). LINES = 139 (3-tuples verified by import with python3 -I). Chapters I-VI + g:title after cold open + g:end. Graphics 37 of 139 lines.
- Gaps varied 0.3-2.4 (max run 3); speed 0.94-1.06.

## STORY CAVEAT (important)
Young's personal backstory DOES NOT EXIST in any public source I could open (no childhood, no joining story, no prior-conviction details, no family; Fox 4 explicitly says none reported). I did NOT invent one. The script says so on camera (ch. I) and tells "the Dead End Boss Man" as crew + one house + the federal case, using only sourced facts: Williams (Corvette carjacking), Love (248 mo.), Hewitt (trial, Zillionaire store, 37+ yrs), the Feb 2025 takedown (alligator, 14 guns), Young's admissions, the Oct 22 2024 house search, city lawsuit, sentencing. History of Four Deuce in Dallas: no primary source found; script says the releases do not give it.

## 7 DOJ evidence photos (img/doj_pic1-7.png; US government, public domain; only 268-307 px wide, NO captions in the release — descriptions are mine from looking at them)
1. doj_pic1 (307x311): Instagram-story-style screenshot: man's face (mouth open, looking down-left) with a large chain/pendant reading "DEAD END", caption text with hashtag #DEADENDBOSSMAN, account handle strips top + bottom -> CROP/BLUR handles. Not captioned: do not name the face on screen as Young (placement right after the medallion paragraph strongly suggests it).
2. doj_pic2 (268x251): AR-style pistol with long magazine on a maroon pillow, loose round beside it, a second magazine above, clothes around.
3. doj_pic3 (279x250): black handgun on a heap of belongings: soda bottle, loose coins/small items in a bag.
4. doj_pic4 (272x298): white powder on a white plate; clear wrapped/zip packages in front.
5. doj_pic5 (291x298): large black trash bag opened, containing a big clear bag of green plant material (release lists multiple kg marijuana).
6. doj_pic6 (279x330): gloved hands (purple nitrile) holding a large plastic jug of dark reddish liquid in a bedroom; other gloved hand at left. (Contents not identified in the release — script does not say PCP.)
7. doj_pic7 (273x337): silver/black pistol with a loose magazine, a holster, an ammunition box and cartridges on a bedspread.
Also exists but NOT downloaded (URL not exposed): Williams release photo (blue "42" cap + gold/diamond necklace), Love release images L1/L2, Hewitt "Pills" photo.
Resolution warning: photos are tiny -> blurred-bed + framed card + slow 'in' only; thumbnails cannot be full-bleed from these.

## Clips (honest)
- Relay (YouTube): NO official/mainstream video of the exact event surfaced from 7 searches. One unverified candidate: tHSRHnzngnc "Have You Heard? Dallas Crime News — Eight Alleged Gang Members Arrested in South Dallas Crackdown" (1:02, small outlet, content/commentary UNKNOWN — build agent must watch; drop if it has anchor faces/commentary/victims). Rejected: CBS Texas fXSVUGqOtj0 (a different Sept 2026 case, 19 indicted), WFAA OxcDtLE_T_4 (Sept 2025 open-air bust, location unverified), YouTubers (Negative Ass Shon, Zillionaire Doe fan channels) = commentary, excluded.
- DVIDS (all lab=1, none in used_clips.json): 1006548, 462181, 820502, 426013, 544036 (+ spares 1006820, 1007837, 1006222). Start seconds in episode.py are PROVISIONAL (only captions read, none downloaded). ATF crime-gun-lab/NIBIN/training b-roll is generic; no street/raid footage of Dallas exists in DVIDS. => Visuals are ~35% DOJ photos/graphics + generic labeled ATF footage. The 'Promise rule' is met by the DOJ photos (dd1, seizure list) in the first minute, not by event video. If tv1 fails there are 5 DVIDS clips (+3 spare) = >=6 total, but footage is the weakest part of this package.
- 'tv1' lines (5) are the only lab=0 lines; if the clip is dropped replace with D(1006548,..) lab=1 or graphics.

## Risks / uncertain items
1. WebFetch returns summaries of justice.gov, not raw text: the Raybould "impunity" quote (two fetches differed: "operate"/"act") and the Hewitt "living in fear" line are PARAPHRASED in the script on purpose; verbatim quotes used: Garner x2 (Fox 4 + Yahoo agree), Raybould "Armed gang members...period." (Williams release, two fetches agree), Bazaldua (Dallas Morning News), 18 USC 924(c), Hewitt caption "I am a drug lord."
2. Source conflicts: Williams plea date (Aug 26 2025 vs June 3 2025) -> "in 2025"; arrests Tue Feb 25 (court appearances Wed Feb 26) vs release "Monday" -> "last week of February"; which school (DISD Wheatley Elementary + charter vs former Phillis Wheatley/Cornerstone Crossroads) -> "near schools" only; Hewitt age 40 (DOJ) vs 39 (Fox) -> age omitted; "12 pleaded guilty" (Young release) vs "12 convicted" (Williams release) -> script attributes "12 pleaded guilty" to the Nov 23 release.
3. Map graphics use an approximate marker for Casey St / Malcolm X Blvd (label says so).
4. Minors: the release says the block is near schools; script states only that. NOT used: "sent young people to recover drugs" (ambiguous), the June 2025 drive-by (victims' ages unknown), Hewitt's prior record (includes a minor-related offense).
5. Young's social-media screenshot: handles must be hidden; the person is not captioned by DOJ.
6. Dates: all stated per sources; "twenty-one months" = Feb 25 2025 -> Nov 23 2026 (computed).
7. Kokoro fallback respell.py provided (names: Godbey, Raybould, Meacham, Toliver, Bazaldua, Calvert, Wheatley, Hewitt, Brantley, Garner, caiman); Chatterbox hint: Godbey, Raybould, Meacham, Toliver, Bazaldua, Calvert, Wheatley, Hewitt, Starr, Garner, Casey, Four Deuce, Crips, K2, PCP, ATF, Zillionaire.
8. No git/TTS/graphics/build was run; pipeline/ and tools/ untouched.
