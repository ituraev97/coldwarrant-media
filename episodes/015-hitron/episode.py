# CASE FILE 015 — 4 Drug Boats in 15 Minutes: The Coast Guard Sniper Mission (HITRON)
# Each entry: (vo_text, shots, opts)  — same format as episodes/001-ms13/episode.py
# shot: ("clip_id", start_sec, {opts}) | ("g:<graphic_name>", 0, {opts})
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

UAS = ("STONE'S DRONE FEED · FOUR GO-FAST BOATS", "FEB. 19, 2025 · ~110 MI SOUTH OF THE GALÁPAGOS · USCG VIA DVIDS")
STONE = ("USCGC STONE · EASTERN PACIFIC", "2024–25 DEPLOYMENT · USCG VIA DVIDS")
STONEX = ("ILLUSTRATIVE · USCGC STONE BOARDING TEAMS", "2024–25 DEPLOYMENT · USCG VIA DVIDS")
STONEV = ("ILLUSTRATIVE · USCGC STONE CREW AT SEA", "FEB. 2026 · USCG VIA DVIDS")
HIT = ("HITRON · JACKSONVILLE, FLA.", "JAN. 2026 · USCG VIA DVIDS")
HITT = ("HITRON TRAINING · ILLUSTRATIVE", "JAN. 2026 · USCG VIA DVIDS")
HITV = ("ILLUSTRATIVE · HITRON AIRCREW VIDEO", "USCG VIA DVIDS")
MAR10 = ("ILLUSTRATIVE · A BOAT STOPPED BY STONE'S HITRON CREW", "MARCH 10, 2025 · NOT THE CASE DESCRIBED · USCG VIA DVIDS")
JAN31 = ("STONE'S DRONE · INFRARED", "JAN. 31, 2025 · STONE'S DRONE · USCG VIA DVIDS")
JAN30 = ("STONE'S DRONE FEED", "JAN. 30, 2025 · USCG VIA DVIDS")
DOOR = ("ILLUSTRATIVE · A HITRON DOOR GUN AT SEA", "JUNE 2025 · NOT THE STONE CASE · USCG VIA DVIDS")
TAH = ("USCGC TAHOMA'S HITRON CREW · OFF CARTAGENA", "MAY 8, 2026 · USCG VIA DVIDS")
TAHO = ("USCGC TAHOMA OFFLOAD · PORT EVERGLADES, FLA.", "MAY 14, 2026 · USCG VIA DVIDS")
TAHN = ("USCGC TAHOMA OFFLOAD · PORT EVERGLADES, FLA.", "NOV. 4, 2026 · USCG VIA DVIDS")
OFF = ("USCGC STONE OFFLOAD · PORT EVERGLADES, FLA.", "MARCH 20, 2025 · USCG VIA DVIDS")

PAC = dict(bounds=[[-112, 20], [-70, -14]], topPad=170,
           highlight={"218": "#2a2a30", "170": "#2a2a30", "484": "#2a2a30", "591": "#2a2a30", "188": "#2a2a30", "604": "#2a2a30"},
           labels=[dict(ll=[-108, 4], t="EASTERN PACIFIC", size=30),
                   dict(ll=[-75.5, 5.5], t="COLOMBIA", size=26)])

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Four drug boats. One Coast Guard helicopter. And one rule for the marksman in the open door: shoot until the engines stop.",
  [C(955958, 26.8, pb=1), C(955958, 31.7, pb=1)], dict(tag=UAS)),
 ("February twenty twenty-five, about a hundred and ten miles south of the Gah-lah-pah-gose Islands. A drone launched from a Coast Guard cutter picks up the boats, running together across open water.",
  [C(955958, 0.3, pb=1), C(955958, 4.6, pb=1), C(955958, 8.9, pb=1)], dict(tag=UAS)),
 ("The Coast Guard's own account calls it four boats in fifteen minutes. Nearly eleven thousand pounds of cocaine. Eight suspected smugglers in custody.",
  [C(955958, 38.7, pb=1), C(955958, 42.0, pb=1), C(955958, 45.3, pb=1)], dict(tag=UAS)),
 ("How does a helicopter stop a speedboat in the middle of the ocean? And why does the Coast Guard keep a squadron of aerial marksmen to do it?",
  [C(997828, 0.4), C(998143, 24.0), C(997828, 57.4)], dict(tag=HITT)),
 ("This is the case file on the Coast Guard's helicopter snipers.",
  [G("title", case="015", title='COAST GUARD <span class="red">SNIPERS</span>', sub="HITRON · THE HELICOPTER SQUADRON", size=150)], dict(gap=2.6)),

 # ---------------- I: ONE BOAT IS A WIN ----------------
 ("Start on the ship.",
  [G("chapter", case="015", n="I", t="ONE BOAT IS A WIN")], {}),
 ("In the winter of twenty twenty-four into twenty twenty-five, the Coast Guard cutter Stone was on a long counter-drug patrol in the Eastern Pacific, off Mexico, Ecuador and the Gah-lah-pah-gose.",
  [C(997205, 46.3), C(956672, 104.0), C(997205, 93.0)], dict(tag=("USCGC STONE · EASTERN PACIFIC", "USCG VIA DVIDS"))),
 ("It had already been a busy trip. Three days before Christmas, Stone's crew had seized about twelve thousand two hundred twenty pounds of cocaine in a single case.",
  [G("map", map=dict(PAC, cities=[
       dict(ll=[-90.4, -0.6], name="GALÁPAGOS", anchor="end", dx=-14, dy=-20, d=0.3, size=26),
       dict(ll=[-90.4, -2.4], name="FEB. 19 · FOUR BOATS", sub="~110 MI SOUTH OF THE GALÁPAGOS", anchor="end", dx=-14, dy=34, d=0.6, size=26, color="#D3212D"),
       dict(ll=[-88.0, -2.0], name="DEC. 22 · 12,220 LB", sub="~180 MI SE OF THE GALÁPAGOS", dx=14, dy=40, d=1.0, size=24),
       dict(ll=[-104.0, 10.0], name="JAN. 30–31", sub="~630–715 MI OFF MEXICO", d=1.4, size=24)]),
     kicker="USCGC STONE · DEC. 2024 – MARCH 2025", title="ONE PATROL", footer="SOURCE: U.S. COAST GUARD, MARCH 20, 2025 · LOCATIONS APPROXIMATE")], {}),
 ("On board, the ship carried a drone, and a helicopter crew from a small Coast Guard unit called Hit-ron.",
  [C(870910, 0.3), C(956672, 63.1)], dict(tag=("USCGC STONE & HITRON · FLIGHT DECK", "USCG VIA DVIDS"))),
 ("The drone did a lot of the hunting. On January thirtieth, about seven hundred fifteen miles off Mexico, it found a suspicious boat carrying about thirty-eight hundred pounds of cocaine.",
  [C(955959, 0.5, pb=1), C(955959, 4.6, pb=1), C(955959, 8.7, pb=1)], dict(tag=JAN30)),
 ("The next day, six hundred thirty miles out, it found another. Its infrared camera picks the boat out on the dark water. More than twenty-five hundred pounds of cocaine were seized.",
  [C(955960, 3.6, pb=1), C(955960, 7.5, pb=1), C(955960, 12.0, pb=1)], dict(tag=JAN31)),
 ("By February, the ship and the helicopter crew had worked six cases together. They had gone through a tough certification side by side, and built trust the ordinary way: board games, swim calls, port visits.",
  [C(870910, 4.0), C(870910, 8.6), C(956672, 51.0)], dict(tag=("USCGC STONE & HITRON · ILLUSTRATIVE", "2023 · 2025 · USCG VIA DVIDS"))),
 ("On February nineteenth, the operations officer, Lieutenant Commander Steven Naylor, was watching the drone's feed in the ship's command center, when a go-fast boat appeared on the screen. Then three more.",
  [C(955958, 13.3, pb=1), C(955958, 17.8, pb=1), C(955958, 22.3, pb=1)], dict(tag=UAS)),
 ("Stone had three small boats to put boarding teams on four targets. So two of the teams would have to share one boat.",
  [C(956672, 95.8), C(956672, 99.5)], dict(tag=STONE)),
 ("The commanding officer, Captain Jonathan Carter, kept the goal modest. One boat, he told the crew, would count as a win.",
  [G("quote", q="“Don't do anything crazy.”", w="CAPT. JONATHAN CARTER · THEN COMMANDING OFFICER, USCGC STONE · AS RECOUNTED BY THE U.S. COAST GUARD, 2026")], dict(gap=0.8)),

 # ---------------- II: WARNING SHOTS, THEN ENGINES ----------------
 ("To understand what happened next, you need to know who was in that helicopter.",
  [G("chapter", case="015", n="II", t="WARNING SHOTS, THEN ENGINES")], {}),
 ("Hit-ron stands for Helicopter Interdiction Tactical Squadron. It is based in Jacksonville, Florida, and the Coast Guard calls it its only airborne use-of-force unit.",
  [C(997828, 18.5), C(998143, 245.0), C(998143, 300.8)], dict(tag=HIT)),
 ("Its crews fly M H sixty-five Dolphin helicopters, and they deploy for weeks at a time aboard Coast Guard cutters, far out at sea.",
  [C(998143, 266.0), C(998143, 276.0), C(997828, 158.4)], dict(tag=HIT)),
 ("On a case, three people in that helicopter matter most. One pilot flies. A second pilot coordinates and tracks the targets. And in the door sits a precision marksman.",
  [C(998143, 47.5), C(998143, 55.5), C(998143, 63.5)], dict(tag=HITT)),
 ("The usual sequence goes like this. First, warning shots. If the boat keeps going, the marksman fires again, this time to disable its engines.",
  [G("list", kicker="HITRON · HOW A BOAT IS STOPPED", title="THE PROCEDURE",
     items=["Helicopter launches from the cutter", "Warning shots", "If it runs: disabling fire at the engines", "Boarding team moves in"],
     footer="SOURCE: U.S. COAST GUARD (MYCG), MAY 2026")], {}),
 ("Once the boat is stopped, a boarding team from the cutter moves in, and the helicopter stays overhead to watch over them.",
  [C(955959, 26.0, pb=1), C(955959, 13.0, pb=1), C(955959, 15.6, pb=1)], dict(tag=STONEX)),
 ("Hit-ron's commanding officer, Captain Dan Broadhurst, describes the job in a way you might not expect.",
  [G("quote", q="“It's fundamentally a life-saving mission.”", w="CAPT. DAN BROADHURST · COMMANDING OFFICER, HITRON · U.S. COAST GUARD (MYCG), MAY 2026")], dict(gap=0.8)),
 ("The squadron runs its own shooting program. One marksman joined with only basic firearms experience, and went on to become an instructor.",
  [C(997828, 66.0), C(997828, 70.4), C(998143, 330.0)], dict(tag=HITT)),
 ("One precision marksman, Petty Officer First Class Taylor Wolf, explained the difference: we're shooting from an aerial platform, which is very different than anywhere else.",
  [C(997828, 61.6), C(998143, 99.0), C(998143, 105.0)], dict(tag=("PO1 TAYLOR WOLF · PRECISION MARKSMAN, HITRON", "JAN. 2026 · USCG VIA DVIDS"))),
 ("The pilots come from everywhere. One of them, Lieutenant Andy Gilliam, flew Black Hawks in the Army before joining the Coast Guard through its direct commission aviator program.",
  [C(997828, 141.3), C(997828, 167.0), C(997828, 176.0)], dict(tag=HITT)),

 # ---------------- III: EMBRACE THE CHAOS ----------------
 ("Back to the four boats.",
  [G("chapter", case="015", n="III", t="EMBRACE THE CHAOS")], {}),
 ("The plan was called Operation Shoot and Move. The helicopter would disable the boats from behind, and Stone's small boats would follow, putting boarding teams aboard.",
  [C(955961, 79.5), C(955961, 83.1), C(955961, 86.7)], dict(tag=STONEX)),
 ("It did not go to plan. The smugglers circled, dumped their cargo into the sea, and split up.",
  [C(955958, 36.6, pb=1), C(968865, 133.0), C(968865, 135.0)], dict(tag=("FEB. 19 DRONE FEED → ILLUSTRATIVE: A HITRON DOOR GUN", "2025 · USCG VIA DVIDS"))),
 ("They scattered like ants, said the pilot tracking them. The other pilot, Lieutenant Commander Adam Ownbey, said plan B was simple: you make it work. Embrace the chaos.",
  [C(956672, 66.9), C(956672, 70.6), C(997828, 145.3)], dict(tag=HITV)),
 ("In the door, the precision marksman, Petty Officer Second Class Ryan Teal, worked the mounted weapon. Every one of those boats had two engines.",
  [C(968865, 85.0), C(968865, 91.0)], dict(tag=DOOR)),
 ("Teal described his rule.",
  [G("quote", q="“I had to shoot until all means of propulsion were disabled.”", w="AMT2 RYAN TEAL · PRECISION MARKSMAN, HITRON · U.S. COAST GUARD (MYCG), 2026")], dict(gap=0.8)),
 ("For the first time on a case, he had to reload. By his own estimate, he fired either thirty-three or thirty-six rounds.",
  [G("stat", a="33 OR 36", b="ROUNDS FIRED (HIS ESTIMATE) · THREE BOATS DISABLED", c="TWO ENGINES EACH · HIS FIRST RELOAD ON A CASE · SOURCE: U.S. COAST GUARD (MYCG), 2026")], {}),
 ("The fourth boat stopped and its crew complied. But a communications mix-up delayed the boarding team, so the helicopter stayed with it, until it was running low on fuel.",
  [C(956672, 111.0), C(955959, 18.4, pb=1), C(955959, 22.0, pb=1)], dict(tag=("ILLUSTRATIVE · STONE'S BOATS AT WORK", "OTHER 2025 CASES · USCG VIA DVIDS"))),
 ("When it was over, Naylor and Carter confirmed the result the simplest way they could. Each held up four fingers.",
  [C(997205, 52.0), C(956672, 10.3)], dict(tag=("ILLUSTRATIVE · USCGC STONE BOARDING TEAMS", "USCG VIA DVIDS"))),
 ("Naylor admitted it afterward: honestly, none of us thought it would happen.",
  [C(997205, 88.4), C(997205, 90.7)], dict(tag=STONEV)),
 ("The Coast Guard's tally: four go-fast boats, eight suspected smugglers, and about ten thousand eight hundred eighty-five pounds of cocaine.",
  [G("cards3", kicker="FEB. 19, 2025 · ~110 MILES SOUTH OF THE GALÁPAGOS", title="ONE DAY",
     cards=[dict(h="4", t="go-fast boats"), dict(h="8", t="suspected smugglers"), dict(h="10,885 LB", t="cocaine")],
     footer="SOURCE: U.S. COAST GUARD PRESS RELEASE, MARCH 20, 2025")], {}),
 ("Stone's patrol still was not over. On March tenth, about two hundred seventy miles southeast of the Gah-lah-pah-gose, the ship's Hit-ron crew spotted one more suspicious boat.",
  [C(955961, 0.5, pb=1), C(955961, 4.5, pb=1), C(955961, 8.5, pb=1)], dict(tag=("USCGC STONE'S HITRON CREW · THE MARCH 10 CASE", "2025 · USCG VIA DVIDS"))),
 ("On the helicopter's camera, it runs, throwing up a long wake. Stone's crew interdicted it: about three thousand nine hundred eighty pounds of cocaine, and two suspected smugglers detained.",
  [C(955961, 34.0, pb=1), C(955961, 40.0, pb=1), C(955961, 96.0)], dict(tag=("USCGC STONE'S HITRON CREW · THE MARCH 10 CASE", "2025 · USCG VIA DVIDS"))),
 ("In August twenty twenty-six, at a ceremony in Washington, the White House drug policy office gave Hit-ron and Stone's crew its Maritime Interdiction Award, for that one day in February.",
  [C(870910, 15.0), C(870910, 20.0), C(997828, 189.2)], dict(tag=("HITRON & USCGC STONE · ILLUSTRATIVE", "2023 · 2026 · USCG VIA DVIDS"))),

 # ---------------- IV: ONE THOUSAND ----------------
 ("That day was one case among more than a thousand.",
  [G("chapter", case="015", n="IV", t="ONE THOUSAND")], {}),
 ("The squadron dates back to nineteen ninety-nine. That August, a Jacksonville Hit-ron crew made its first drug interdiction, by shooting out the outboard motors of a go-fast boat.",
  [C(998143, 249.0), C(998143, 256.7), C(998143, 285.0)], dict(tag=("HITRON MH-65 DOLPHINS · ILLUSTRATIVE", "JAN. 2026 · USCG VIA DVIDS"))),
 ("By its twentieth year, it counted more than five hundred interdictions, and more than twenty billion dollars' worth of narcotics stopped.",
  [G("timeline", kicker="HITRON · HELICOPTER INTERDICTION TACTICAL SQUADRON", title="FROM 1 TO 1,000",
     events=[dict(y="AUG. 1999", t="First interdiction"), dict(y="2019", t="500+ interdictions"), dict(y="AUG. 2025", t="1,000th interdiction")],
     footer="SOURCES: MARITIME EXECUTIVE, 2019 · U.S. COAST GUARD, 2025")], {}),
 ("The thousandth came on August twenty-fifth, twenty twenty-five, working with the cutter Midgett in the Eastern Pacific: about three thousand six hundred six pounds of suspected cocaine, and six suspected smugglers apprehended. The boat would not comply, and the aircrew used force to stop it.",
  [C(968865, 158.0), C(968865, 163.0), C(968865, 168.0), C(968865, 173.0)], dict(tag=("ILLUSTRATIVE · HITRON AIRCREW VIDEO", "2025–26 · NOT THE MIDGETT CASE · USCG VIA DVIDS"))),
 ("It was a record stretch. From October twenty twenty-four to that September, the Coast Guard says, Hit-ron crews interdicted three point three billion dollars in drugs, about three times the unit's historic annual average.",
  [C(968865, 240.0), C(968865, 250.0), C(968865, 278.0)], dict(tag=("$3.3 BILLION IN UNDER A YEAR · ≈3× AVERAGE", "U.S. COAST GUARD · ILLUSTRATIVE: HITRON, JUNE 2025"))),
 ("Then came the cutter Munro. It left Al-uh-mee-duh, California, in November twenty twenty-five. Somewhere in the Eastern Pacific, its Hit-ron aircrew used warning shots and disabling fire to stop one go-fast boat.",
  [C(968865, 288.0), C(968865, 296.0), C(997828, 101.0)], dict(tag=("ILLUSTRATIVE · HITRON AIRCREW VIDEO", "NOT THE MUNRO CASE · USCG VIA DVIDS"))),
 ("On board: twenty-two thousand fifty-two pounds of cocaine. The Coast Guard called it the single largest maritime drug seizure in eighteen years. Six suspected smugglers were detained.",
  [G("stat", a="22,052 LB", b="COCAINE · ONE GO-FAST BOAT · USCGC MUNRO", c="LARGEST SINGLE MARITIME DRUG SEIZURE IN 18 YEARS · SOURCE: U.S. COAST GUARD")], {}),
 ("By then the Coast Guard had launched Operation Pacific Viper in the Eastern Pacific. By its own count, the operation was averaging about sixteen hundred pounds of cocaine a day.",
  [G("stat", a="~1,600 LB", b="COCAINE INTERDICTED PER DAY · OPERATION PACIFIC VIPER", c="LAUNCHED AUG. 2025 · EASTERN PACIFIC · SOURCE: U.S. COAST GUARD")], {}),
 ("To mark the year, Hit-ron painted one of its helicopters black. The Coast Guard calls it the Blackfin scheme, for the unit's role in seizing more than five hundred eleven thousand pounds of cocaine.",
  [C(998078, 0.4, vert=1), C(998078, 4.6, vert=1), C(998078, 8.8, vert=1)], dict(tag=("HITRON'S BLACKFIN MH-65", "2026 · USCG VIA DVIDS"))),

 # ---------------- V: THREE BOATS AT ONCE ----------------
 ("The method has not changed. Here it is in twenty twenty-six.",
  [G("chapter", case="015", n="V", t="THREE BOATS AT ONCE")], {}),
 ("Most of these chases start long before the helicopter takes off. A joint task force in Key West, Florida, watches the smuggling routes. Once an interdiction is close, control shifts to the Coast Guard.",
  [G("map", map=dict(bounds=[[-92, 27], [-66, 2]], topPad=170,
       highlight={"170": "#2a2a30", "591": "#2a2a30", "862": "#2a2a30", "192": "#2a2a30"},
       labels=[dict(ll=[-77.5, 15.5], t="CARIBBEAN SEA", size=30), dict(ll=[-73.5, 5.0], t="COLOMBIA", size=28)],
       cities=[dict(ll=[-81.78, 24.56], name="KEY WEST", sub="JOINT INTERAGENCY TASK FORCE SOUTH", anchor="end", dx=-14, dy=10, d=0.3, size=28),
               dict(ll=[-76.3, 10.4], name="~90 MI OFF CARTAGENA", sub="MAY 8, 2026 · THREE BOATS", anchor="end", dx=-14, dy=-30, d=0.8, size=26, color="#D3212D"),
               ]),
     kicker="USCGC TAHOMA · MAY 2026", title="WATCHED, THEN STOPPED", footer="SOURCE: U.S. COAST GUARD, MAY 14, 2026 · LOCATIONS APPROXIMATE")], {}),
 ("May eighth. About ninety miles off Car-tah-hay-nah, Colombia, the crew of the cutter Tahoma went after three suspected smuggling boats at once, with two small boats and a Hit-ron aircrew.",
  [C(1006861, 7.4), C(1006861, 39.4), C(997828, 4.4)], dict(tag=TAH)),
 ("Two of the boats stopped when Coast Guard crews told them to. The third kept going, and the helicopter crew used precision sniper fire on its engines.",
  [C(955961, 18.0, pb=1), C(955961, 26.0, pb=1)], dict(tag=MAR10)),
 ("The suspected smugglers aboard jumped into the sea. The aircrew dropped flotation devices, and they were rescued, with no injuries reported.",
  [C(997205, 19.5), C(997205, 21.8), C(955961, 92.0)], dict(tag=STONEV)),
 ("About six thousand eighty-five pounds of cocaine, worth nearly forty-five point eight million dollars. Commander Nolan Kway-vahs, Tahoma's commanding officer, called interdicting three vessels at once a testament to the unwavering professionalism of the crews involved.",
  [C(1007057, 24.0), C(1007057, 17.5), C(1007057, 28.7), C(1007057, 57.3)], dict(tag=TAHO)),
 ("Six days later, at Port Everglades, Florida, Tahoma's crew offloaded about eight thousand one hundred eighty-five pounds of narcotics, worth about sixty-one point six million dollars.",
  [C(1007057, 2.0), C(1007057, 36.0), C(1007057, 45.0)], dict(tag=TAHO)),
 ("And in November twenty twenty-six, Tahoma was back at the same pier, with another three thousand six hundred twenty-two pounds.",
  [C(1028611, 2.0), C(1028611, 20.0), C(1028611, 27.0)], dict(tag=TAHN)),

 # ---------------- VI: THE DOCK AND THE COURT ----------------
 ("Every one of these chases ends in the same two places. A pier, and a courtroom.",
  [G("chapter", case="015", n="VI", t="THE DOCK AND THE COURT")], {}),
 ("Stone's patrol ended in March twenty twenty-five. At Port Everglades, Florida, its crew offloaded about forty-five thousand six hundred pounds of narcotics, worth more than five hundred seventeen point five million dollars.",
  [C(955996, 37.75), C(955996, 42.75), C(955996, 53.0)], dict(tag=OFF)),
 ("It was the haul from fourteen interdictions. Thirty-five suspected smugglers were transferred ashore, to face federal prosecution in U.S. courts.",
  [C(955996, 71.0), C(955996, 66.8), C(955996, 13.0)], dict(tag=("14 INTERDICTIONS · 35 SUSPECTS → FEDERAL COURT", "MARCH 20, 2025 · USCG VIA DVIDS"))),
 ("None of them is named here. A charge is an accusation, and anyone charged is presumed innocent unless proven guilty in court.",
  [C(955996, 19.5), C(955996, 24.5)], dict(tag=OFF)),
 ("Stone was not alone out there. The cutter Mohawk worked the same waters, and its commanding officer, Commander David Ratner, summed up the strategy.",
  [C(955996, 29.4), C(955996, 3.8)], dict(tag=OFF)),
 ("In his words.",
  [G("quote", q="“The fight against drug trafficking and transnational criminal organizations doesn't begin at our U.S. maritime borders.”", w="CMDR. DAVID RATNER · COMMANDING OFFICER, USCGC MOHAWK · U.S. COAST GUARD, MARCH 2025")], dict(gap=0.8)),
 ("Captain Carter credited the partnership between the ship and the helicopter.",
  [G("quote", q="“The HITRON crew seamlessly integrated into our crew and together we unified to achieve historic results.”", w="RDML JONATHAN CARTER · COMMANDING OFFICER OF USCGC STONE AT THE TIME · U.S. COAST GUARD (MYCG), 2026")], dict(gap=0.8)),
 ("Since nineteen ninety-nine, the method has barely changed. Find the boat from the air. Warn it. And if it runs, take away its engines.",
  [C(998143, 270.0), C(998143, 292.0)], dict(tag=HIT)),
 ("Hit-ron passed one thousand interdictions in twenty twenty-five. The boats keep coming. So does the helicopter.",
  [C(997828, 114.2), C(997828, 123.0)], dict(tag=STONEV)),
 ("Case file zero one five. Closed for now.",
  [G("end", case="015", label="COAST GUARD SNIPERS")], dict(gap=3.0)),
]

DISPLAY = [
 ("twenty twenty-six", "2026"), ("twenty twenty-five", "2025"), ("twenty twenty-four", "2024"), ("twenty twenty-three", "2023"),
 ("nineteen ninety-nine", "1999"), ("Hit-ron", "HITRON"),
 ("M H sixty-five", "MH-65"), ("a hundred and ten miles", "110 miles"),
 ("four boats in fifteen minutes", "four boats in 15 minutes"),
 ("Nearly eleven thousand pounds", "Nearly 11,000 pounds"),
 ("twelve thousand two hundred twenty pounds", "12,220 pounds"),
 ("February nineteenth", "February 19"), ("August twenty-fifth", "August 25"), ("May eighth", "May 8"),
 ("thirty-three or thirty-six rounds", "33 or 36 rounds"),
 ("ten thousand eight hundred eighty-five pounds", "10,885 pounds"),
 ("more than five hundred interdictions", "more than 500 interdictions"),
 ("twenty billion dollars'", "$20 billion"),
 ("three thousand six hundred six pounds", "3,606 pounds"),
 ("three point three billion dollars", "$3.3 billion"),
 ("twenty-two thousand fifty-two pounds", "22,052 pounds"), ("eighteen years", "18 years"),
 ("sixteen hundred pounds", "1,600 pounds"),
 ("five hundred eleven thousand pounds", "511,000 pounds"),
 ("ninety miles", "90 miles"),
 ("six thousand eighty-five pounds", "6,085 pounds"), ("forty-five point eight million dollars", "$45.8 million"),
 ("eight thousand one hundred eighty-five pounds", "8,185 pounds"), ("sixty-one point six million dollars", "$61.6 million"),
 ("three thousand six hundred twenty-two pounds", "3,622 pounds"),
 ("forty-five thousand six hundred pounds", "45,600 pounds"), ("five hundred seventeen point five million dollars", "$517.5 million"),
 ("fourteen interdictions", "14 interdictions"), ("Thirty-five suspected", "35 suspected"),
 ("one thousand interdictions", "1,000 interdictions"),
 ("zero one five", "015"), ("Gah-lah-pah-gose", "Galápagos"), ("Car-tah-hay-nah", "Cartagena"), ("Kway-vahs", "Cuevas"), ("Al-uh-mee-duh", "Alameda"),
 ("January thirtieth", "January 30"), ("seven hundred fifteen miles", "715 miles"), ("thirty-eight hundred pounds", "3,800 pounds"),
 ("six hundred thirty miles", "630 miles"), ("twenty-five hundred pounds", "2,500 pounds"), ("March tenth", "March 10"),
 ("two hundred seventy miles", "270 miles"), ("three thousand nine hundred eighty pounds", "3,980 pounds"),
]

META = dict(
    case="015", label="COAST GUARD SNIPERS",
    title="4 Drug Boats in 15 Minutes: The Coast Guard Sniper Mission",
    imgs={},
    # interdiction / produced-feature videos: no nat sound (possible gunfire, licensed music, interviews)
    mute_nat=[955958, 955959, 955960, 955961, 956672, 997205, 997828, 998143, 998078, 968865, 1006861, 870910],
    credit=("Footage: U.S. Coast Guard via DVIDS — public domain."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."),
    shorts=[
        dict(id="s1", lines=[1, 3], hook="4 DRUG BOATS<br>[1 HELICOPTER]", title="4 Drug Boats, 1 Helicopter: 10,885 Pounds of Cocaine Stopped", template="single action moment (drone feed: four go-fasts → stopped)"),
        dict(id="s2", lines=[28, 30], hook="“SCATTERED LIKE ANTS”<br>[4 BOATS · 1 HELICOPTER]", title="4 Drug Boats 'Scattered Like Ants' — the Coast Guard Got All 4", template="verbatim quote"),
        dict(id="s3", lines=[51, 53], hook="3 BOATS AT ONCE<br>[6,085 LB OF COCAINE]", title="3 Drug Boats at Once: Smugglers Jump Overboard, All Rescued", template="single action moment (sniper stop → jump → rescue)"),
        dict(id="s4", lines=[58, 59], hook="45,600 LB<br>[UNLOADED FROM 1 CUTTER]", title="45,600 Pounds of Drugs Unloaded From One Coast Guard Cutter", template="before→after seizure reveal"),
        dict(id="s5", lines=[43, 44], hook="1,000 INTERDICTIONS<br>[$3.3 BILLION IN UNDER A YEAR]", title="1,000 Interdictions: The Coast Guard's Helicopter Sniper Squadron", template="countdown / ranking (1,000th → $3.3B → record)"),
    ],
)
