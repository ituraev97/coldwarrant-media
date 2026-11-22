# CASE FILE 022 — FACT-CHECK (independent), Nov. 22, 2026

Line numbers = /home/claude/work/script_display.txt. Source lines (src) = episode_src.py.

## REQUIRED FIXES

1. **L52 (src 155) — WRONG COURT.** Current: "On November 26, 2019, a second grand jury indicted him, this time in the Southern District of California, in San Diego."
   Problem: The Nov. 26, 2019 document is a SUPERSEDING INDICTMENT in the **District of Columbia**, Criminal No. 12-116 (BAH), Chief Judge Beryl Howell, "Grand Jury Sworn on May 7, 2019" (PDF caption: "FILED IN OPEN COURT NOV 26 2019 … UNITED STATES DISTRICT COURT FOR THE DISTRICT OF COLUMBIA … SUPERSEDING INDICTMENT"). The Dec. 6, 2019 release names only Criminal Division NDDS trial attorneys and FBI Washington Field Office, no San Diego office. (The separate S.D. Cal. case 19-CR-1272 exists per DOJ May 2025, but its date is not established.) This also makes L126 ("second time his Washington case has been rewritten") correct: 2019 = first superseding, Sept. 25 = second.
   Replace: "On November 26, 2019, a new grand jury in Washington returned a superseding indictment against him, adding to the 2012 charges."
   Also fix: src 160–162 timeline `dict(y="NOV 2019", t="Indicted, San Diego")` → `t="Superseding indictment, D.C."`; src 167 big sub "INDICTMENT, NOV. 26, 2019" → "SUPERSEDING INDICTMENT, D.D.C., NOV. 26, 2019".
   Optional add after L56: "Separately, prosecutors in San Diego have their own pending case against him."
   Sources: https://www.justice.gov/opa/press-release/file/1224016/download ; https://www.justice.gov/archives/opa/pr/leader-violent-mexican-drug-trafficking-organization-charged-international-drug-importation

2. **L58 (src 170)** Current: "$5 million, and another 6 years would go by." Problem: Dec. 2019 → Nov. 20, 2026 is 6 years 11 months. Replace: "$5 million, and almost seven more years would go by." Source: 2019 release (dated Dec. 6, 2019).

3. **L77, L79 (src 216, 222) + HAT tag (src 14) — WRONG MONTH.** The Inzunza Noriega release is dated **Tuesday, May 13, 2025** (No. 25-499; "Updated June 24, 2025"; the images sit in a /2025-06/ folder, which is where "June" came from). On-screen exhibits also read "Indictment, Filed 05/02/25".
   L77 replace "In June 2025," → "In May 2025,". L79 replace "That same June release" → "That same May release". HAT tag line 2 → "U.S. v. INZUNZA NORIEGA ET AL., S.D. CAL. · DOJ, MAY 13, 2025".
   Source: https://www.justice.gov/opa/pr/sinaloa-cartel-leaders-charged-narco-terrorism-material-support-terrorism-and-drug

4. **L80 (src 224) + HAT tag (src 14) — "seized" unsupported.** DOJ caption for _05 is: "Pedro Inzunza branded hat with Fausto Isidro Meza Flores, aka, "Chapo Isidro" and Oscar Manuel Gastelum Iribe aka, "El Musico" symbols". It never says the hat was seized.
   L80 replace: "A baseball cap. According to the Justice Department's caption, it was branded for one of that case's defendants and bore the symbols of Chapo Isidro and another alleged leader known as El Músico."
   HAT tag line 1 → "HAT WITH THE SYMBOLS OF \"CHAPO ISIDRO\" AND \"EL MUSICO\", PER DOJ CAPTION". Same source as #3.

5. **L64 (src 184–187, both stat graphics) — misattribution.** CNN gives 2,829 and 1,656 "según cifras oficiales"; they are not attributed to the Crisis Group (only the four-group breakdown is "de acuerdo con el informe").
   L64 replace: "According to official figures reported by CNN, Sinaloa recorded 2,829 intentional homicides between September 2024 and May 2026." Graphics c= → "OFFICIAL FIGURES · VIA CNN". L65 fine as is.
   Source: https://wtop.com/news/2026/07/batalla-por-el-cartel-de-sinaloa-asi-es-la-confrontacion-entre-grupos-que-ha-disparado-la-violencia-en-ese-estado-de-mexico/

6. **L67 (src 194)** Current: "…he had recently become a key ally of Los Mayos." AP: "He was also a key ally to 'Los Mayos'…" — no "recently". Replace: "The Associated Press reports that he was a key ally of Los Mayos." Source: https://www.arabnews.com/world/11-killed-in-burst-of-violence-in-northern-mexico-after-capture-of-cartel-leader-3013342

7. **L93 (src 252)** Current: "According to the AP, the firefight began around 7 p.m." AP attributes this to residents. Replace: "According to residents quoted by the AP, the firefight began around 7 p.m." Same AP source.

8. **L91 (src 248)** Current: "The AP reports they relied on stealth and surprise." AP: "Mexican authorities said that they used 'stealth and surprise'". Replace: "Mexican authorities told the AP they relied on stealth and surprise." Same AP source.

9. **L108 (src 287) — baseball game unsourced.** UnoTV (the listed source) mentions blockades "en municipios como Guasave y Ahome" but no baseball game; I could not find it elsewhere. Replace: "Mexican outlets reported roadblocks in neighboring Ahome as well." (Keep the game only if you have a specific outlet URL, and name it.) Source: https://www.unotv.com/nacional/captura-del-chapo-isidro-deja-11-muertos-en-sinaloa-cuatro-eran-militares/

10. **L82 + L86 (src 228, 236) — implies more than source.** (a) L82 "the search for him was turning violent" frames the Nov. 3, 2025 clash as a hunt for him; Reforma says forces tracked a stolen vehicle's GPS to gunmen under a bridge. (b) L86 "among them" follows "nine people who had been kidnapped were freed", so it reads as if he was among the kidnapping victims.
    L82 replace: "Meanwhile, in his home territory, the violence kept coming." L86 replace: "Rumors spread that Chapo Isidro was among those detained. The governor of Sinaloa said no prominent figure had been detained."
    Source: https://planoinformativo.com/1108667/chapo-isidro-no-fue-detenido-ruben-rocha

11. **L32 (src 103) — allegation stated as fact + "made".** InSight: "allegedly involved in trafficking marijuana, heroin, methamphetamine, and fentanyl to the United States." Replace: "And that his organization allegedly trafficked drugs north, to the United States." Source: https://insightcrime.org/personalities-mexico/fausto-isidro-meza-flores-chapo-isidro

12. **L78 (src 220) — allegation as fact.** Current: "A rival in 2013. A senior leader of the same cartel by 2026." Replace: "A rival, in Treasury's words, in 2013. An alleged senior leader of the same cartel, in the Justice Department's words, by 2026."

13. **L46 (src 143)** Current: "Ordinary businesses, in his home town, …" Treasury says only the DTO "operates out of" Guasave and the companies are "located in Guasave"; it never calls it his home town (DOJ says "of Sonora"). Replace: "Ordinary businesses in Guasave, named by the U.S. government as part of a drug trafficking organization." Source: https://home.treasury.gov/news/press-releases/tg1824

14. **L21 (src 66)** Current: "…For more than a decade, that was as precise as the public record got." This contradicts our own L41–46: Treasury publicly placed his organization in Guasave in 2013. (Also, this notice is the one attached to the Dec. 2019 release, not a 2012 document.) Replace: "The same notice says the FBI believed he was living in Mexico." (Drop the second sentence.)

15. **L33 (src 107)** Current: "…begins with a sealed piece of paper in Washington." No source says the 2012 indictment was sealed. Replace: "The American case against him begins with a piece of paper in Washington."

16. **L117 (src 307)** Current: "FBI Director Kash Patel posted the scorecard." The quote comes from the DOJ release; I found no post by Patel. Replace: "FBI Director Kash Patel kept score." Source: DOJ 26-1395.

17. **FILE FOOTAGE badges missing (legal).** In finish_ep.py the badge appears only on lines with `lab=1`. In episode_src.py only the El Chapo 2017 line (src 372) has it. sources.md says all footage is "labeled", but it isn't. The raid narration runs over unbadged Mexican-forces/patrol footage (MXU/MXW/PATROL/DIAB/DIABX), including big tags like "4 SOLDIERS KILLED". Add `lab=1` to the dict of at least src 32, 34 (L6–7), 230–237 (L83–86), 246–261 (L90–97), 264–272 (L99–103), 281–289 (L105–109), and 381/383. Also add it on every footage line in Shorts s1, s2, s3 and s5. Otherwise viewers are invited to read the file footage as this operation.

18. **Short s4 (src 438–439) — false/misleading title and hook.**
    Title "'Off the Board': FBI Says Its 11th Top Ten Fugitive Was Just Caught" reads as the FBI's 11th capture ever (the counter was already 496). Patel: "the 11th Ten Most Wanted fugitive captured under the Trump Administration." Replace: "'Off the Board': FBI Says It's the 11th Top Ten Fugitive Caught Under Trump".
    Hook "496 CAUGHT<br>[NOW ONE MORE]" implies he is No. 497. The 496 figure is from March 2025, and other captures followed. Replace: "11TH CAPTURE<br>[UNDER THIS ADMINISTRATION]" (or "496 CAUGHT<br>[AS OF MARCH 2025]").

## OPTIONAL IMPROVEMENTS
- L2: "On Saturday morning" — the release is dated Saturday, Nov. 21; I could not verify the time of day. Safer: "On Saturday, the Justice Department…".
- L116: The FBI B-roll is dated March 12, 2025 (release/slate date; the shoot date is not stated). Safer: "In FBI footage released in March 2025, five weeks after his name went up, the counter read 496." Counter 496 confirmed on frames at ~44–51 s.
- L75: Narcoterrorism (21 U.S.C. 960a) does not strictly need an FTO designation, and both charges apply to supporters, not only leaders. Safer: "That designation opened the door to terrorism-related charges against people accused of helping the cartel. Material support to terrorists. Narcoterrorism."
- L73: Driscoll's quote continues "…with fentanyl, cocaine, heroin, and other deadly drugs". Consider "flooding the U.S. with fentanyl and other drugs."
- L100: The cousin/second-in-command description comes from Mexico's Defense Ministry (La Razón, UnoTV, Proceso). Better: "Mexico's Defense Ministry describes him as Chapo Isidro's cousin and second-in-command."
- L102: The seized-items list is attributed to the Defense Ministry (Proceso). "Mexico's Defense Ministry listed what soldiers recovered…" is stronger than "Mexican outlets reported".
- L103 / L106: The AP gives the 4 a.m. extraction and the "at least 10 roadblocks" on the word of an anonymous federal official. Optional: "…a federal official told the AP…".
- src 80 doc body: the unquoted paraphrase "allegedly responsible for large quantities of heroin… into the United States" is garbled. Verbatim: "allegedly responsible for the possession, distribution, and importation of large quantities of heroin, methamphetamine, cocaine and marijuana into the United States".
- src 73 quote card: the Treasury 2023 sentence continues past "Mexico" ("…, as these organizations battled…"). End the card with "…" not ".".
- src 15 DRG tag: the drug images are _02 (1,680 kg cocaine, Mexico City) and _04 (fentanyl pills/bricks). Consider "DRUG SEIZURES SHOWN IN A 2025 BELTRAN LEYVA FACTION CASE".
- src 83 map: the "SONORA" pin sits at Hermosillo while the claim is "southern Sonora". Move it south (e.g., Navojoa/Ciudad Obregón area) or label it "SOUTHERN SONORA".
- Shorts: none carries a "charged, not convicted" line. Add a persistent on-screen line "CHARGED, NOT CONVICTED" (s1, s2, s4 especially). s2 ends on naming El Serafín; add L100 or end at L98.
- W12 tag: the wanted notice (poster2012.jpg) was published with the Dec. 6, 2019 release (DOJ file 1224021). The tag is accurate, but don't call it a "2012 poster" anywhere.

## SPECIFIC QUESTIONS
1. **Sept. 25 year:** DOJ 26-1395 gives no year, and I found no public source that does. The charges (material support, narcoterrorism) need the Feb. 20, 2025 FTO designation, so it is Sept. 25, 2025 or Sept. 25, 2026. On May 13, 2025, DOJ listed 12-116BAH as "pending" without terrorism charges. Keeping the year out is correct. The PACER docket for 1:12-cr-00116 (D.D.C.) would settle it.
2. **Hat image:** It is **_05** (250514-US-v-Inzunza-Noriega-et-al_05.jpg). Caption: "Pedro Inzunza branded hat with Fausto Isidro Meza Flores, aka, "Chapo Isidro" and Oscar Manuel Gastelum Iribe aka, "El Musico" symbols". hat.jpg matches hat_05.jpg (three panels, "120" cap, treble clef patch). Other captions: _01 "1,500 kilogram fentanyl seizure on December 5, 2024"; _02 "1,680 kilogram cocaine seizure in Mexico City" (= drugs.jpg); _03 "Cocaine seizure with the "Incredibles" brand and "R" brand"; _04 "Rainbow colored fentanyl pills and fentanyl bricks with "Louis Vuitton" and "Rolls Royce" stamps" (= pills.jpg).
3. **Reward:** Up to $5M was announced Dec. 6, 2019 by FBI WFO "in partnership with the U.S. Department of State's Narcotics Rewards Program" (DOJ 19-1355; KJZZ Dec. 13, 2019; InSight Crime "US offers $5 million reward"). It was in place long before the capture, so "$5M fugitive" is OK. Top Ten: added Tuesday Feb. 4, 2025, "the 533rd fugitive added … since it was created in March 1950" (Fox News; UPI). Confirmed.
4. **Toll and details:** Defense Ministry: 4 Army infantry soldiers, 7 attackers killed, 8 detained (3 to FEMDO in Mexico City, 5 to FGR Culiacán) (Reuters/JPost, Proceso, La Razón). AP: "stealth and surprise" (authorities); ~7 p.m. (residents); out "until 4 a.m. on Saturday" (federal official); "at least '10 roadblocks'"; helicopters/drones "opened fire on key locations across the city"; "at least 11 people dead". Infobae: ~19:50 (unattributed). Proceso: 5:20 a.m. Seized: Barrett .50, "diez armas de diversos calibres", grenade launcher, two hand grenades, magazines, cartridges, tactical gear, drugs (Sedena). Harfuch Nov. 3, 2025: 13 attackers killed, 4 detained, 9 kidnapped freed (Reforma). Johnson quote is verbatim. Crisis Group: see fix 5.
5. **14 years / 13 years:** May 2, 2012 → Nov. 20, 2026 = 14 yr 6 mo. "14 years" is fine. 2013 → 2026 = 13. Both OK.
6. **Treasury:** 2013 claims verified (7 relatives: wife, father, mother, sister, three uncles; 3 Guasave companies: grain transport, gas station, construction; quote verbatim; "extremely violent turf war"; since 2000 meth, heroin, marijuana, cocaine). 2023: no "three current leaders" phrase. The page names him with two others who "make up today's BLO's leadership", so the paraphrase (not in quotes) is OK.
7. **FBI board:** "496" confirmed in DVIDS 955350 (FBI B-roll slate "March 12, 2025"). Feb. 4 → Mar. 12 = 36 days ≈ five weeks. OK (see optional note).
8. **Legal risk:** Main items are fix 17 (unbadged file footage under raid narration and in Shorts), fixes 11/12 (allegations stated as fact) and fix 10 (Nov. 3 clash framed as a hunt for him). No victims are named. The detainees named (Galvez Meza) are already named by DOJ.

## PACKAGING VERDICTS
**Long titles**
- (a) "FBI Top Ten Fugitive 'Chapo Isidro' Captured — 4 Soldiers Killed" — SAFE. All true (FBI Top Ten; captured; 4 soldiers killed per Defense Ministry). **My pick.**
- (b) "$5 Million Fugitive 'Chapo Isidro' Captured After 14 Years" — SAFE but weaker. The reward is "up to" $5M and dates from 2019, not the full 14 years. Acceptable, not preferred.
- (c) "Wanted Since 2012: FBI Top Ten Fugitive 'Chapo Isidro' Captured" — SAFE. The most precise; good A/B alternative.

**Thumbnails**
- A "$5 MILLION / CAPTURED" over the DOJ CAPTURED poster — SAFE (the poster itself shows "REWARD OF UP TO $5,000,000 USD" and the stamp).
- B "FBI TOP 10 / CAUGHT" — SAFE.
- C "WANTED / 14 YEARS" — SAFE (May 2012 → Nov 2026).

**Shorts**
- s1 "Up to $5 Million Reward: FBI Top Ten Fugitive Captured in Mexico" / hook "$5M FUGITIVE [CAPTURED]" — SAFE, but needs FILE FOOTAGE badges (fix 17) and a "charged, not convicted" line.
- s2 "Captured in a Firefight: 4 Soldiers Killed, 8 Detained in Guasave" / "4 SOLDIERS KILLED [8 DETAINED]" — SAFE, with the same badge requirement. Consider adding L100.
- s3 "A .50-Cal Rifle and a Grenade Launcher: What Soldiers Seized" / ".50-CAL RIFLE [+ GRENADE LAUNCHER]" — SAFE (Defense Ministry list), with badges.
- s4 "'Off the Board': FBI Says Its 11th Top Ten Fugitive Was Just Caught" / "496 CAUGHT [NOW ONE MORE]" — NOT SAFE. Fix per item 18.
- s5 "10+ Roadblocks and Burning Vehicles After the Capture, AP Reports" / "10+ ROADBLOCKS [AFTER THE ARREST]" — SAFE, with badges.

## Not reachable
state.gov/fausto-isidro-meza-flores and dvidshub.net/video/955350 were blocked from this session (DVIDS metadata checked via the local clip JSON and af.mil mirror); CNN Nov. 21 article blocked (robots). Rio Times not re-checked (L95 is supported by Proceso/Sedena).
