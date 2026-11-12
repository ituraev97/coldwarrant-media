# CASE FILE 014 — How a Black Hawk Stopped a Cocaine Boat Off Puerto Rico
# Each entry: (vo_text, shots, opts)  — same format as episodes/001-ms13/episode.py
# shot: ("clip_id", start_sec, {opts}) | ("g:<graphic_name>", 0, {opts})
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

BH = ("CBP AIR AND MARINE OPERATIONS · NORTH OF SAN JUAN", "MAY 14, 2026 · THE CASE IN THIS FILE · CBP VIA DVIDS")
BHIR = ("AIRCREW INFRARED · THE YOLA, MAY 14, 2026", "NORTH OF SAN JUAN · CBP VIA DVIDS")
BHB = ("AGENTS BOARD THE YOLA · MAY 14, 2026", "FACES BLURRED BY CBP · CBP VIA DVIDS")
MACEDA = ("CBP MARINE UNIT · OFF PUERTO RICO", "SEPT. 2025 · CBP VIA DVIDS")
VAL = ("AMO AIRCREW VIDEO · GO-FAST NE OF THE DOMINICAN REP.", "FEB. 2025 · USCG / CBP VIA DVIDS")
P3 = ("CBP P-3 AIRCREW VIDEO · CARIBBEAN", "2021 · CBP VIA DVIDS")
P3L = ("CBP P-3 AIRCREW VIDEO", "RELEASED APRIL 2021 · CBP VIA DVIDS")
P3B = ("CBP P-3 AIRCRAFT", "ILLUSTRATIVE · CBP VIA DVIDS")
P3I = ("INSIDE A CBP P-3 · RADAR STATIONS", "ILLUSTRATIVE · CBP VIA DVIDS")
MEA = ("CBP MULTI-ROLE ENFORCEMENT AIRCRAFT · SAN DIEGO", "APRIL 2026 · ILLUSTRATIVE · CBP VIA DVIDS")
HAWK = ("CBP UH-60 BLACK HAWK · SAN DIEGO", "SEPT. 2025 · ILLUSTRATIVE · CBP VIA DVIDS")
CIV = ("CBP COASTAL INTERCEPTOR VESSEL · SAN DIEGO", "2021 · ILLUSTRATIVE · CBP VIA DVIDS")
OFF20 = ("COAST GUARD OFFLOAD · SAN JUAN", "OCT. 2, 2020 · 62 BALES · USCG VIA DVIDS")
OFF22 = ("COAST GUARD OFFLOAD · SAN JUAN", "APRIL 2022 · ~1,000 KG · USCG VIA DVIDS")
OFF21 = ("COAST GUARD & CBP OFFLOAD · SAN JUAN", "JULY 2021 · 502 KG · USCG VIA DVIDS")
OFF20B = ("COAST GUARD OFFLOAD · SAN JUAN", "JULY 2020 · 1,375 KG · USCG VIA DVIDS")
OFFX = ("ILLUSTRATIVE · COAST GUARD OFFLOAD, SAN JUAN", "2020–2022 · NOT THE CASES DESCRIBED · USCG VIA DVIDS")

CARIB = dict(bounds=[[-76.5, 21.0], [-60.5, 9.6]], topPad=170,
             highlight={"630": "#5a1217", "214": "#2a2a30", "862": "#2a2a30", "170": "#2a2a30"},
             labels=[dict(ll=[-70.6, 19.1], t="DOMINICAN REP.", size=24), dict(ll=[-66.0, 8.2], t="VENEZUELA", size=30),
                     dict(ll=[-73.6, 7.8], t="COLOMBIA", size=30), dict(ll=[-70.5, 14.6], t="CARIBBEAN SEA", size=26)])
PRMAP = dict(bounds=[[-67.6, 18.75], [-65.0, 17.35]], topPad=170, highlight={"630": "#2a2a30"},
             labels=[dict(ll=[-66.45, 18.2], t="PUERTO RICO", size=34)])

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Three hundred ninety-one pounds of cocaine, and a boat that won't stop.",
  [C(1008245, 3.05), C(1008245, 47.0)], dict(tag=BHIR)),
 ("May twenty twenty-six, off Puerto Rico. Through an aircrew's infrared camera, the men on board start throwing packages into the sea.",
  [C(1008245, 8.0), C(1008245, 11.0), C(1008245, 13.85)], dict(tag=BHIR)),
 ("By the end of the night, the boat is stopped, three men are in custody, and the bales are back on a federal deck.",
  [C(1008245, 57.0), C(1008245, 60.0), C(1008245, 108.0)], dict(tag=BH)),
 ("This is a fight most Americans never see. A U.S. agency hunting smugglers across open water, at night. Why Puerto Rico? And how do you stop a boat that runs?",
  [C(1010409, 120), C(1010409, 300), C(954506, 0.5)], dict(tag=("CBP AIR AND MARINE OPERATIONS · AIRCREW SCREENS", "2025–2026 · ILLUSTRATIVE · CBP / USCG VIA DVIDS"))),
 ("This is the case file on the Caribbean front.",
  [G("title", case="014", title='BLACK HAWK <span class="red">vs. DRUG BOAT</span>', sub="THE CARIBBEAN FRONT · PUERTO RICO", size=150)], dict(gap=2.6)),

 # ---------------- I: NORTH OF SAN JUAN ----------------
 ("Start with the night it worked.",
  [G("chapter", case="014", n="I", t="NORTH OF SAN JUAN")], {}),
 ("On May thirteenth, twenty twenty-six, a crew from C B P's Air and Marine Operations spotted what the agency calls a target of interest, northwest of Puerto Rico.",
  [C(1010409, 190), C(1010409, 230), C(1010409, 380)], dict(tag=MEA)),
 ("A twenty-five-foot blue boat of the type called a yola. Three people on board. And packages, visible from the air.",
  [G("doc", header="CBP AIR AND MARINE OPERATIONS · MAY 13–14, 2026", title="TARGET OF INTEREST", tsize=110,
     body="25-ft blue yola-type vessel · northwest of Puerto Rico.<br>Three people on board · packages visible from the air.<br>Tracked overnight as it approached the island.<br>Intercepted north of San Juan on May 14.",
     source="SOURCES: CBP (DVIDS) · CBS12 · FOX NEWS", stamp="TRACKED")], {}),
 ("Aircrews and an operations center kept watch on it through the night, as it closed in on the island.",
  [C(1010409, 470), C(1010409, 310)], dict(tag=MEA)),
 ("The next day, May fourteenth, the San Juan Marine Unit launched two coastal interceptor boats, steered toward the yola by directions from the aircrew. A C B P Black Hawk helicopter joined the chase.",
  [C(795143, 60), C(795143, 96), C(976211, 126)], dict(tag=("ILLUSTRATIVE · CBP INTERCEPTOR & BLACK HAWK, SAN DIEGO", "2021 · 2025 · CBP VIA DVIDS"))),
 ("When the agents closed in, the boat tried to run. On board, the men started dumping their cargo over the side.",
  [C(1008245, 17.0), C(1008245, 19.45), C(1008245, 22.0)], dict(tag=("AGENTS CLOSE IN · MAY 14, 2026", "AGENTS' VIDEO · NORTH OF SAN JUAN · CBP VIA DVIDS"))),
 ("Then the helicopter crew did something you rarely hear about. They used what C B P calls air disabling fire, to stop the boat.",
  [C(1008245, 62.4), C(1008245, 52.0)], dict(tag=BH)),
 ("North of San Juan, the yola stopped. Agents pulled alongside and went aboard.",
  [C(1008245, 81.9), C(1008245, 84.0), C(1008245, 67.0)], dict(tag=BHB)),
 ("Agents recovered the bales, along with electronic devices. Five bales in all: about one hundred seventy-eight kilos, or three hundred ninety-one pounds of cocaine.",
  [C(1008245, 122.1), C(1008245, 118.0), C(1008245, 133.2)], dict(tag=BHB)),
 ("In a search of the boat, agents also found empty plastic containers and other packages they could not yet identify.",
  [C(1008245, 72.0), C(1008245, 88.0)], dict(tag=BHB)),
 ("Three men, all nationals of the Dominican Republic, were taken into custody, and handed to Homeland Security Task Force investigators with the drugs. Any charges are allegations; they are presumed innocent unless proven guilty.",
  [C(1008245, 141.7), C(859902, 3), C(859902, 21)], dict(tag=("THE YOLA AFTER THE STOP → ILLUSTRATIVE: A SAN JUAN HANDOVER", "MAY 14, 2026 · 2022 · CBP / USCG VIA DVIDS"))),
 ("The branch director, Christopher Hunter, credited the helicopter crew's decisive use of air disabling fire.",
  [G("quote", q="“Our Air and Marine Operations teams demonstrated exceptional skill and coordination in this interdiction.”", w="CHRISTOPHER HUNTER · DIRECTOR, CARIBBEAN AIR AND MARINE BRANCH, CBP · MAY 2026")], dict(gap=0.8)),

 # ---------------- II: THE BRIDGE ----------------
 ("C B P said the case reflects a wider Caribbean trafficking route that feeds drugs toward the United States, with South Florida as a major hub. That same week, authorities reported seizing about nine hundred pounds of cocaine in Miami, in a separate case.",
  [C(1010409, 240), C(1010409, 545), C(512126, 130), C(512126, 330)], dict(tag=("ILLUSTRATIVE · CBP AMO AIRCRAFT", "2017–2026 · CBP VIA DVIDS"))),
 ("Why here?",
  [G("chapter", case="014", n="II", t="THE BRIDGE")], {}),
 ("Look at the map. Puerto Rico sits far closer to Venezuela, Colombia and the Dominican Republic than to Florida.",
  [G("map", map=dict(CARIB, cities=[
       dict(ll=[-66.1, 18.45], name="SAN JUAN", sub="PUERTO RICO · U.S.", dy=-34, d=0.3, size=30, color="#D3212D"),
       dict(ll=[-69.9, 18.48], name="SANTO DOMINGO", anchor="end", dy=40, d=0.7, size=24),
       dict(ll=[-66.9, 10.5], name="CARACAS", dy=-30, d=1.1, size=24)],
       arcs=[dict(**{"from": [-66.9, 10.8]}, to=[-66.4, 17.8], d=1.3, dur=0.6, bend=0.12, color="#E8A33D"),
             dict(**{"from": [-69.6, 18.4]}, to=[-67.3, 18.2], d=1.6, dur=0.4, bend=-0.3, color="#E8A33D")]),
     kicker="THE EASTERN CARIBBEAN", title="A U.S. ISLAND IN THE MIDDLE")], {}),
 ("The Border Patrol's chief in Puerto Rico, Reggie Johnson, called the island a bridge to the United States.",
  [G("quote", q="“The Caribbean has always been a hot spot for cocaine.”", w="REGGIE JOHNSON · CHIEF PATROL AGENT, RAMEY SECTOR · TO THE DAILY SIGNAL, AUG. 2025")], dict(gap=0.6)),
 ("Most of the drugs, he said, arrive by boat. And once cocaine is on the island, flights on to the mainland are domestic flights.",
  [C(806610, 1), C(806610, 9), C(806610, 15)], dict(tag=OFF21)),
 ("Border Patrol's cocaine seizures in Puerto Rico and the Virgin Islands, as reported by The Daily Signal, tell the story: about five thousand three hundred pounds in twenty twenty-three, fifty-nine hundred in twenty twenty-four, and ninety-six hundred already in fiscal twenty twenty-five, with weeks still to go.",
  [G("cards3", kicker="COCAINE SEIZED · BORDER PATROL (PUERTO RICO & U.S. VIRGIN ISLANDS)", title="RISING",
     cards=[dict(h="5,300 LB", t="2023"), dict(h="5,900 LB", t="2024"), dict(h="9,600 LB", t="fiscal 2025", s="as of Aug. 2025")],
     footer="SOURCE: THE DAILY SIGNAL, AUG. 23, 2025, CITING BORDER PATROL")], {}),
 ("From the island, prosecutors say, the cocaine keeps moving north. In September twenty twenty-six, a federal grand jury in Puerto Rico indicted seventeen people, accused of sending cocaine through San Juan's international airport and the U.S. mail to the continental United States.",
  [G("doc", header="DEA CARIBBEAN DIVISION · SEPT. 22, 2026", title="17 INDICTED", tsize=130,
     body="Alleged route: Puerto Rico → Luis Muñoz Marín airport<br>and the U.S. mail → the continental United States.<br>Investigation led by HSI, with DEA and FBI.<br>An indictment is only an allegation.",
     source="SOURCE: DEA PRESS RELEASE, SEPT. 22, 2026", stamp="CHARGED")], {}),
 ("An indictment is only an allegation; all seventeen are presumed innocent. The D E A's special agent in charge for the Caribbean, Michael Mayer, put it plainly.",
  [G("quote", q="“Puerto Rico will not be used as a gateway for cocaine destined for communities across the United States.”", w="MICHAEL C. MAYER · DEA SPECIAL AGENT IN CHARGE, CARIBBEAN DIVISION · SEPT. 2026")], dict(gap=0.8)),
 ("Earlier that year, a postal inspection operation called Path to Zero had seized more than five hundred fifty-six kilos of cocaine, from more than four hundred forty-eight parcels bound for the mainland.",
  [G("stat", a="556+ KG", b="COCAINE SEIZED · 448+ PARCELS BOUND FOR THE MAINLAND", c="OPERATION PATH TO ZERO (USPIS-LED, FROM JAN. 2026) · SOURCE: DEA, MAY 21, 2026")], {}),

 # ---------------- III: EYES IN THE SKY ----------------
 ("So the fight starts offshore, before the boats reach the beach.",
  [G("chapter", case="014", n="III", t="EYES IN THE SKY")], {}),
 ("Air and Marine Operations is the part of Customs and Border Protection that flies and sails. Its long-range eyes are aircraft like these: Multi-Role Enforcement Aircraft, and the big P-3s with radar domes on their backs.",
  [C(403619, 6), C(403619, 18), C(403619, 120)], dict(tag=P3B)),
 ("Inside, crews work radar and camera stations for hours, scanning open ocean for a boat that doesn't belong.",
  [C(403632, 92), C(403632, 182), C(403632, 62)], dict(tag=P3I)),
 ("Off San Diego, in C B P's words, these crews patrol to identify suspicious vessels heading north from Mexican waters that may be involved in human trafficking or drug smuggling. The Caribbean crews hunt the same way.",
  [C(1010409, 30), C(1010409, 60), C(1010409, 100)], dict(tag=MEA)),
 ("In twenty twenty-one, C B P released what its P-3 crews see. This low profile vessel, designed to run very low in the water to avoid detection, was carrying about four thousand one hundred thirty-four pounds of cocaine.",
  [C(792912, 3), C(792912, 15), C(792912, 27)], dict(tag=P3L)),
 ("This one is a semi-submersible, tracked in the Caribbean. A partner agency boarded it and detained five suspects. On board: about sixteen thousand nine hundred thirty-eight pounds of cocaine, valued by C B P at two hundred twenty-one million dollars.",
  [C(792910, 18), C(792910, 24), C(792910, 42), C(792910, 49)], dict(tag=P3)),
 ("And this go-fast crew, in the western Caribbean, threw its load overboard while the P-3 watched. A partner agency recovered one hundred eleven bales of marijuana, about fifty-four hundred fifty pounds.",
  [C(792908, 0.5), C(792908, 6), C(792908, 51), C(792908, 60)], dict(tag=P3)),
 ("In these cases, the aircraft find and follow, and a boat makes the stop. In February twenty twenty-five, an A M O aircrew spotted a go-fast about fifty miles northeast of the Dominican Republic and guided the Coast Guard cutter Valiant to it.",
  [C(403628, 120), C(403628, 230), C(954506, 9.0), C(954506, 13.2)], dict(tag=("P-3 COCKPIT (ILLUSTRATIVE) → AMO AIRCREW VIDEO OF THE GO-FAST", "FEB. 2025 · NE OF THE DOMINICAN REP. · CBP / USCG VIA DVIDS"))),
 ("The Valiant's crew apprehended five suspected smugglers and seized about twelve hundred eighty pounds of cocaine.",
  [C(954506, 17.4), C(954506, 21.2)], dict(tag=VAL)),

 # ---------------- IV: TWENTY FUEL CANS ----------------
 ("The same handoff, in July twenty twenty-one: an A M O enforcement aircraft helped the cutter Joseph Tezanos stop a go-fast in the Mona Passage, between Puerto Rico and the Dominican Republic. Five hundred two kilos of cocaine, two suspected smugglers.",
  [C(1010406, 144), C(1010406, 252), C(806610, 4.0), C(806610, 18.5)], dict(tag=("ILLUSTRATIVE AMO AIRCRAFT (SAN DIEGO) → OFFLOAD, SAN JUAN", "JULY 2021 · 502 KG · CBP / USCG VIA DVIDS"))),
 ("About two weeks before the Black Hawk chase, the same system caught a bigger load.",
  [G("chapter", case="014", n="IV", t="TWENTY FUEL CANS")], {}),
 ("April twenty-eighth, twenty twenty-six, at ten fifty-two at night. An A M O Multi-Role Enforcement Aircraft spotted a thirty-foot yola about thirty-five nautical miles southeast of Puerto Rico.",
  [C(1010409, 250), C(1010409, 280), C(1010409, 460)], dict(tag=MEA)),
 ("A Black Hawk kept it under surveillance. Interceptor boats raced out from Pon-say and Fah-har-doh.",
  [C(976211, 144), C(795143, 102), C(795143, 114)], dict(tag=("ILLUSTRATIVE · CBP BLACK HAWK & INTERCEPTOR", "SAN DIEGO · 2025 · 2021 · CBP VIA DVIDS"))),
 ("According to the U.S. Attorney's Office, marine interdiction agents intercepted the yola after agents fired two warning rounds. The operator stopped. It was two minutes to one in the morning.",
  [C(987448, 15.5, pb=1), C(795143, 126), C(795143, 132)], dict(tag=("ILLUSTRATIVE · CBP MARINE UNITS · PUERTO RICO 2025, SAN DIEGO 2021", "NOT THE APRIL CASE · CBP VIA DVIDS"))),
 ("The boat carried twenty black fuel containers. Inside them, agents found bricks of cocaine: six hundred forty-three kilos, or one thousand four hundred eighteen pounds.",
  [G("cards3", kicker="SOUTHEAST OF PUERTO RICO · APRIL 29, 2026", title="ONE YOLA",
     cards=[dict(h="30 FT", t="yola · two outboards"), dict(h="20", t="black fuel containers"), dict(h="1,418 LB", t="cocaine bricks", s="643.3 kg")],
     footer="SOURCE: U.S. ATTORNEY'S OFFICE, DISTRICT OF PUERTO RICO, MAY 4, 2026")], {}),
 ("Three Venezuelan nationals were charged by criminal complaint with possessing cocaine with intent to distribute and importing it. A complaint is an accusation; they are presumed innocent unless proven guilty.",
  [G("doc", header="U.S. ATTORNEY'S OFFICE · DISTRICT OF PUERTO RICO", title="CRIMINAL COMPLAINT", tsize=110,
     body="Three Venezuelan nationals · charged.<br>Possession with intent to distribute cocaine.<br>Importation of cocaine.<br>Investigation: Homeland Security Task Force.",
     source="SOURCE: USAO-PR PRESS RELEASE 2026-039, MAY 4, 2026", stamp="CHARGED")], {}),
 ("What is disabling fire? In the Coast Guard's own helicopter playbook, the sequence is warning shots on command, then, if the boat keeps running, a marksman fires again to disable the engines.",
  [C(976211, 150), C(976211, 160), C(512126, 38)], dict(tag=("ILLUSTRATIVE · CBP BLACK HAWK & AMO AIRCREW VIDEO", "CBP VIA DVIDS"))),
 ("One Coast Guard captain called it the safest way to stop a boat moving at high speed on the open ocean.",
  [G("quote", q="“…the safest way to disable these vessels at high speed on the open ocean.”", w="CAPT. DAN BROADHURST · COMMANDING OFFICER, COAST GUARD HITRON · MYCG, MAY 2026")], dict(gap=0.6)),
 ("C B P's own marine agents use disabling fire too. In a video dated September twenty twenty-five, C B P showed its agents stopping a smuggling vessel off Puerto Rico this way; sixteen Dominican nationals on board were arrested.",
  [C(987448, 39.3, pb=1), C(987448, 51.2, pb=1), C(512126, 50)], dict(tag=("CBP MARINE UNIT · OFF PUERTO RICO, SEPT. 2025 → ILLUSTRATIVE AMO VIDEO", "CBP VIA DVIDS"))),

 # ---------------- V: BALES IN THE WATER ----------------
 ("When the boats can't run, the cargo goes over the side.",
  [G("chapter", case="014", n="V", t="BALES IN THE WATER")], {}),
 ("January twenty-eighth, twenty twenty-six, off Puerto Rico, near San Juan. The Coast Guard got a report: a trawler towing a barge, bundles going into the water, and a man jumping overboard.",
  [C(760607, 2), C(760607, 9), C(760607, 15)], dict(tag=OFFX)),
 ("C B P marine agents joined the search. By eight in the morning, authorities had pulled the man from the water. He was taken into custody.",
  [C(795143, 24), C(795143, 66), C(795143, 84)], dict(tag=CIV)),
 ("From the sea and the barge, agents recovered ten bales: seven hundred eighty-nine pounds of cocaine, worth more than five million dollars, by C B P's estimate.",
  [C(762246, 21), C(762246, 33), C(762246, 39)], dict(tag=OFFX)),
 ("Dumping the load is the oldest trick on the water. In July twenty twenty, a go-fast crew threw its cargo overboard in the Caribbean. Fifty-five bales were recovered: thirteen hundred seventy-five kilos.",
  [C(760607, 21), C(760607, 26), C(760607, 31)], dict(tag=OFF20B)),
 ("And in October twenty twenty-six, crews from C B P's Pon-say marine unit stopped another yola, south of the town of Gwy-a-nee-ya.",
  [C(795143, 36), C(795143, 108), C(795143, 120)], dict(tag=CIV)),
 ("Three Venezuelan nationals were on board, with one thousand three hundred nine pounds of cocaine. Estimated value: nine point four million dollars.",
  [G("stat", a="1,309 LB", b="COCAINE · ONE YOLA · SOUTH OF GUAYANILLA", c="OCT. 7 · 3 VENEZUELAN NATIONALS ON BOARD · EST. $9.4 MILLION · SOURCE: CBP STATEMENT AS PUBLISHED BY WORLD BORDER CONGRESS, OCT. 30, 2026")], {}),
 ("Four cases around one island, in one year. On the map, they surround it.",
  [G("map", map=dict(PRMAP, cities=[
       dict(ll=[-66.08, 18.62], name="789 LB", sub="JAN. 2026", dy=-30, d=0.3, size=30),
       dict(ll=[-66.25, 18.70], name="391 LB", sub="MAY 2026 · BLACK HAWK", anchor="end", dy=-30, d=0.7, size=30, color="#D3212D"),
       dict(ll=[-65.55, 17.72], name="1,418 LB", sub="APRIL 2026", dy=40, d=1.1, size=30),
       dict(ll=[-66.78, 17.80], name="1,309 LB", sub="OCT. 2026", anchor="end", dy=40, d=1.5, size=30)]),
     kicker="AIR AND MARINE OPERATIONS · 2026 CASES IN THIS FILE", title="AROUND ONE ISLAND", footer="LOCATIONS APPROXIMATE · SOURCES: CBP · USAO-PR")], {}),

 # ---------------- VI: THE DOCK AND THE COURTROOM ----------------
 ("Every chase ends at the same two places.",
  [G("chapter", case="014", n="VI", t="THE DOCK AND THE COURT")], {}),
 ("The first is a dock in San Juan. In October twenty twenty, the cutter Ary-bear-toe Er-nan-dez unloaded sixty-two bales of cocaine here, about nineteen hundred eighty-one kilos, from two go-fast interdictions. The Coast Guard valued the shipment at forty-eight million dollars.",
  [C(768299, 36), C(768299, 54), C(768299, 78), C(768299, 93)], dict(tag=OFF20)),
 ("In April twenty twenty-two, another cutter brought in about a thousand kilos, valued at twenty million dollars, after a go-fast was stopped near Puerto Rico. D E A agents took custody of two suspected smugglers.",
  [C(837729, 9), C(837729, 18), C(837729, 48)], dict(tag=OFF22)),
 ("These cases are built by many agencies at once: the Coast Guard, C B P, the D E A, Homeland Security Investigations, and federal prosecutors in San Juan, working through joint task forces.",
  [C(806610, 24), C(737847, 2), C(737847, 14)], dict(tag=("COAST GUARD & CBP AGENTS · SAN JUAN OFFLOADS", "2020–2021 · ILLUSTRATIVE · USCG VIA DVIDS"))),
 ("The U.S. attorney for Puerto Rico, Stephen Muldrow, said his office is committed to pursuing transnational drug traffickers, and bringing them before the courts.",
  [C(837729, 27), C(837729, 36)], dict(tag=OFF22)),
 ("The second place is a federal courtroom. Smuggling five kilos or more of cocaine can carry a mandatory minimum of ten years, and up to life.",
  [G("stat", a="10 YEARS", b="MANDATORY MINIMUM · 5 KG OR MORE OF COCAINE", c="UP TO LIFE IN FEDERAL PRISON · AS STATED BY DEA, SEPT. 2026 · ACTUAL SENTENCES VARY")], {}),
 ("Actual sentences vary. In May twenty twenty-six, a man who had pleaded guilty to a cocaine case aboard a vessel was re-sentenced in Puerto Rico to ninety-six months. In August, a man who admitted conspiring to import about one hundred fifty kilos got one hundred twenty months.",
  [G("doc", header="U.S. ATTORNEY'S OFFICE · DISTRICT OF PUERTO RICO", title="SENTENCED", tsize=120,
     body="May 27, 2026 · 5+ kg of cocaine aboard a vessel<br>→ 96 months (guilty plea, re-sentenced).<br>Aug. 6, 2026 · conspiracy to import ~150 kg<br>→ 120 months (guilty plea).",
     source="SOURCES: USAO-PR HSTF CASE ROUNDUPS, JUNE & AUG. 2026", stamp="CONVICTED")], {}),

 # ---------------- CLOSE ----------------
 ("Back to the night north of San Juan.",
  [C(1008245, 76.2)], dict(tag=("AGENTS' VIDEO · MAY 14, 2026", "NORTH OF SAN JUAN · CBP VIA DVIDS"))),
 ("Three hundred ninety-one pounds, stopped by a helicopter. Fourteen hundred eighteen pounds in twenty fuel cans. Thirteen hundred nine off Gwy-a-nee-ya. Seven hundred eighty-nine pounds pulled from the sea and a barge.",
  [C(1008245, 93.0), C(512126, 46), C(859902, 30), C(762246, 27)], dict(tag=("THE 2026 CASES", "FOOTAGE: MAY 14 CASE + ILLUSTRATIVE (2017–2022) · CBP / USCG VIA DVIDS"))),
 ("About thirty-nine hundred pounds of cocaine, from just four cases in this file involving Air and Marine Operations, around one island, in one year.",
  [C(768299, 0.5), C(768299, 85)], dict(tag=OFFX)),
 ("After the October seizure, the branch director said Air and Marine Operations remains committed to protecting Puerto Rico's maritime borders. Those are the boats that got caught. Nobody can count the ones that didn't.",
  [C(1010409, 330), C(1010409, 600), C(1010409, 620)], dict(tag=MEA)),
 ("Case file zero one four. Closed for now.",
  [G("end", case="014", label="BLACK HAWK vs. DRUG BOAT")], dict(gap=3.0)),
]

DISPLAY = [
 ("twenty twenty-six", "2026"), ("twenty twenty-five", "2025"), ("twenty twenty-three", "2023"), ("twenty twenty-two", "2022"),
 ("twenty twenty-one", "2021"), ("twenty twenty", "2020"),
 ("Three hundred ninety-one pounds", "391 pounds"), ("three hundred ninety-one pounds", "391 pounds"),
 ("one hundred seventy-eight kilos", "178 kilos"), ("twenty-five-foot", "25-foot"), ("thirty-foot", "30-foot"),
 ("May thirteenth", "May 13"), ("May fourteenth", "May 14"), ("April twenty-eighth", "April 28"), ("January twenty-eighth", "January 28"),
 ("about five thousand three hundred pounds", "about 5,300 pounds"), ("fifty-nine hundred", "5,900"), ("ninety-six hundred", "9,600"),
 ("seventeen", "17"), ("five hundred fifty-six kilos", "556 kilos"), ("four hundred forty-eight parcels", "448 parcels"),
 ("four thousand one hundred thirty-four pounds", "4,134 pounds"), ("sixteen thousand nine hundred thirty-eight pounds", "16,938 pounds"),
 ("two hundred twenty-one million dollars", "$221 million"), ("one hundred eleven bales", "111 bales"), ("fifty-four hundred fifty pounds", "5,450 pounds"),
 ("fifty miles", "50 miles"), ("Five hundred two kilos", "502 kilos"), ("nine hundred pounds", "900 pounds"), ("twelve hundred eighty pounds", "1,280 pounds"),
 ("ten fifty-two", "10:52"), ("thirty-five nautical miles", "35 nautical miles"), ("two warning rounds", "two warning rounds"),
 ("twenty black fuel containers", "20 black fuel containers"), ("six hundred forty-three kilos", "643 kilos"),
 ("one thousand four hundred eighteen pounds", "1,418 pounds"), ("sixteen Dominican", "16 Dominican"),
 ("seven hundred eighty-nine pounds", "789 pounds"), ("Seven hundred eighty-nine pounds", "789 pounds"), ("five million dollars", "$5 million"),
 ("fifty-five bales", "55 bales"), ("thirteen hundred seventy-five kilos", "1,375 kilos"),
 ("one thousand three hundred nine pounds", "1,309 pounds"), ("nine point four million dollars", "$9.4 million"),
 ("sixty-two bales", "62 bales"), ("nineteen hundred eighty-one kilos", "1,981 kilos"), ("forty-eight million dollars", "$48 million"),
 ("a thousand kilos", "1,000 kilos"), ("twenty million dollars", "$20 million"),
 ("five kilos", "5 kilos"), ("ten years", "10 years"), ("ninety-six months", "96 months"), ("one hundred fifty kilos", "150 kilos"), ("one hundred twenty months", "120 months"),
 ("Fourteen hundred eighteen pounds", "1,418 pounds"), ("twenty fuel cans", "20 fuel cans"), ("Thirteen hundred nine", "1,309"),
 ("About thirty-nine hundred pounds", "About 3,900 pounds"),
 ("Gwy-a-nee-ya", "Guayanilla"),
 ("zero one four", "014"), ("C B P", "CBP"), ("D E A", "DEA"), ("A M O", "AMO"),
]

META = dict(
    case="014", label="BLACK HAWK vs. DRUG BOAT",
    title="How a Black Hawk Stopped a Cocaine Boat Off Puerto Rico",
    imgs={},
    mute_nat=[1008245, 987448],  # interdiction videos: keep their audio out of the mix (possible gunfire)
    credit=("Footage: U.S. Customs and Border Protection and U.S. Coast Guard via DVIDS — public domain."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."),
    shorts=[
        dict(id="s1", lines=[1, 3], hook="391 LB OF COCAINE<br>[BLACK HAWK STOPS THE BOAT]", title="Black Hawk Stops a Boat Carrying 391 Pounds of Cocaine", template="single action moment (IR chase → jettison → boats surround)"),
        dict(id="s2", lines=[55, 56], hook="62 BALES · 1,981 KG<br>[UNLOADED IN SAN JUAN]", title="62 Bales of Cocaine Unloaded on One Dock: $48 Million", template="before→after seizure reveal"),
        dict(id="s3", lines=[12, 14], hook="“AIR DISABLING FIRE”<br>[391 LB OF COCAINE]", title="391 Pounds of Cocaine Stopped by 'Air Disabling Fire'", template="verbatim quote"),
        dict(id="s4", lines=[62, 63], hook="4 BOATS · 1 ISLAND<br>[3,900 LB OF COCAINE]", title="4 Boats, 3,900 Pounds of Cocaine Around One Island", template="countdown / ranking"),
        dict(id="s5", lines=[32, 33], hook="16,938 LB OF COCAINE<br>[ONE SEMI-SUB]", title="16,938 Pounds of Cocaine on a Semi-Sub, Spotted From the Air", template="single action moment (P-3 tracking → jettison)"),
    ],
)
