# CASE FILE 007 — Smuggled by Sea: The Deadly Boat Routes Into the U.S.
# Each entry: (vo_text, shots, opts)  — same format as episodes/001-ms13/episode.py
# shot: ("clip_id", start_sec, {opts}) | ("g:<graphic_name>", 0, {opts})
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)

SD = dict(bounds=[[-118.5, 33.85], [-116.3, 31.95]], topPad=170, useCounties=True, highlight={"06073": "#2a2a30", "06059": "#2a2a30"})
FL = dict(bounds=[[-81.4, 28.0], [-78.2, 25.0]], topPad=170, highlight={"44": "#2a2a30"})
PR = dict(bounds=[[-71.3, 19.9], [-65.4, 17.4]], topPad=170, highlight={"214": "#2a2a30", "630": "#5a1217"})

AMO_SD = ("CBP AIR AND MARINE OPERATIONS · SAN DIEGO", "B-ROLL · MARCH 2026")
AMO_AIR = ("CBP MULTI-ROLE ENFORCEMENT AIRCRAFT · SAN DIEGO", "B-ROLL · APRIL 2026")
ILL_SD = ("ILLUSTRATIVE · CBP MARINE UNIT, SAN DIEGO · 2026", "NOT THE VESSEL IN THIS CASE")
PANGAS22 = ("CBP AIR AND MARINE OPERATIONS · OFF SAN DIEGO", "THREE PANGAS, 72 PEOPLE · APRIL 2022")
LANDING17 = ("U.S. COAST GUARD · POINT LOMA, SAN DIEGO", "BOAT LANDING · AUGUST 2017")
PANGA09 = ("U.S. COAST GUARD · SECTOR SAN DIEGO", "PANGA WITH 21 ABOARD · MARCH 2009")
TORREY10 = ("FILE FOOTAGE · COAST GUARD OFF TORREY PINES", "JANUARY 2010 · NOT THE 2023 INCIDENT")
MARATHON = ("U.S. COAST GUARD · OFF MARATHON, FLORIDA", "DECEMBER 2022")
KEYS23 = ("COAST GUARD AND CBP · OFF MARATHON, FLORIDA", "FEBRUARY 2023")
BAHAMAS26 = ("CBP AIR AND MARINE OPERATIONS · NEAR FREEPORT, BAHAMAS", "MAY 11, 2026 · 21 PEOPLE ABOARD")
KEYS26 = ("CBP AND COAST GUARD · NEAR ANGELFISH CREEK, FLA.", "OPERATION VIGILANT SENTRY · SEPT. 2026")
MONA26 = ("U.S. COAST GUARD · MONA PASSAGE", "63 PEOPLE ABOARD · OCTOBER 16, 2026")
PR26 = ("CBP AND BORDER PATROL · PUERTO RICO", "JULY 20, 2026")
CARIB22 = ("U.S. COAST GUARD AIR STATION MIAMI", "INTERDICTED MIGRANT VOYAGE · CARIBBEAN · 2022")
TCI26 = ("CBP AIRCRAFT · NEAR TURKS AND CAICOS", "240 PEOPLE ABOARD · MAY 31, 2026")
POINTLOMA25 = ("U.S. COAST GUARD · 20 MILES OFF POINT LOMA", "14 PEOPLE ABOARD · JANUARY 2025")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("May second, two thousand twenty-one. Early morning, off Point Loma, in San Diego. A forty-foot boat has lost its engine.",
  [C(1026262, 22), C(1026262, 14)], dict(tag=ILL_SD)),
 ("Thirty-two passengers are on board, including three unaccompanied minors. They were told to stay below deck.",
  [C(1026262, 184), C(1026262, 246)], dict(tag=ILL_SD)),
 ("In rain and large swells, the boat drifts aground, and breaks apart.",
  [C(853936, 70), C(853936, 74)], dict(tag=("FILE FOOTAGE · SAN DIEGO COAST", "CBP · NOT THE VESSEL IN THIS CASE"))),
 ("Three people die. Twenty-nine are pulled from the water. The captain swims to shore.",
  [G("stat", a="3", b="DEAD · 29 RESCUED FROM THE WATER", c="POINT LOMA, SAN DIEGO · MAY 2, 2021 · SOURCE: USAO S.D. CAL.")], {}),
 ("The passengers had agreed to pay fifteen to eighteen thousand dollars each. Who sells a seat on a boat like that? And who is out there, trying to stop them?",
  [C(545682, 90), C(545682, 100)], dict(tag=LANDING17, gap=0.6)),
 ("This is the case of human smuggling at sea.",
  [G("title", case="007", title='SMUGGLED BY <span class="red">SEA</span>', sub="THE DEADLY BOAT ROUTES INTO THE U.S.", size=180)], dict(gap=2.6)),

 # ---------------- I: THE PANGAS ----------------
 ("To understand the boats, start with the water south of San Diego.",
  [G("chapter", case="007", n="I", t="THE PANGAS")], {}),
 ("ICE describes the boats smugglers use there in two ways. Pleasure craft. And pangas, repurposed Mexican fishing vessels. Long, open boats, sitting low in the water.",
  [C(314054, 128), C(314054, 150)], dict(tag=PANGA09)),
 ("In one case in April, twenty twenty-two, CBP's Air and Marine Operations detected three pangas with their lights off, heading toward the maritime border. Seventy-two people were on board.",
  [C(853936, 4), C(853936, 40), C(853936, 12)], dict(tag=PANGAS22)),
 ("The boats leave from the coast of Baja California, from places like Po-pot-la, south of Tijuana. Many try to land in San Diego County. Some go much farther north.",
  [G("map", map=dict(SD, cities=[dict(ll=[-117.08, 32.33], name="POPOTLA, MEXICO", d=0.3, size=30, dy=-6), dict(ll=[-117.02, 32.53], name="TIJUANA", d=0.5, size=30, dx=10),
     dict(ll=[-117.24, 32.67], name="POINT LOMA", anchor="end", d=0.7, size=30, dx=-14), dict(ll=[-117.27, 32.96], name="DEL MAR", anchor="end", d=0.85, size=30, dx=-14), dict(ll=[-117.87, 33.6], name="ORANGE COUNTY", d=1.0, size=28)]),
     kicker="THE PACIFIC ROUTE", title="NORTH BY NIGHT", footer="SOURCES: ICE, AUG. 2021 · USAO S.D. CAL., 2026 · BOUNDARIES: U.S. CENSUS")], {}),
 ("In July twenty twenty-one alone, the task force responded to twelve smuggling events off Orange, Los Angeles and Ventura counties.",
  [C(545682, 70), C(545682, 84)], dict(tag=LANDING17)),
 ("Some make it. In August twenty seventeen, a Coast Guard camera followed two boats. One landed at Point Loma, the other in Mission Bay. Twelve Mexican nationals were taken into Border Patrol custody.",
  [C(545682, 25), C(545682, 40), C(545682, 55)], dict(tag=LANDING17)),
 ("In San Diego Sector, from October twenty twenty to the end of August twenty twenty-one, the Border Patrol intercepted three hundred thirty maritime-related events, and made one thousand seven hundred fifty-one arrests.",
  [G("stat", a="1,751", b="ARRESTS · 330 MARITIME-RELATED EVENTS", c="BORDER PATROL SAN DIEGO SECTOR · OCT. 1, 2020 – AUG. 31, 2021 · SOURCE: CBP")], {}),
 ("To fight back, the agencies built a joint command. The Regional Coordinating Mechanism. Ree-com.",
  [G("list", kicker="SAN DIEGO REGIONAL COORDINATING MECHANISM", title="ReCoM",
     items=["CBP Air and Marine Operations", "U.S. Border Patrol · CBP Field Operations", "U.S. Coast Guard", "ICE Homeland Security Investigations", "State and local law enforcement"],
     footer="SOURCE: CBP, JULY 2020 · AUG. 2021")], {}),
 ("They share intelligence, pool their boats and aircraft, and plan operations together.",
  [C(1026262, 70), C(1026262, 98)], dict(tag=AMO_SD)),
 ("The head of the Border Patrol's San Diego Sector, Aaron Hite-key, put it this way.",
  [G("quote", q="“Smuggling along the California coastline is inherently dangerous for all of the involved parties.”", w="AARON HEITKE · CHIEF PATROL AGENT, U.S. BORDER PATROL SAN DIEGO SECTOR · AUG. 2021")], dict(gap=1.0)),

 # ---------------- II: POINT LOMA ----------------
 ("Back to Point Loma.",
  [G("chapter", case="007", n="II", t="POINT LOMA")], {}),
 ("The captain that morning was Antonio Hur-tah-doe, a forty-year-old man from San Diego.",
  [G("doc", header="UNITED STATES v. ANTONIO HURTADO · S.D. CAL.", title="THE CAPTAIN", tsize=120,
     body="Antonio Hurtado, 40, of San Diego.<br>Captain of a 40-foot boat.<br>32 passengers, including 3 unaccompanied minors.<br>Each agreed to pay $15,000 – $18,000.",
     source="SOURCE: USAO S.D. CAL., APRIL 6, 2022", stamp="CONVICTED")], {}),
 ("According to his plea agreement, he repeatedly used controlled substances during the trip, and lost consciousness at least once. For more than an hour, the boat went in circles.",
  [G("timeline", kicker="AS ADMITTED IN THE PLEA AGREEMENT", title="THE TRIP",
     events=[dict(y="AT SEA", t="Captain uses drugs"), dict(y="1+ HOUR", t="Boat circles"), dict(y="~6 A.M.", t="Engine fails"), dict(y="MORNING", t="Drifts aground")],
     footer="SOURCE: USAO S.D. CAL., APRIL 6, 2022")], {}),
 ("Then, around six in the morning, the engine failed. The boat drifted toward the rocks near the Ka-bree-yo National Monument.",
  [G("map", map=dict(bounds=[[-117.42, 32.80], [-117.10, 32.60]], topPad=170, useCounties=True, highlight={"06073": "#2a2a30"},
     cities=[dict(ll=[-117.245, 32.672], name="CABRILLO NATIONAL MONUMENT", sub="BOAT BREAKS APART · MAY 2, 2021", anchor="end", color="#D3212D", d=0.5, size=30, dx=-14), dict(ll=[-117.16, 32.72], name="SAN DIEGO", d=0.8, size=30)]),
     kicker="POINT LOMA", title="THE ROCKS", footer="SOURCES: USAO S.D. CAL. · KPBS, MAY 2021 · BOUNDARIES: U.S. CENSUS")], {}),
 ("Hur-tah-doe jumped overboard, and swam to shore.",
  [C(1026262, 303)], dict(tag=ILL_SD)),
 ("Twenty-nine people were rescued. Three did not survive. Mah-ree-seh-lah Hernandez-Sanchez. Victor Perez-Degollado. Maria Eugenia Chavez-Segovia.",
  [G("doc", header="POINT LOMA · MAY 2, 2021", title="THREE LIVES", tsize=120,
     body="Maricela Hernandez-Sanchez<br>Victor Perez-Degollado<br>Maria Eugenia Chavez-Segovia<br>All three were Mexican citizens.",
     source="SOURCE: USAO S.D. CAL., APR. 6 & AUG. 12, 2022", stamp="IN MEMORY")], dict(gap=0.8)),
 ("In April twenty twenty-two, Hur-tah-doe pleaded guilty. Three counts of attempted bringing in of migrants, resulting in death. He also admitted assaulting a federal officer. He had kneed a Border Patrol agent in the head.",
  [G("list", kicker="UNITED STATES v. HURTADO · GUILTY PLEA", title="THE COUNTS",
     items=["3 × attempted bringing in of aliens resulting in death", "3 × attempted bringing in for financial gain", "1 × assault on a federal officer"],
     footer="SOURCE: USAO S.D. CAL., APRIL 6, 2022")], {}),
 ("That August, Judge Janis Sammartino sentenced him to eighteen years in federal prison.",
  [G("stat", a="18 YEARS", b="FEDERAL PRISON · PLUS 3 YEARS SUPERVISED RELEASE", c="ANTONIO HURTADO · JUDGE JANIS L. SAMMARTINO · AUG. 12, 2022")], {}),
 ("She said it was the most serious kind of case she had seen.",
  [G("quote", q="“…the most egregious case I've ever had in my courtroom in over 15 years in the Southern District of California.”", w="U.S. DISTRICT JUDGE JANIS L. SAMMARTINO · AUG. 12, 2022 · VIA USAO S.D. CAL.")], {}),
 ("At sentencing, the U S attorney, Randy Grossman, said the passengers had put their savings and their lives in this defendant's hands. When Hur-tah-doe pleaded guilty, his advice had been three words.",
  [G("quote", q="“Never trust a smuggler.”", w="RANDY GROSSMAN · U.S. ATTORNEY, SOUTHERN DISTRICT OF CALIFORNIA · APRIL 6, 2022")], {}),
 ("The head of H S I in San Diego, Chad Plantz, said the case showed that human smugglers have no respect for human life.",
  [G("quote", q="“Human smugglers have no respect for human life, as is demonstrated by this defendant.”", w="CHAD PLANTZ · SPECIAL AGENT IN CHARGE, HSI SAN DIEGO · AUG. 12, 2022")], dict(gap=1.0)),

 # ---------------- III: THE FOG ----------------
 ("Point Loma was not the last.",
  [G("chapter", case="007", n="III", t="THE FOG")], {}),
 ("November twenty-sixth, twenty twenty-two. Off Imperial Beach, a boat carrying eight migrants, and its two captains. Three people die.",
  [C(458626, 12), C(458626, 22)], dict(tag=("FILE FOOTAGE · DISABLED PANGA OFF PACIFIC BEACH", "U.S. COAST GUARD · APRIL 2016 · NOT THIS INCIDENT"))),
 ("Prosecutors said the passengers had been told to take off their life vests. A common practice, they wrote, so passengers are quicker and more inconspicuous.",
  [G("quote", q="“…a common practice so passengers are quicker and more inconspicuous…”", w="USAO S.D. CAL. ON PASSENGERS TOLD TO REMOVE LIFE VESTS · DEC. 14, 2023")], {}),
 ("The captain, Jorge Armando Pre-see-ah-doe Vasquez, was sentenced to fifty-four months. His co-captain, Alexis Martinez Pre-see-ah-doe, got fifty months.",
  [G("cards3", kicker="IMPERIAL BEACH · NOV. 26, 2022", title="THE SENTENCES",
     cards=[dict(h="8", t="Migrants aboard", s="Plus 2 crew"), dict(h="54 MO.", t="Captain", s="J. A. Preciado-Vasquez"), dict(h="50 MO.", t="Co-captain", s="A. Martinez-Preciado")],
     footer="SOURCE: USAO S.D. CAL., DEC. 14, 2023")], {}),
 ("Then, March eleventh, twenty twenty-three. Close to midnight, in heavy fog, two pangas approach Black's Beach, in San Diego.",
  [C(314797, 24), C(314797, 33)], dict(tag=TORREY10)),
 ("The pangas overturn in the surf. Eight people die. San Diego's fire chief, James Gartland, called it one of the worst maritime smuggling tragedies he could think of in California.",
  [G("quote", q="“One of the worst maritime smuggling tragedies that I can think of in California.”", w="CHIEF JAMES GARTLAND · SAN DIEGO FIRE-RESCUE · MARCH 2023 · VIA NBC SAN DIEGO")], {}),
 ("A CBP spokesman blamed callous human smugglers, who have no regard for human life.",
  [C(314797, 12), C(314797, 6)], dict(tag=TORREY10)),
 ("The deaths had been climbing. Off Southern California, maritime smuggling deaths went from three in fiscal twenty nineteen, according to the regional task force, to thirteen by late March of fiscal twenty twenty-three, according to authorities cited by eye-news-source.",
  [G("cards3", kicker="MARITIME SMUGGLING DEATHS · SOUTHERN CALIFORNIA COAST", title="RISING",
     cards=[dict(h="3", t="Fiscal year 2019", s="Regional task force"), dict(h="5", t="Fiscal years 2021 and 2022", s="Regional task force"), dict(h="13", t="Fiscal year 2023", s="By late March · authorities")],
     footer="FY2019–22: ReCoM · FY2023: AUTHORITIES · VIA INEWSOURCE / KPBS, MARCH 28, 2023")], {}),
 ("And on May fifth, twenty twenty-five, a twenty-foot panga from Po-pot-la, with nineteen people on board, capsized about two hundred yards off Del Mar. Four died. Two of them were children, fourteen and ten years old.",
  [G("stat", a="4", b="DEAD · 2 OF THEM CHILDREN", c="20-FOOT PANGA · 19 ABOARD · DEL MAR, CALIF. · MAY 5, 2025 · SOURCE: USAO S.D. CAL.")], {}),
 ("Survivors said the captains told them to take off their life jackets. Each passenger paid about thirteen thousand five hundred dollars. In April twenty twenty-six, the two captains pleaded guilty. They were scheduled to be sentenced in June. We found no public record of their sentences.",
  [C(1026262, 152), C(1026262, 205), C(1026262, 285)], dict(tag=ILL_SD)),
 ("Three other people tied to the case were sentenced in federal court in San Diego, to between ten and twenty-one months.",
  [G("cards3", kicker="DEL MAR · MAY 5, 2025", title="THE CASE",
     cards=[dict(h="~$13,500", t="Paid per passenger"), dict(h="2", t="Captains pleaded guilty", s="April 2026"), dict(h="10–21 MO.", t="Three co-defendants sentenced")],
     footer="SOURCES: USAO S.D. CAL., APRIL 14, 2026 · TIMES OF SAN DIEGO, MARCH 23, 2026")], dict(gap=1.0)),

 # ---------------- IV: FORTY ABOARD ----------------
 ("On the other side of the country, the crossing is shorter. And just as dangerous.",
  [G("chapter", case="007", n="IV", t="FORTY ABOARD")], {}),
 ("Saturday night, January twenty-second, twenty twenty-two. A twenty-five-foot boat leaves Bim-ih-nee, in the Bahamas, headed for Florida.",
  [G("map", map=dict(FL, arcs=[dict(**{"from": [-79.27, 25.72], "to": [-79.55, 27.45]}, d=0.4, dur=1.2, bend=-0.2)],
     cities=[dict(ll=[-79.27, 25.72], name="BIMINI", sub="THE BAHAMAS", d=0.2, size=32, dx=14), dict(ll=[-80.32, 27.45], name="FORT PIERCE", anchor="end", d=0.6, size=30, dx=-14),
     dict(ll=[-80.19, 25.77], name="MIAMI", anchor="end", d=0.8, size=30, dx=-14), dict(ll=[-79.55, 27.45], name="SURVIVOR FOUND", sub="~45 MI EAST OF FORT PIERCE INLET", color="#D3212D", d=1.6, size=26, dx=14, dy=-40)]),
     kicker="JANUARY 22–25, 2022", title="THE CROSSING", footer="SOURCE: U.S. COAST GUARD, JAN. 27, 2022 · ROUTE SIMPLIFIED")], {}),
 ("On Sunday, in severe weather, it capsizes. No one on board is wearing a life jacket.",
  [C(866996, 12), C(866996, 30)], dict(tag=("ILLUSTRATIVE · COAST GUARD BOAT CREW AT SEA", "OFF MARATHON, FLA. · DEC. 2022 · NOT THIS INCIDENT"))),
 ("On Tuesday morning, a good Samaritan rescues a man from the capsized boat, about forty-five miles east of Fort Pierce Inlet. He tells the Coast Guard thirty-nine other people were with him.",
  [C(861048, 23), C(861048, 30)], dict(tag=("FILE FOOTAGE · COAST GUARD AIRCREW", "CARIBBEAN · 2022 · NOT THIS INCIDENT"))),
 ("He was Juan Esteban Montoya, twenty-two, from Colombia. His sister was on that boat. She did not survive.",
  [G("quote", q="“Those waves started to come over the boat, and we started to sink.”", w="JUAN ESTEBAN MONTOYA · SURVIVOR · JAN. 31, 2022 · VIA WPTV")], {}),
 ("Crews searched more than ten thousand five hundred square miles. Five bodies were recovered. Thirty-four people were never found.",
  [G("cards3", kicker="FORT PIERCE · JANUARY 2022", title="THE SEARCH",
     cards=[dict(h="10,500+", t="Square miles searched"), dict(h="5", t="Bodies recovered"), dict(h="34", t="Never found")],
     footer="SOURCE: U.S. COAST GUARD SEVENTH DISTRICT, JAN. 27, 2022")], {}),
 ("On January twenty-seventh, the commander of Coast Guard Sector Miami called off the search.",
  [G("quote", q="“…it's with a heavy heart that I have decided to suspend the search.”", w="CAPT. JO-ANN BURDIAN · COMMANDER, COAST GUARD SECTOR MIAMI · JAN. 27, 2022")], {}),
 ("In March twenty twenty-four, federal prosecutors in Miami unsealed an indictment against a Bahamian man, Vandrick Nelson Smith.",
  [G("doc", header="UNITED STATES v. VANDRICK NELSON SMITH · S.D. FLA.", title="CHARGED", tsize=130,
     body="Bahamian national, 33 · arrested in The Bahamas, March 2024.<br>Charged: attempting to bring noncitizens to the U.S. resulting in death (Jan. 2022 voyage), conspiracy, and counts tied to 2021 and 2022 ventures.<br>Maximum penalty: life in prison.",
     source="SOURCE: USAO S.D. FLA., MARCH 26, 2024 · ALLEGATIONS ONLY", stamp="ALLEGED")], {}),
 ("He is charged with attempting to bring noncitizens into the United States, resulting in death, for that voyage. These are allegations. He is presumed innocent unless proven guilty. As of early twenty twenty-five, his extradition case was still pending in the Bahamas. We found no later public update.",
  [C(861048, 0), C(861048, 16), C(861048, 44)], dict(tag=("ILLUSTRATIVE · COAST GUARD AIRCREW SURVEILLANCE", "2022 · NOT THE DEFENDANT OR THIS VOYAGE"))),
 ("The U S attorney in Miami, Markenzy La-point, said human smuggling ventures put people's lives at risk for the sake of profit.",
  [G("quote", q="“Human smuggling ventures put people's lives at risk for the sake of profit.”", w="MARKENZY LAPOINTE · U.S. ATTORNEY, SOUTHERN DISTRICT OF FLORIDA · MARCH 26, 2024")], {}),
 ("The Bim-ih-nee route has a long history. In October twenty thirteen, a boat capsized about seven miles off Miami. Four Haitian women drowned. The smuggler, Naaman Davis, from Bim-ih-nee, had been smoking crack cocaine during the trip. He was sentenced to fourteen years.",
  [G("doc", header="UNITED STATES v. NAAMAN DAVIS · S.D. FLA.", title="14 YEARS", tsize=140,
     body="Naaman Davis, 54, of Bimini, The Bahamas.<br>Oct. 15, 2013: boat capsizes about 7 miles off Miami.<br>Four Haitian women drowned.<br>Smoked crack cocaine during the trip.",
     source="SOURCE: USAO S.D. FLA.", stamp="SENTENCED")], dict(gap=1.0)),

 # ---------------- V: THE MONA PASSAGE ----------------
 ("The third front is in the Caribbean.",
  [G("chapter", case="007", n="V", t="THE MONA PASSAGE")], {}),
 ("Between the Dominican Republic and Puerto Rico lies the Mona Passage. Overloaded boats cross it, headed for Puerto Rico.",
  [G("map", map=dict(PR, arcs=[dict(**{"from": [-69.0, 18.5], "to": [-67.3, 18.2]}, d=0.4, dur=1.2, bend=-0.15)],
     cities=[dict(ll=[-69.9, 18.48], name="DOMINICAN REPUBLIC", anchor="end", d=0.2, size=30, dx=-10, dy=-40), dict(ll=[-66.1, 18.45], name="PUERTO RICO", sub="U.S. TERRITORY", d=0.6, size=32, dy=-40),
     dict(ll=[-67.9, 18.08], name="MONA PASSAGE", color="#D3212D", d=1.0, size=26, dy=60)]),
     kicker="THE CARIBBEAN ROUTE", title="THE PASSAGE", footer="BOUNDARIES: NATURAL EARTH · ROUTE SIMPLIFIED")], {}),
 ("In October twenty twenty-six, a Coast Guard helicopter crew filmed this one. Sixty-three people on board. They were sent back to the Dominican Republic the next day.",
  [C(1026857, 0, crop="iw*0.8:ih:iw*0.1:0"), C(1026857, 40, crop="iw*0.8:ih:iw*0.1:0")], dict(tag=MONA26)),
 ("In May twenty twenty-six, a CBP aircraft out of Jacksonville found another one, near the Turks and Caicos Islands. Two hundred forty people. Its engines had lost power, and it was taking on water. Local authorities rescued them.",
  [C(1009312, 2), C(1009312, 9), C(1009312, 15)], dict(tag=TCI26)),
 ("Some boats don't make it. In May twenty twenty-two, a boat from the Dominican Republic carried forty-eight people toward Puerto Rico. Eleven died.",
  [G("stat", a="11", b="DEAD · 48 PEOPLE ON BOARD", c="VOYAGE FROM THE DOMINICAN REPUBLIC · MAY 2022 · SOURCE: U.S. DEPT. OF JUSTICE")], {}),
 ("A Dominican man, Fermin Mon-tee-ya, pleaded guilty to bringing in aliens at an unauthorized place, resulting in death. In February twenty twenty-five, he was sentenced to nine years.",
  [G("doc", header="UNITED STATES v. FERMIN MONTILLA · D. PUERTO RICO", title="9 YEARS", tsize=140,
     body="Fermin Montilla, 45, Dominican national.<br>Pleaded guilty Sept. 13, 2024: bringing in aliens at an unauthorized place resulting in death.<br>Sentenced Feb. 10, 2025.",
     source="SOURCE: U.S. DEPARTMENT OF JUSTICE, FEB. 2025", stamp="SENTENCED")], {}),
 ("The head of H S I in San Juan, Rebecca Gonzalez-Ramos, had a warning for anyone thinking of making the trip.",
  [G("quote", q="“…it's extremely dangerous and is not worth your life.”", w="REBECCA GONZALEZ-RAMOS · SPECIAL AGENT IN CHARGE, HSI SAN JUAN · FEB. 2025")], {}),
 ("And the landings continue. On July twentieth, twenty twenty-six, agents stopped two smuggling ventures on opposite ends of Puerto Rico. Thirty-seven people were apprehended, along with one U S citizen.",
  [C(1015881, 62), C(1015881, 85), C(1015881, 128)], dict(tag=PR26, gap=1.0)),

 # ---------------- VI: THE HUNTERS ----------------
 ("So what does the law say about the people who run these boats?",
  [G("chapter", case="007", n="VI", t="THE HUNTERS")], {}),
 ("Under federal law, bringing someone into the U S anywhere other than a port of entry carries up to ten years in prison. If lives are put in danger, up to twenty. If someone dies, up to life, or even death.",
  [G("cards3", kicker="8 U.S.C. § 1324 · BRINGING IN ALIENS", title="THE PENALTIES",
     cards=[dict(h="10 YRS", t="Maximum, per person"), dict(h="20 YRS", t="If lives are endangered", s="Or serious bodily injury"), dict(h="LIFE", t="If a death results", s="Or the death penalty")],
     footer="SOURCE: 8 U.S.C. § 1324(a)(1)(B) · ANY VESSEL USED IS SUBJECT TO FORFEITURE")], {}),
 ("And any vessel used in the crime is seized, and subject to forfeiture.",
  [C(314054, 200), C(314054, 225)], dict(tag=PANGA09)),
 ("Smuggling for profit can also bring a mandatory minimum. Three years for each person, on a first or second violation.",
  [G("stat", a="3 YEARS", b="MINIMUM · FOR EACH PERSON BROUGHT IN FOR PROFIT", c="FIRST OR SECOND VIOLATION · 8 U.S.C. § 1324(a)(2)(B)")], {}),
 ("To find the boats before they land, CBP flies long-range patrols, looking for vessels heading north from Mexican waters.",
  [C(1010409, 22), C(1010409, 236), C(1010409, 320)], dict(tag=AMO_AIR)),
 ("In May twenty twenty-six, near Freeport, in the Bahamas, a CBP aircrew spotted a suspicious cabin cruiser. After hours of surveillance, two marine units moved in. Twenty-one people were on board.",
  [C(1007294, 30), C(1007294, 48), C(1007294, 62)], dict(tag=BAHAMAS26)),
 ("In September, near Angelfish Creek in Florida, a CBP aircraft on patrol spotted a twenty-seven-foot boat. One suspected smuggler. Twenty-two migrants.",
  [C(1023782, 14), C(1023782, 30)], dict(tag=KEYS26)),
 ("Back in California, in January twenty twenty-five, the Coast Guard cutter Terrell Horne and CBP crews stopped a boat about twenty miles off Point Loma. Fourteen people were on board.",
  [C(950728, 10.2), C(950728, 42)], dict(tag=POINTLOMA25)),
 ("Off the Florida Keys, Coast Guard and CBP crews pull alongside makeshift vessels like this one, and take the passengers off.",
  [C(874557, 23), C(874557, 35), C(874557, 64)], dict(tag=KEYS23)),
 ("A CBP Air and Marine Operations official in San Diego, Brandon Tucker, summed up the problem.",
  [G("quote", q="“Smugglers don't adhere to boating safety standards.”", w="BRANDON TUCKER · DEPUTY DIRECTOR OF AIR OPERATIONS, CBP AMO SAN DIEGO · AUG. 2021")], dict(gap=1.0)),

 # ---------------- CLOSE ----------------
 ("Point Loma. Imperial Beach. Black's Beach. Del Mar. Fort Pierce. The Mona Passage.",
  [G("timeline", kicker="HUMAN SMUGGLING AT SEA · CASES IN THIS FILE", title="THE CROSSINGS",
     events=[dict(y="MAY 2021", t="Point Loma · 3 dead"), dict(y="JAN. 2022", t="Fort Pierce · 39 lost"), dict(y="MAY 2022", t="Puerto Rico · 11 dead"), dict(y="MAR. 2023", t="Black's Beach · 8 dead"), dict(y="MAY 2025", t="Del Mar · 4 dead")],
     footer="SOURCES: USAO S.D. CAL. · USAO S.D. FLA. · DOJ · U.S. COAST GUARD · NBC SAN DIEGO")], {}),
 ("Fifteen thousand dollars. Eighteen thousand. Thirteen thousand five hundred. That's what a seat costs, according to court records.",
  [C(874559, 20), C(874559, 40)], dict(tag=KEYS23)),
 ("The smugglers set the price. The passengers carry the risk. And the crews on the water keep looking for the next boat.",
  [C(1026262, 260), C(1026262, 60)], dict(tag=AMO_SD, gap=0.8)),
 ("Case file zero zero seven. Closed. The next file is already on the desk.",
  [G("end", case="007", label="SMUGGLED BY SEA")], dict(gap=4.0)),
]

# spoken -> display replacements for subtitles (longest first where they overlap)
DISPLAY = [
 ("two thousand twenty-one", "2021"),
 ("twenty twenty-six", "2026"), ("twenty twenty-five", "2025"), ("twenty twenty-four", "2024"), ("twenty twenty-three", "2023"), ("twenty twenty-two", "2022"),
 ("twenty twenty-one", "2021"), ("twenty twenty", "2020"), ("twenty nineteen", "2019"),
 ("May second", "May 2"), ("November twenty-sixth", "November 26"), ("March eleventh", "March 11"), ("May fifth", "May 5"),
 ("January twenty-second", "January 22"), ("January twenty-seventh", "January 27"), ("July twentieth", "July 20"),
 ("fifteen to eighteen thousand dollars", "$15,000 to $18,000"), ("thirteen thousand five hundred dollars", "$13,500"),
 ("Fifteen thousand dollars", "$15,000"), ("Eighteen thousand", "$18,000"), ("Thirteen thousand five hundred", "$13,500"),
 ("one thousand seven hundred fifty-one", "1,751"), ("three hundred thirty", "330"), ("ten thousand five hundred", "10,500"),
 ("Thirty-two", "32"), ("Twenty-nine", "29"), ("Seventy-two", "72"), ("Sixty-three", "63"), ("Thirty-seven", "37"), ("Thirty-four", "34"), ("Twenty-one", "21"), ("Twenty-two", "22"),
 ("thirty-nine", "39"), ("forty-eight", "48"), ("forty-five", "45"), ("fifty-four months", "54 months"), ("fifty months", "50 months"),
 ("forty-foot", "40-foot"), ("forty-year-old", "40-year-old"), ("twenty-foot", "20-foot"), ("twenty-five-foot", "25-foot"), ("twenty-seven-foot", "27-foot"),
 ("twenty-two,", "22,"), ("eighteen years", "18 years"), ("two hundred yards", "200 yards"), ("nineteen people", "19 people"),
 ("twelve smuggling", "12 smuggling"), ("fourteen and ten", "14 and 10"), ("thirteen by", "13 by"),
 ("Hur-tah-doe", "Hurtado"), ("Ka-bree-yo", "Cabrillo"), ("Po-pot-la", "Popotla"), ("Ree-com", "ReCoM"), ("Hite-key", "Heitke"), ("Bim-ih-nee", "Bimini"), ("Mon-tee-ya", "Montilla"), ("Mah-ree-seh-lah", "Maricela"), ("Two hundred forty", "240"), ("twenty seventeen", "2017"), ("twenty thirteen", "2013"), ("Twelve Mexican", "12 Mexican"), ("Fourteen people", "14 people"), ("eight migrants", "8 migrants"), ("twenty miles", "20 miles"), ("seven miles", "7 miles"), ("fourteen years", "14 years"), ("twenty-one months", "21 months"), ("ten and", "10 and"), ("Three years for", "Three years for"),
 ("Pre-see-ah-doe Vasquez", "Preciado-Vasquez"), ("Martinez Pre-see-ah-doe", "Martinez-Preciado"), ("La-point", "Lapointe"), ("eye-news-source", "inewsource"),
 ("H S I", "HSI"), ("U S ", "U.S. "), ("U S,", "U.S.,"),
 ("zero zero seven", "007"),
]

META = dict(
    case="007", label="SMUGGLED BY SEA",
    title="Smuggled by Sea: The Deadly Boat Routes Into the U.S.",
    imgs={},
    credit=("Footage: U.S. Customs and Border Protection and U.S. Coast Guard via DVIDS — public domain."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."),
    shorts=[
        dict(id="s1", lines=[1, 5], hook="$18,000 A SEAT<br>[3 NEVER MADE IT]"),
        dict(id="s2", lines=[18, 24], hook="THE CAPTAIN<br>[GOT 18 YEARS]"),
        dict(id="s3", lines=[40, 45], hook="40 ON BOARD<br>[1 SURVIVOR]"),
        dict(id="s4", lines=[32, 35], hook="THE FOG<br>[AT BLACK'S BEACH]"),
        dict(id="s5", lines=[51, 56], hook="THE MONA PASSAGE<br>[11 DEAD]"),
    ],
)
