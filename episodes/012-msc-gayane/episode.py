# CASE FILE 012 — 20 Tons of Cocaine Hidden on One Cargo Ship: The $1.3 Billion Bust
# Each entry: (vo_text, shots, opts)  — same format as episodes/001-ms13/episode.py
# shot: ("clip_id", start_sec, {opts}) | ("g:<graphic_name>", 0, {opts})
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

PHL = ("CBP · PORT OF PHILADELPHIA · MSC GAYANE SEIZURE", "JUNE 2019 · SOURCE: CBP VIA DVIDS")
PHL_N = ("CBP · PORT OF PHILADELPHIA · JUNE 2019", "39,525 LB OF COCAINE · ~$1.3 BILLION · SOURCE: CBP")
PRESS = ("CBP PRESS CONFERENCE · U.S. CUSTOM HOUSE, PHILADELPHIA", "JUNE 21, 2019 · ABOUT A QUARTER OF THE SEIZURE ON DISPLAY")
PANGA = ("ILLUSTRATIVE · COAST GUARD PURSUES A SMUGGLING BOAT", "EASTERN PACIFIC · 2019 · NOT THE MSC GAYANE CASE")
PANGA2 = ("ILLUSTRATIVE · SMUGGLING BOATS AT SEA", "EASTERN PACIFIC · 2025 · NOT THE MSC GAYANE CASE")
HOU = ("ILLUSTRATIVE · CONTAINER INSPECTIONS, PORT OF HOUSTON", "2025 · NOT THE MSC GAYANE CASE")
BAL = ("ILLUSTRATIVE · CONTAINER INSPECTIONS, PORT OF BALTIMORE", "2026 · NOT THE MSC GAYANE CASE")
SAV = ("ILLUSTRATIVE · CBP CARGO OPERATIONS, PORT OF SAVANNAH", "NOT THE MSC GAYANE CASE")
SAV_NII = ("ILLUSTRATIVE · CBP X-RAY SCAN OF CONTAINERS, SAVANNAH", "2023 · NOT THE MSC GAYANE CASE")

# route map: Europe -> Panama -> Peru -> Chile -> Panama -> Bahamas -> Philadelphia
ROUTE = dict(bounds=[[-95, 56], [12, -38]], topPad=170, highlight={604: "#5a1217", 152: "#2a2a30", 591: "#2a2a30"})

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Nearly twenty tons of cocaine. One cargo ship.",
  [C(691452, 5.5), C(691452, 11)], dict(tag=PHL_N)),
 ("June seventeenth, twenty nineteen. Federal officers climb aboard a container ship at the Packer Marine Terminal in Philadelphia.",
  [C(691452, 104.5), C(691452, 110), C(691452, 115.5)], dict(tag=PHL)),
 ("Inside seven of its containers, they find bricks. Thousands of them. The final count: thirty-nine thousand five hundred twenty-five pounds. Customs puts the street value at about one point three billion dollars.",
  [C(691452, 16.5), C(691452, 22), C(691452, 27.5), C(691452, 33)], dict(tag=PHL_N)),
 ("Customs calls it the largest cocaine seizure in its two hundred thirty year history.",
  [C(692217, 20), C(692217, 147.5)], dict(tag=PRESS)),
 ("And it didn't come aboard in a port. According to prosecutors, it was lifted aboard at sea, at night, by the ship's own crane. So who loaded it? And how did twenty tons ride thousands of miles without anyone stopping it?",
  [C(669728, 36), C(669728, 42), C(955021, 18), C(955021, 24)], dict(tag=PANGA)),
 ("This is the case of the M S C Gah-yah-nay.",
  [G("title", case="012", title='20 TONS <span class="red">ONE SHIP</span>', sub="THE MSC GAYANE COCAINE CASE", size=170)], dict(gap=2.6)),

 # ---------------- I: THE SHIP ----------------
 ("Start with the ship.",
  [G("chapter", case="012", n="I", t="THE SHIP")], {}),
 ("The M S C Gah-yah-nay is a container ship, one thousand thirty feet long, sailing under the flag of Liberia. It was built in twenty eighteen, and operated by the Swiss-based Mediterranean Shipping Company, M S C.",
  [C(691452, 66), C(691452, 71.5), C(691452, 77)], dict(tag=("MSC GAYANE AT PACKER MARINE TERMINAL", "PHILADELPHIA · JUNE 2019 · CBP VIA DVIDS"))),
 ("Ships like this carry thousands of steel boxes. Each container is closed with a numbered seal. If the seal is intact, the box hasn't been opened. That small piece of metal is the whole system of trust.",
  [C(1025719, 9), C(1025719, 171), C(1025719, 180)], dict(tag=HOU)),
 ("In the spring of twenty nineteen, the Gah-yah-nay leaves Europe on April twenty-seventh. It crosses the Atlantic, goes through the Panama Canal, and turns south, down the Pacific coast of South America.",
  [G("map", map=dict(ROUTE, arcs=[dict(**{"from": [4.4, 51.2]}, to=[-79.6, 9.2], d=0.3, dur=0.8, bend=0.18, color="#ECE7DC"),
                                  dict(**{"from": [-79.6, 9.2]}, to=[-77.2, -12.0], d=1.1, dur=0.4, bend=0.2, color="#ECE7DC"),
                                  dict(**{"from": [-77.2, -12.0]}, to=[-71.6, -33.0], d=1.5, dur=0.4, bend=0.2, color="#ECE7DC")],
     cities=[dict(ll=[4.4, 51.2], name="EUROPE · APRIL 27", anchor="end", dy=-30, d=0.2, size=30),
             dict(ll=[-79.6, 9.2], name="PANAMA CANAL", anchor="end", d=1.1, size=30),
             dict(ll=[-77.2, -12.0], name="PERU", anchor="end", d=1.5, size=30),
             dict(ll=[-71.6, -33.0], name="CHILE", anchor="end", d=1.9, size=30)],
     labels=[dict(ll=[-38, 30], t="ATLANTIC OCEAN", size=30), dict(ll=[-92, -20], t="PACIFIC", size=30)]),
     kicker="SOURCE: FREIGHTWAVES, FROM COURT FILINGS · ROUTE ILLUSTRATIVE", title="SOUTHBOUND · 2019")], {}),
 ("After Chile, it turns north again: back through the canal, a stop in the Bahamas, and then Philadelphia. The next stop on the schedule is Rotterdam.",
  [G("map", map=dict(ROUTE, arcs=[dict(**{"from": [-71.6, -33.0]}, to=[-79.6, 9.2], d=0.3, dur=0.6, bend=-0.2, color="#D3212D"),
                                  dict(**{"from": [-79.6, 9.2]}, to=[-78.7, 26.5], d=0.9, dur=0.4, bend=0.2, color="#D3212D"),
                                  dict(**{"from": [-78.7, 26.5]}, to=[-75.15, 39.9], d=1.3, dur=0.4, bend=0.2, color="#D3212D")],
     cities=[dict(ll=[-71.6, -33.0], name="CHILE", anchor="end", d=0.2, size=30),
             dict(ll=[-79.6, 9.2], name="PANAMA CANAL", anchor="end", d=0.9, size=30),
             dict(ll=[-78.7, 26.5], name="BAHAMAS", anchor="end", d=1.3, size=30),
             dict(ll=[-75.15, 39.9], name="PHILADELPHIA", sub="JUNE 16–17, 2019", d=1.7, size=34, color="#D3212D"),
             dict(ll=[4.4, 51.9], name="ROTTERDAM", sub="NEXT STOP", anchor="end", dy=-30, d=2.0, size=28)],
     labels=[dict(ll=[-30, 18], t="ATLANTIC OCEAN", size=30), dict(ll=[-92, -20], t="PACIFIC", size=30)]),
     kicker="SOURCES: FREIGHTWAVES · 6ABC · ROUTE ILLUSTRATIVE", title="NORTHBOUND · 2019")], {}),
 ("On paper, an ordinary voyage. But somewhere off South America, the ship had company.",
  [C(891556, 202.5), C(891556, 249)], dict(tag=SAV)),

 # ---------------- II: THE NIGHT DROPS ----------------
 ("The pickups.",
  [G("chapter", case="012", n="II", t="THE NIGHT DROPS")], {}),
 ("According to court records, speedboats came out to meet the Gah-yah-nay at night, more than once, while it was at sea.",
  [C(669728, 18), C(669728, 24), C(669728, 30)], dict(tag=PANGA)),
 ("A federal agent's affidavit says two crew members admitted loading cocaine from fourteen boats at sea.",
  [C(955021, 3), C(955021, 9), C(955021, 14)], dict(tag=PANGA2)),
 ("The method was simple. The speedboats brought duffel bags of bricks in cargo nets. On the ship, a crane at the stern, normally used to lift supplies aboard, hoisted the nets up onto the deck.",
  [C(669728, 51), C(669728, 56.5), C(669728, 75)], dict(tag=PANGA)),
 ("Then the crew went to work. They hid the bags inside shipping containers, among the legitimate cargo. To fit it all in, prosecutors say, they bent railings and pulled back container doors.",
  [C(1010029, 46.2), C(1010029, 88.2), C(1010029, 134.4)], dict(tag=BAL)),
 ("And then the trick that was supposed to make it invisible. Every container they opened got a new seal. A fake one, from a cache of counterfeit seals the gang kept.",
  [C(1025719, 72), C(1025719, 90), C(1025719, 198.5)], dict(tag=HOU)),
 ("Investigators described one more move. On the way south, the first load went into a single container bound for Chile. That way, it would not be checked in Peru, where only the boxes coming off the ship got inspected.",
  [G("timeline", kicker="AS DESCRIBED BY INVESTIGATORS · VIA FREIGHTWAVES", title="A MOVING HIDING PLACE",
     events=[dict(y="1", t="Into a container bound for Chile"), dict(y="2", t="Past Peru · into the ship's ventilation"), dict(y="3", t="Past Chile · into boxes bound for Europe")],
     footer="SOURCE: FREIGHTWAVES, FROM UNSEALED INVESTIGATION REPORT")], {}),
 ("After Peru, the drugs were moved into the ship's ventilation system. After Chile, into containers headed for Europe. More was loaded by crane on the run north, before the canal.",
  [C(691452, 137.5), C(691452, 143), C(691452, 126.5)], dict(tag=PHL)),
 ("The cocaine was never meant for Philadelphia. Investigators say it was bound for Europe.",
  [C(891556, 7.5), C(891556, 60), C(891556, 67.5)], dict(tag=SAV)),

 # ---------------- III: THE CREW ----------------
 ("So who did the lifting?",
  [G("chapter", case="012", n="III", t="THE CREW")], {}),
 ("The Gah-yah-nay had twenty-two crew members. Prosecutors would show that at least eight of them were in on it.",
  [G("stat", a="8 OF 22", b="CREW MEMBERS CONVICTED", c="SOURCES: U.S. ATTORNEY, E.D. PA. · FREIGHTWAVES")], {}),
 ("Four were recruited before they ever boarded, by a criminal organization in Montenegro. One of them, the electrician, later said he'd been approached outside a café, by people who already knew about his upcoming voyage. He joined the ship in Antwerp, Belgium, in late April.",
  [C(691452, 148.5), C(691452, 164.8), C(691452, 171)], dict(tag=("CBP OFFICERS ABOARD THE MSC GAYANE", "PHILADELPHIA · JUNE 2019 · CREW NOT SHOWN"))),
 ("The chief officer, Bosh-ko Mar-ko-vitch, a seaman with nineteen years at sea, managed the cargo plan. He knew which container would come off at which port.",
  [G("cards3", kicker="MSC GAYANE · THE RECRUITED CREW", title="WHO DID WHAT",
     cards=[dict(h="CHIEF OFFICER", t="Bosko Markovic", s="Ran the cargo plan"), dict(h="SECOND OFFICER", t="Ivan Durasevic", s="Recruited crew at sea"), dict(h="ENGINEER CADET", t="Nenad Ilic", s="Operated the crane")],
     footer="SOURCES: U.S. ATTORNEY, E.D. PA. · FREIGHTWAVES")], {}),
 ("The engineer cadet, Nenad Ee-litch, ran the crane. And the electrician, Aleksandar Kah-vah-yah, passed information to the organizers on land, over so-called narco phones, about which containers were going where.",
  [C(1010029, 105), C(1010029, 113.4), C(1010029, 126)], dict(tag=BAL)),
 ("After the ship left Europe, four more were brought in. A fourth engineer. An assistant reefer man. And two seamen from Samoa, who helped unload the bags and hide them in the cargo.",
  [C(1025719, 117), C(1025719, 135), C(1025719, 144)], dict(tag=HOU)),
 ("One of those seamen told agents the second officer had recruited him, and that he was paid about fifty thousand euros to help load cocaine on an earlier voyage. In his cabin, agents found a stack of fifty-euro notes, hidden in a carton of cigarettes.",
  [G("doc", header="HSI AFFIDAVIT · AS REPORTED BY FREIGHTWAVES", title="THE CIGARETTE CARTON", tsize=96,
     body="A crew member told agents he was paid about €50,000 to help load cocaine on an earlier voyage.<br>Agents found 50-euro notes hidden in a carton of cigarettes in his cabin — partial payment, he said.",
     source="SOURCE: FREIGHTWAVES, SEPT. 2, 2021", stamp="EVIDENCE")], {}),
 ("An earlier voyage. Which means the June run may not have been the first.",
  [C(825710, 24), C(825710, 36)], dict(tag=SAV)),

 ("An investigator's affidavit places that earlier trip in the winter. That seaman had boarded in Antwerp on December fifth, twenty eighteen. The second officer joined in Balboa, Panama, on January fourth, twenty nineteen. The engineer cadet and the other Samoan seaman were aboard too.",
  [C(825710, 12), C(825710, 360), C(825710, 372)], dict(tag=SAV)),
 # ---------------- IV: PHILADELPHIA ----------------
 ("And then, the Delaware River.",
  [G("chapter", case="012", n="IV", t="PHILADELPHIA")], {}),
 ("When the Gah-yah-nay comes up the Delaware in June twenty nineteen, a crowd is waiting: Homeland Security Investigations, Customs and Border Protection, the Coast Guard, state police from Pennsylvania and Delaware, and Philadelphia police.",
  [C(691452, 182.2), C(691452, 187.7), C(691452, 99)], dict(tag=PHL)),
 ("Court records don't say whether someone tipped them off. But one crew member, the engineer cadet, later admitted that when he saw law enforcement coming in Delaware Bay, he threw his narco phone overboard.",
  [C(891556, 82.5), C(891556, 135), C(891556, 172.5)], dict(tag=SAV)),
 ("On the night of June sixteenth, officers spot something wrong in seven containers. The next day they confirm it, with fiber optic scopes, drug-sniffing dogs, and an X-ray truck.",
  [C(891551, 150), C(891551, 157.5), C(891551, 225)], dict(tag=SAV_NII)),
 ("Seven containers. Inside each one, between one thousand two hundred and three thousand bricks. Early counts put the total at about fifteen thousand.",
  [C(691452, 154.6), C(691452, 159.7)], dict(tag=PHL)),
 ("Then comes the counting. Officers pack the bricks into evidence boxes, and weigh them on a scale.",
  [C(691452, 38.5), C(691452, 49.5)], dict(tag=PHL)),
 ("The first estimate is about sixteen and a half tons. The number keeps growing. By June twenty-sixth, the final count is in: thirty-nine thousand five hundred twenty-five pounds.",
  [C(692217, 62.5), C(692217, 71)], dict(tag=("CBP PRESS CONFERENCE · PHILADELPHIA · JUNE 21, 2019", "FINAL COUNT: 39,525 LB · FIRST ESTIMATE ~16.5 TONS · SOURCE: CBP"))),
 ("At a news conference on June twenty-first, officials stand behind a table of bricks. It's only about a quarter of the load.",
  [C(692217, 3), C(692217, 37), C(692217, 54)], dict(tag=PRESS)),
 ("Within days, a federal complaint had charged the second officer and another crewman with conspiracy. Both, investigators said, confessed. By June twenty-first, six crew members were charged.",
  [C(692217, 122), C(692217, 139), C(692217, 156)], dict(tag=PRESS)),
 ("Casey Durst, Customs' director of field operations in Baltimore, gave the room a picture of the scale. Laid end to end, she said, the bricks would cover about two and a half miles.",
  [C(692217, 88), C(692217, 96.5), C(692217, 105)], dict(tag=("CBP PRESS CONFERENCE · PHILADELPHIA", "JUNE 21, 2019 · “ABOUT 2.5 MILES” END TO END"))),

 # ---------------- V: THE SHIP ON TRIAL ----------------
 ("Then the government went after the ship itself.",
  [G("chapter", case="012", n="V", t="SEIZING THE SHIP")], {}),
 ("On July fourth, twenty nineteen, Customs executes a federal seizure warrant, and takes the Gah-yah-nay. Durst calls it the largest vessel seized in the agency's two hundred thirty year history. Seizing a ship this size, she said, is an unusual enforcement action.",
  [C(691452, 82.5), C(691452, 88.7), G("doc", header="U.S. DISTRICT COURT · E.D. PENNSYLVANIA", title="SEIZURE WARRANT", tsize=110, body="July 4, 2019: CBP seizes the MSC Gayane under its Title 19 seizure and forfeiture authority.<br>“Largest vessel seized in U.S. Customs and Border Protection's 230-year history.” — Casey Durst, CBP", source="SOURCE: CBP, JULY 8, 2019", stamp="SEIZED")], dict(tag=("MSC GAYANE · PORT OF PHILADELPHIA", "JUNE 2019 · CBP VIA DVIDS"))),
 ("In the statement announcing the seizure, the U S Attorney in Philadelphia, William McSwain, put the whole case in one line.",
  [C(891556, 105), C(891556, 112.5)], dict(tag=SAV)),
 ("We found nearly twenty tons of cocaine hidden on this ship.",
  [G("quote", q="“We found nearly 20 tons of cocaine hidden on this ship.”", w="WILLIAM McSWAIN · U.S. ATTORNEY, E.D. PENNSYLVANIA · JULY 2019")], dict(gap=0.8)),
 ("It doesn't stay seized for long. The ship's owner and operator put up ten million dollars in cash and a forty million dollar surety bond. Fifty million dollars in all. By mid-July, the Gah-yah-nay is back at sea, heading for Rotterdam.",
  [G("cards3", kicker="JULY 2019", title="THE PRICE OF THE SHIP",
     cards=[dict(h="$10M", t="cash"), dict(h="$40M", t="surety bond"), dict(h="$50M", t="to release the ship", s="per U.S. Attorney McSwain")],
     footer="SOURCES: CBP · GCAPTAIN, JULY 16, 2019")], {}),
 ("Prosecutors have not accused M S C of any wrongdoing, and the company was not charged. It said that shipping firms are, quote, from time to time affected by trafficking problems, and that it took the case very seriously.",
  [C(825710, 228), C(825710, 264), C(825710, 288)], dict(tag=SAV)),
 ("But the Gah-yah-nay wasn't the only problem that year. In March, at the same port, officers had pulled about one thousand two hundred pounds of cocaine from containers on another M S C ship, the Desiree.",
  [G("timeline", kicker="2019 · COCAINE IN SHIPPING CONTAINERS", title="ONE YEAR",
     events=[dict(y="EARLY 2019", t="New Jersey · ~3,200 lb"), dict(y="MARCH 2019", t="MSC Desiree, Philadelphia · ~1,200 lb"), dict(y="MAY 2019", t="Philadelphia · ~450 kg"), dict(y="JUNE 2019", t="MSC Gayane · 39,525 lb")],
     footer="SOURCES: NPR · MARITIME EXECUTIVE · 6ABC")], {}),
 ("In New Jersey, early that year, three thousand two hundred pounds had turned up in a container that held mostly dried fruit. And in May, separately, about four hundred fifty kilos were seized at the same port.",
  [C(825710, 240), C(825710, 252), C(825710, 276)], dict(tag=SAV)),
 ("Customs suspended the line's status in its trusted-shipper program, C T PAT, after the two Philadelphia cases.",
  [C(891551, 165), C(891551, 172.5), C(891551, 180)], dict(tag=SAV_NII)),

 # ---------------- VI: THE SENTENCES ----------------
 ("And the crew?",
  [G("chapter", case="012", n="VI", t="THE SENTENCES")], {}),
 ("All eight pleaded guilty to conspiracy to possess cocaine with intent to distribute, aboard a vessel subject to U S jurisdiction. In federal court in Philadelphia, the sentences came down one by one. The last, at the end of August twenty twenty-one.",
  [C(691452, 42), C(691452, 53), C(691452, 58.8)], dict(tag=("CBP · EVIDENCE PROCESSING", "PHILADELPHIA · JUNE 2019"))),
 ("The chief officer and the engineer cadet: seven years each. The second officer: six and a half years. The electrician: seven years and four months. The fourth engineer: five years and ten months. The reefer man and the two Samoan seamen: five years each.",
  [G("list", kicker="U.S. DISTRICT COURT · E.D. PENNSYLVANIA", title="EIGHT SENTENCES",
     items=["Markovic · Ilic — 7 years each", "Kavaja — 7 years 4 months", "Durasevic — 6 years 6 months", "Penda — 5 years 10 months", "Bojevic · Tiasaga · Pulu — 5 years each"],
     footer="SOURCES: U.S. ATTORNEY, E.D. PA. · FREIGHTWAVES")], {}),
 ("The captain was not charged. Prosecutors said there was insufficient evidence to charge him, or any other crew members.",
  [C(891556, 217.5), C(891556, 225)], dict(tag=SAV)),
 ("Back in July twenty nineteen, Homeland Security Investigations had set its goal. Its special agent in charge in Philadelphia, Marlon Miller, said it wanted to bring to justice, quote, those who had roles in this drug smuggling venture.",
  [C(1010029, 25.2), C(1010029, 4.2), G("quote", q="“…bring to justice those who had roles in this drug smuggling venture.”", w="MARLON MILLER · HSI PHILADELPHIA SPECIAL AGENT IN CHARGE · JULY 2019")], dict(gap=0.8, tag=BAL)),
 ("When the second officer and the engineer cadet were sentenced, in August twenty twenty-one, the acting U S Attorney, Jennifer Arbittier Williams, said this.",
  [C(825710, 384), C(825710, 396)], dict(tag=SAV)),
 ("Drug smuggling operations will be uncovered one way or another.",
  [G("quote", q="“…drug smuggling operations will be uncovered one way or another.”", w="JENNIFER ARBITTIER WILLIAMS · ACTING U.S. ATTORNEY · 2021")], dict(gap=0.8)),

 ("The crew was only one end of it. In October twenty twenty-two, federal prosecutors in Brooklyn charged a man from Montenegro: Goran Go-gitch, a former heavyweight boxer. They allege he helped move cocaine on three M S C ships between twenty eighteen and twenty nineteen, the Gah-yah-nay among them. He has pleaded not guilty, and is presumed innocent.",
  [G("doc", header="U.S. DISTRICT COURT · E.D. NEW YORK · INDICTMENT UNSEALED OCT. 2022", title="UNITED STATES v. GORAN GOGIC", tsize=88,
     body="Alleged: conspiracy, May 2018 – July 2019, to move cocaine in containers on MSC ships — Carlotta, Desiree, Gayane.<br>Pleaded not guilty. Charges are allegations; he is presumed innocent.",
     source="SOURCES: GCAPTAIN, OCT. 31, 2022 · A&E, SEPT. 2026", stamp="PENDING"),
   G("cards3", kicker="AS ALLEGED IN THE BROOKLYN INDICTMENT", title="THREE MSC SHIPS",
     cards=[dict(h="CARLOTTA", t="~1,437 kg", s="New York / New Jersey · Feb. 27, 2019"), dict(h="DESIREE", t="~537 kg", s="Philadelphia · March 18, 2019"), dict(h="GAYANE", t="~17,956 kg", s="Philadelphia · June 2019")],
     footer="SOURCE: GCAPTAIN, OCT. 31, 2022 · ALLEGATIONS, NOT PROVEN")], {}),
 ("His trial was set to begin in November twenty twenty-five. It never reached opening statements. The whole jury was dismissed after a plot to bribe a juror. Three men have since pleaded guilty to obstruction of justice in that plot. As of September twenty twenty-six, no new trial date had been reported.",
  [G("timeline", kicker="UNITED STATES v. GOGIC · BROOKLYN", title="A TRIAL THAT HASN'T HAPPENED",
     events=[dict(y="OCT 2022", t="Arrested in Miami · indicted"), dict(y="NOV 2025", t="Jury dismissed · juror-bribery plot"), dict(y="2026", t="3 men plead guilty"), dict(y="SEPT 2026", t="No new trial date reported")],
     footer="SOURCES: GCAPTAIN · A&E (AETV.COM), UPDATED SEPT. 2, 2026")], {}),
 ("Look at what actually broke in this case. Not a border. Not a scanner. A container seal is a promise that nobody opened the box. On the Gah-yah-nay, the people who broke that promise were the crew. And the only reason we know is that in Philadelphia, someone checked.",
  [C(1010029, 58.8), C(1010029, 75.6), C(1025719, 207)], dict(tag=BAL)),
 # ---------------- CLOSE ----------------
 ("So here's what the record shows. Fourteen boats at sea. One crane. Seven containers with suspicious seals. Thirty-nine thousand five hundred twenty-five pounds of cocaine. Eight sailors sentenced to federal prison. And one question the crew's case never answered: had it worked before Philadelphia, and how often?",
  [C(669728, 84), C(955021, 48), C(1025719, 189), C(691452, 120), C(692217, 11.5)], dict(tag=("COLD WARRANT · CASE FILE 012", "FOOTAGE: CBP · U.S. COAST GUARD VIA DVIDS"))),
 ("Case file zero one two. The crew's case is closed. The alleged organizer's case is still open.",
  [G("end", case="012", label="20 TONS · ONE SHIP")], dict(gap=4.0)),
]

# spoken -> display replacements for subtitles (longest first where they overlap)
DISPLAY = [
 ("thirty-nine thousand five hundred twenty-five pounds", "39,525 pounds"), ("Thirty-nine thousand five hundred twenty-five pounds", "39,525 pounds"),
 ("one point three billion dollars", "$1.3 billion"), ("two hundred thirty year", "230-year"),
 ("one thousand thirty feet", "1,030 feet"), ("between one thousand two hundred and three thousand", "between 1,200 and 3,000"),
 ("about one thousand two hundred pounds", "about 1,200 pounds"), ("three thousand two hundred pounds", "3,200 pounds"),
 ("about fifty thousand euros", "about €50,000"), ("fifty-euro notes", "50-euro notes"), ("about fifteen thousand", "about 15,000"), ("about four hundred fifty kilos", "about 450 kilos"), ("December fifth", "December 5"), ("January fourth", "January 4"),
 ("ten million dollars", "$10 million"), ("forty million dollar", "$40 million"), ("Fifty million dollars", "$50 million"),
 ("sixteen and a half tons", "16.5 tons"), ("two and a half miles", "2.5 miles"),
 ("Nearly twenty tons", "Nearly 20 tons"), ("nearly twenty tons", "nearly 20 tons"), ("twenty tons", "20 tons"),
 ("twenty-two crew", "22 crew"), ("nineteen years", "19 years"), ("Fourteen boats", "14 boats"), ("fourteen boats", "14 boats"),
 ("June seventeenth", "June 17"), ("June sixteenth", "June 16"), ("June twenty-first", "June 21"), ("June twenty-sixth", "June 26"),
 ("April twenty-seventh", "April 27"), ("July fourth", "July 4"),
 ("twenty twenty-one", "2021"), ("twenty nineteen", "2019"), ("twenty eighteen", "2018"),
 ("zero one two", "012"), ("Go-gitch", "Gogic"), ("twenty twenty-two", "2022"), ("twenty twenty-five", "2025"), ("twenty twenty-six", "2026"), ("June twenty-first", "June 21"), ("Gah-yah-nay", "Gayane"), ("Bosh-ko Mar-ko-vitch", "Bosko Markovic"), ("Ee-litch", "Ilic"), ("Kah-vah-yah", "Kavaja"),
 ("reefer man", "reeferman"), ("C T PAT", "C-TPAT"), ("Bartle the third", "Bartle III"),
 ("U S Attorney", "U.S. Attorney"), ("U S jurisdiction", "U.S. jurisdiction"), ("U S case", "U.S. case"), ("M S C", "MSC"),
]

META = dict(
    case="012", label="20 TONS · ONE SHIP",
    title="20 Tons of Cocaine Hidden on One Cargo Ship: The $1.3 Billion Bust",
    imgs={},
    credit=("Footage: U.S. Customs and Border Protection and U.S. Coast Guard via DVIDS — public domain."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."),
    shorts=[
        dict(id="s1", lines=[1, 3], hook="20 TONS OF COCAINE<br>[ONE CARGO SHIP]", title="20 Tons of Cocaine Found on One Cargo Ship", template="before→after seizure reveal"),
        dict(id="s2", lines=[14, 16], hook="14 BOATS AT SEA<br>[ONE CARGO SHIP]", title="14 Boats Loaded One Cargo Ship at Sea", template="single action moment (smuggling boats at sea, illustrative)"),
        dict(id="s3", lines=[38, 40], hook="2.5 MILES OF COCAINE<br>[“LAID END TO END”]", title="2.5 Miles of Cocaine Bricks From One Ship", template="verbatim quote"),
        dict(id="s4", lines=[32, 33], hook="6 AGENCIES<br>[WAITING FOR ONE SHIP]", title="6 Agencies Waited for One Cargo Ship in Philadelphia", template="single action moment (boarding)"),
        dict(id="s5", lines=[35, 37], hook="39,525 POUNDS<br>[COUNTED BRICK BY BRICK]", title="39,525 Pounds of Cocaine, Counted Brick by Brick", template="countdown / numbers"),
    ],
)
