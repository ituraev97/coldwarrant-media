# CASE FILE 020 — Independent fact-check (2026-11-19)

Pages opened myself: USAO W.D. Tex. Nov. 12, 2026 [R1], March 13, 2026 [R2], May 4, 2026 Galvan [R3], Feb. 25, 2026 Najera [R4], Aug. 1, 2023 Medina [R5]; GAO-21-322; CRS IF12190; DOJ OPA June 11, 2024; ABA Journal June 5, 2025; Faegre Drinker summary of Smith & Wesson v. Mexico.
R1 = https://www.justice.gov/usao-wdtx/pr/firearms-smugglers-sentenced-del-rio-combined-395-years-federal-prison
R2 = https://www.justice.gov/usao-wdtx/pr/mexican-firearms-smuggler-sentenced-15-years-federal-prison-15000-fine-del-rio
R3 = https://www.justice.gov/usao-wdtx/pr/texas-man-found-guilty-hstf-case-involving-large-scale-cartel-firearm-trafficking
R4 = https://www.justice.gov/usao-wdtx/pr/north-carolina-family-members-plead-guilty-trafficking-firearms-mexican-cartel
Could NOT open: DVIDS 965069 (permission timed out), so line 167's press-event details are unverified by me. Photo contents (sign text, evidence tags) were not checked visually.

## Problems, most severe first

1. **L162–171 (production bug, critical).** Lines 165 ("Two years later…500 defendants") and 167 ("Then, in February 2025…FTO…press event") are pasted *inside* the BSCA `cards3` `cards=[...]` list. Python parses them as cards (verified: LINES has 147 entries, neither line is in it; cards = dict, tuple, tuple, dict, dict). They will never be spoken and the graphic will get two malformed cards. **Fix:** close the cards3 after the §932 card with the §933 and PENALTY cards, then put L165 and L167 as their own LINES entries after it.

2. **L204 "But the stop at Eagle Pass didn't just catch a courier. It set off everything else." (+ L174 "But first, somebody had to get caught at the border.")** Causal claim no source makes. R1 says only that Montelongo-Loera "was arrested on July 14, 2025, after a co-conspirator was found attempting to smuggle eight handguns and 19 magazines into Mexico." The investigation was already running from Aug. 2024 (R1). R2 makes no link. **Replace L204:** "Two days after that stop, the case moved fast." **L174:** "Then, in July 2025, a car was stopped at the border."

3. **L96 and L98 doc card: "posted photos of himself with multiple firearms, as his profile pictures" / "Had posted photos of himself with multiple firearms…"** R1: Montelongo-Loera "had displayed multiple firearms in his social media profile pictures." It does not say the photos showed him. **Replace (spoken):** "According to federal prosecutors, his social media profile pictures displayed multiple firearms." **Card:** "Had displayed multiple firearms in his social media profile pictures · Was also recorded crossing in the same vehicle". Related: L100 "Out where anyone could see it" and L371 "where anyone could see them". R1 says nothing about who could see them. Cut both, or use "on his own social media profile."

4. **Thumbnail A "200+ GUNS / INTO MEXICO" over the San Antonio seizure photo + "SENTENCED · 39.5 YEARS".** The pictured guns were seized and never crossed. The 200+ figure belongs to the 10-conspirator case (R1, Simmons: "ten conspirators who smuggled more than 200 weapons into Mexico"), not to the three sentenced, and the source says "weapons," not "guns." **Replace:** "24 GUNS SEIZED" over this photo, or "200+ WEAPONS / 10-PERSON RING, PROSECUTORS SAY" over a non-seizure image. **Long title:** "Brother, Sister, Husband: The Gun Ring That Sent 200+ Into Mexico" pins the ring-wide count on the family. **Replace:** "Brother, Sister, Husband: Inside a 10-Person Gun Ring That Smuggled 200+ Weapons Into Mexico". **L46 title card:** "THE FAMILY PIPELINE" with sub "200+ WEAPONS INTO MEXICO" has the same problem. Use sub "10 CONSPIRATORS · 200+ WEAPONS, PER U.S. ATTORNEY".

5. **L242 "But someone at the U.S. Attorney's Office decided that picture belonged in the case file they showed the public." (Santa Muerte, L238–243).** This is insinuation, and "case file" is wrong: it was a press-release photo (R2). It also leaves out what the government actually wrote. R2 caption: "Additional La Santa Muerte (Saint Death) statues inside Reymundo Hernandez-Nino's San Antonio residence, where law enforcement executed a search warrant on July 16, 2025. La Santa Muerte is a spiritual icon found among members of various Mexican drug cartels." **Replace L242:** "The government's caption says La Santa Muerte is a spiritual icon found among members of various Mexican drug cartels. It does not say the statues are evidence of any crime, and owning one isn't one." L240 ("popular across Mexico, among all kinds of people") is general knowledge, not in any source. Keep it only if you add a source.

6. **L353 "Two families. Two cartels. Same courthouse. Same pattern. Buy the guns here, drive them south within days, and let the cartel pay for the trip."** The Montelongo case's cartel is unnamed, so "two cartels" is unsupported (it could be Sinaloa too). No source says either cartel "paid for the trip." Cruz-Cardoza's payer isn't named (R2), and the Najeras cited a debt (R4). **Replace:** "Two families. Same courthouse. A similar pattern, according to prosecutors: buy the guns in the U.S., and move them south within days."

7. **L202 "For the cartel on the other end, that's cheap."** No source says who was paying Cruz-Cardoza or that the Eagle Pass guns were cartel-bound. ATF's cartel determination is about the San Antonio items (R1/R2). **Replace:** "For the courier, the price turned out to be fifteen years." (Drop the cartel sentence.)

8. **L318 "One was recovered after a shootout between cartel members and Mexican law enforcement."** This implies the rifle was one of the 24. R3: Galvan "straw purchased numerous weapons, to include an AK-47 rifle that was recovered after it was used in a shootout between cartel members and Mexican law enforcement." It does not say that rifle was one of the 24. **Replace:** "Another gun he straw-purchased, an AK-47 rifle, was recovered after it was used in a shootout between cartel members and Mexican law enforcement."

9. **L314 "In May, a jury there convicted…"** R3 is dated Monday, May 4, 2026, and gives no verdict date. The verdict may have come in late April. **Replace:** "In May, prosecutors announced that a jury there had convicted…"

10. **L280 "There's no parole in the federal system. A federal sentence is served, not waited out on a parole board."** Federal parole was abolished for offenses after Nov. 1, 1987, so that part holds. But the second sentence implies the full term is served, and inmates can earn up to 54 days a year of good-conduct credit. No source in sources.md covers this line. **Replace:** "There's no parole in the federal system. With good-conduct credit, federal inmates generally serve at least about 85 percent of their sentence." Cite 18 U.S.C. §3624(b) / BOP.

11. **L43 "And it ended with a man's own profile pictures."** Chronology is wrong. The profile pictures were in the Aug. 2024 information (R1). The case ended with the July 2025 arrests, search and sentencing. **Replace:** "And a man's own profile pictures."

12. **L130 "why a few pistols bought in Texas matter"** R1 does not say where Kenia bought the guns. **Replace:** "bought in the United States".

13. **L339 "A text message on his phone showed an unsaved Mexican number asking for fifty guns"** + L341 card. R4: a text exchange between the father (Najera) and son (Najera-Avalos) contained a screenshot of a message in which "an unsaved Mexican phone number asked for 50 guns over a few months" beginning in March 2024. **Replace:** "Texts between the father and son included a screenshot of a message from an unsaved Mexican number, asking for fifty guns over a few months, starting in March twenty twenty-four." **Card:** "Screenshot shared between father and son: an unsaved Mexican number asks for 50 guns over a few months, starting March 2024 · …"

14. **L335 "the sons bought the guns in North Carolina"** R4 says the sons "would purchase the firearms and provide them to their father to transport into Mexico," and the trips "typically occurred within a week after purchasing firearms." Only the Oct. 31 rifle is placed in North Carolina. **Replace:** "Prosecutors say the sons bought the guns, and the father drove them to Mexico, usually within a week of the purchases." L337 "over five trips": the five trips were the father's crossings (R4: "On those five occasions, Najera-Avalos purchased a total of 14 firearms"). **Replace:** "…bought fourteen firearms tied to five trips his father made…"

15. **L106 "When his sister made those trips into Mexico, Montelongo-Loera was recorded crossing in the same vehicle."** This implies every trip. R1: "Montelongo-Loera…was also recorded crossing in the same vehicle." **Replace:** "And Montelongo-Loera, prosecutors say, was also recorded crossing in the same vehicle." The L98 card is fine once "also" is added.

16. **L55 "…the government never said the woman…lied on a form, and she wasn't charged with that."** We have not seen the indictment, so "wasn't charged" is unverified. R1 lists only her plea. **Replace:** "…the government's releases never say the woman at the center of this story lied on a form, and that isn't what she pleaded guilty to."

17. **L125 card MOVE "Across at Laredo & Eagle Pass" / "Days after purchase · couriers paid per gun"** and **L124 BUY "Requested guns obtained by a \"buddy\""**. These conflate Kenia's Laredo crossings with Cruz-Cardoza's Eagle Pass stop. "Couriers" (plural) paid per gun rests on one man's statement (R2). R1 says the buddy "could get requested firearms," not that he obtained them. **Replace:** BUY s="A \"buddy\" who could get requested firearms". MOVE t="Crossings at Laredo; a courier stopped at Eagle Pass", s="One courier said he'd be paid $150–$200 per gun".

18. **L117 quote card `…a "buddy" who could obtain requested firearms, and someone to transport them.`** This is a quote card that doesn't match the source wording. R1: "his “buddy” could get requested firearms and that he had someone who could transport them." **Replace:** q='his "buddy" could get requested firearms and…he had someone who could transport them.'

19. **L282 order error.** "Simmons went further…prison of addiction" plays *before* L284/286 introduce Simmons and the "terrorize" quote. In R1 the "terrorize" sentence comes first. **Fix:** move L282 to after L287. **L287 card:** R1 reads "Specifically, these weapons are used by cartels to terrorize Mexican citizens and war with law enforcement…". Change q to "…these weapons are used by cartels to terrorize Mexican citizens and war with law enforcement…".

20. **L158 "Before 2022, there was no federal statute aimed specifically at straw purchasing or gun trafficking. …which critics called mere paperwork violations."** The cited CRS IF12190 doesn't say "no federal statute aimed specifically." It says straw purchases were "unlawful under two existing laws," prosecutions of which "have been characterized by some as mere paperwork violations." **Replace:** "Before 2022, straw purchases were usually prosecuted as false statements on the paperwork, cases that some characterized as mere paperwork violations." **L160 card:** 'Characterized by some as "mere paperwork violations"'.

21. **L164 card "18 U.S.C. § 932 / Straw purchasing / Buying a gun for someone else"** oversimplifies. §932 covers buying for someone the buyer knows or has reason to believe is prohibited or intends to commit certain crimes (CRS IF12190). **Replace s:** "Buying a gun for a prohibited person or a criminal purpose".

22. **L236 "The government hasn't named the cartel publicly" and L375 "The cartel they were meant for hasn't been named."** We only know the press releases don't name it (R1, R2). **Replace:** "The government's press releases don't name the cartel" / "isn't named in the government's releases."

23. **L270 "On Tuesday, November tenth, they stood before Chief U.S. District Judge Alia Moses."** Tuesday = Nov. 10, 2026 is correct (Thursday Nov. 12 release). But R1 names Moses only for Montelongo-Loera's sentence; the other two are in the passive voice. **Replace:** "On Tuesday, November tenth, all three were sentenced in federal court in Del Rio."

24. **L140 "…so thousands of guns recovered by Mexican states never make it into the data."** GAO: ATF "does not receive complete data about thousands of firearms, such as those recovered by Mexican states." **Replace:** "…so A-T-F doesn't get complete data on thousands of guns, like those recovered by Mexican states." Also L144 "the seizures were small by comparison": this compares different datasets and periods (GAO). **Replace:** "And on the U.S. side, ICE-led task forces seized…"

25. **L367 pistols photo (tag=EP) under "Kenya Montelongo bought at least eight pistols…".** Those are Cruz-Cardoza's Eagle Pass handguns, not her purchases. The juxtaposition implies they are hers. **Fix:** use footage or a neutral card.

26. **L41 "Then a car full of pistols"** and **Thumbnail B "8 PISTOLS / CAUGHT AT THE BORDER"**. R2 says "eight handguns" (it does not say they were all pistols), and eight is not "a car full." **Replace:** "Then a car carrying eight handguns…" / "8 HANDGUNS / CAUGHT AT THE BORDER".

27. **L258 "In March 2026, he was sentenced…"** R2 gives no sentencing date (displayed date March 13, 2026; metadata publish March 12). **Replace:** "In March 2026, prosecutors announced his sentence: fifteen years…"

28. **L327/L330 "in February, three more defendants pleaded guilty" / card "PLEADED GUILTY · FEB. 2026".** R4 (Feb. 25, 2026) gives no plea date. **Replace:** "And in February, prosecutors announced that three more defendants had pleaded guilty in Del Rio." Card: "PLEAS ANNOUNCED FEB. 25, 2026".

29. **L357 doc stamp "DISMISSED".** The Court reversed the First Circuit (which had revived the suit). Unanimous, Kagan; PLCAA bars the suit because aiding and abetting wasn't plausibly alleged (ABA Journal; Faegre Drinker). **Stamp:** "REVERSED". "Threw that lawsuit out" is acceptable shorthand.

30. **Short 3 title "'Between $150 and $200 for Each Firearm': What a Gun Courier Told Investigators".** The quoted words are the release's paraphrase ("Cruz-Cardoza stated he would be paid between $150 and $200 for each firearm he smuggled"), not his words. **Replace:** "Paid $150–$200 Per Gun: What a Gun Courier Admitted, Prosecutors Say". **Short 5:** add attribution, "…by One 10-Person Ring, Prosecutors Say". **Thumbnail C "4,000 ROUNDS"** → "4,000+ ROUNDS" (R1: "more than 4,000").

31. **L51 "answers a question near the top of it"** (Form 4473 "actual buyer" question). The position is unverified. **Replace:** "answers a question on it."

32. **L25 "Last week".** Nov. 10, 2026 is "last week" only if the video publishes by Sun. Nov. 22, 2026. Otherwise say "On November 10".

33. **Unverified by me:** L167 press event details (DVIDS 965069 blocked; "put seized weapons on a table" not confirmed). L192 sign text "Port of Eagle Pass, Texas" and L230 "Every gun…carries its own evidence tag" need a visual check of the DOJ photos. L172 "exactly the charge": releases don't cite §933; soften to "That's the charge…".

## Verified OK
- Names, ages, residence. Montelongo-Loera, 39, of Dallas. Kenia Lizbeth Montelongo, 31, his sister and Hernandez-Nino's wife; "younger/older" follows from the ages. Hernandez-Nino, 41, described as an illegal alien from Mexico, with a San Antonio residence. (R1)
- Sentences 180/150/144 months = 474 months = 39.5 years. "On Tuesday" in the Thu. Nov. 12, 2026 release = Nov. 10, 2026. (R1)
- Pleas: Montelongo-Loera, conspiracy to traffic firearms, Feb. 23. Hernandez-Nino (Feb. 26), smuggling goods and alien in possession. Kenia, smuggling goods and sale or transfer to a prohibited person. (R1/R2)
- Purchases May 17–July 5, 2024: seven .380 pistols and a .22 pistol. Crossings through Laredo in the days after each purchase. ATF information Aug. 2024. WhatsApp Aug. & Nov. 2024. (R1)
- Arrest July 14, 2025, after a co-conspirator was found attempting to smuggle 8 handguns and 19 magazines. Search two days later (July 16 per R2) by ATF, SAPD and ICE ERO. 24 firearms immediately recovered (handguns, AR-15-style rifles, a shotgun), 4,000+ rounds, multiple sets of body armor. ATF determined, "based on other evidence," that they were bound for a Mexican drug cartel. Couple arrested during the search. (R1/R2)
- Simmons "massive case…ten conspirators…more than 200 weapons into Mexico," "terrorize…war with law enforcement…routes," "prison of addiction" (R1). Weddel "played significant roles…intended for a Mexican drug cartel" (R1). Simmons "This case is the model for how a Homeland Security Task Force should work" and Weddel "The illegal trafficking of firearms to Mexico directly fuels cartel violence" (R2).
- Judge Moses, AUSA Brett Miner, Case 2:25cr1979. HSTF under EO 14159; Operation Take Back America. (R1/R2)
- Cruz-Cardoza, 52, of Piedras Negras. July 12, 2025, Eagle Pass outbound inspection, negative declaration (firearms, ammunition, currency over $10,000), CBP vehicle search: 8 handguns, 19 magazines. Said he'd be paid $150–$200 per firearm; smuggled about 10–12 previous times. Pleaded in September; 180 months; $15,000 fine in the headline only. Francisco Cardoza Jr. pleaded in October. Photo captions for the Eagle Pass and San Antonio photos. (R2)
- Galvan: 30, jury in Del Rio, two counts. Sept. 16, 2023–Apr. 14, 2024. 24 AK-47-styled firearms. Attempted to obliterate serials. Toluca. LNFM, FTO-designated Feb. 20, 2025. (R3)
- Najera: 54, Elon, N.C. Sons 26 and 22. Sinaloa Cartel. 14 firearms June–Oct. 2024. Debt; $70,000. Oct. 31, 2024 Del Rio outbound inspection, CBP alert for crossing history, black tarp in the truck bed, disassembled rifle and box magazine. Denial, warning, then admission. Conspiracy pleas; up to 15 years each. (R4)
- Medina: Sept. 2020 Del Rio outbound lane, didn't declare, duffle bag of small boxes in the trunk, 10,498 rounds, 57 months. (R5)
- GAO-21-322 (Feb. 2021): 70% figure (2014–2018, traced, ATF data); "national security threat" quote verbatim; ICE 1,012 vs ATF 56,000; 1,104 seized FY2015–17; CBP increased outbound inspection at some ports in FY2020.
- CRS: BSCA June 2022, §932/§933, attempts and conspiracies, up to 15 years (25 in some straw cases); prior 10-year and 5-year false-statement provisions.
- DOJ OPA June 11, 2024: "charged more than 500 defendants."
- Smith & Wesson v. Mexico, June 5, 2025: unanimous, Kagan; both Kagan quotes match the ABA Journal wording.
- Shorts 1, 2 and 4 titles are supported (R1/R2). Short 4 matches "In the days following each of the purchases, Montelongo crossed into Mexico through Laredo."
