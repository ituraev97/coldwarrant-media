# CASE FILE 028 — Duane "Keefe D" Davis, South Side Compton Crips: convicted Aug. 31, 2026 (Clark County, NV) of the 1996 murder of Tupac Shakur; sentenced Oct. 13, 2026 to 40 years to life.
# CONVICTED AT TRIAL, APPEAL EXPECTED. Sources: episodes/028-keefe-d/sources.md
# shot: ("clip_id", start_sec, {opts}) | ("g:<graphic_name>", 0, {opts}) | ("img:<key>", 0, {kb}) | ("pool:NAME", 0, {}) resolved by alloc.py
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)
F = lambda pool: ("pool:" + pool, 0, {})

LINES = [
 # ---- COLD OPEN
 ("Monday, August thirty-first, twenty twenty-six. A jury in Las Vegas needs less than three hours to convict a sixty-three-year-old man of murder.",
  [F("VER")], {"gap": 0.9, "speed": 1.0}),
 ("The victim is Tupac Shakur. He was shot at a red light in September nineteen ninety-six, and died six days later. He was twenty-five.",
  [F("VER")], {"gap": 0.9, "speed": 1.0}),
 ("The man now convicted is Duane Davis, known to everyone as Keefe D. And prosecutors never claimed he pulled the trigger.",
  [F("VER")], {"gap": 1.0, "speed": 1.0}),
 ("The defense says nothing else put him in that car. No surveillance video. No phone records. Only his own words: to police, to documentary crews, and in a book he wrote himself.",
  [F("VER")], {"gap": 1.1, "speed": 1.0}),
 ("So how does a man talk his way into forty years to life? And how does a thirty-year-old murder end in a conviction, when, according to prosecutors, every other man in the car is dead?",
  [F("SEN")], {"gap": 1.3, "speed": 0.97}),
 ("Case file zero two eight.",
  [G("title", case="028", title='<span class="red">KEEFE D</span>: THE MAN WHO TALKED', sub='DUANE DAVIS · CONVICTED AUG. 31, 2026 · 40 YEARS TO LIFE · 1996 MURDER OF TUPAC SHAKUR', size=130)], {"gap": 2.4}),

 # ---- I THE NIGHT
 ("This is the story of one night in Las Vegas, and the thirty years that followed.",
  [G("chapter", case="028", n="I", t="THE NIGHT")], {"gap": 0.5, "speed": 1.0}),
 ("September seventh, nineteen ninety-six. At the MGM Grand, Mike Tyson fights Bruce Seldon. It lasts one minute and forty-nine seconds. About nine thousand people are there, and many of them boo.",
  [F("OPEN")], {"gap": 0.7, "speed": 1.0}),
 ("Tupac Shakur is at that fight, with Marion Suge Knight, the head of Death Row Records, and a group from Death Row's entourage.",
  [F("OPEN")], {"gap": 0.8, "speed": 1.0}),
 ("After the fight, in the casino lobby, Tupac spots a man named Orlando Anderson. Baby Lane, to his friends. A member of the South Side Compton Crips. Sports Illustrated reported that Anderson had allegedly stolen a medallion from a Death Row member.",
  [F("OPEN")], {"gap": 0.8, "speed": 1.0}),
 ("Tupac punches him. Anderson goes down, and gets stomped by Tupac, Knight, and several others.",
  [F("OPEN")], {"gap": 1.1, "speed": 0.97}),
 ("Remember Anderson's name. He is the nephew of Duane Davis. And according to prosecutors, that beating is the reason everything else happens.",
  [G("cards3", kicker="THE BEATING IN THE MGM GRAND LOBBY · SEPT. 7, 1996", title="WHO IS WHO", cards=[
      {"h": "TUPAC SHAKUR", "t": "Rapper, 25. Death Row Records."},
      {"h": "ORLANDO ANDERSON", "t": "South Side Compton Crips. Beaten in the lobby. Davis's nephew."},
      {"h": "DUANE DAVIS", "t": "Anderson's uncle. Former South Side Compton Crips leader."}])], {"gap": 1.0, "speed": 1.0}),
 ("Later that night, Tupac is in the front seat of a black BMW driven by Suge Knight, in a convoy of about ten cars.",
  [F("PC")], {"gap": 0.7, "speed": 1.0}),
 ("At a red light, at Flamingo Road and Koval Lane, a white Cadillac pulls up beside the BMW. Shots are fired. Tupac is hit several times. Knight is grazed in the head.",
  [I("cad", kb="in"), I("cad2", kb="pan")], {"gap": 1.2, "speed": 0.97, "big": ("WHITE CADILLAC", "FLAMINGO ROAD AND KOVAL LANE · LAS VEGAS · SEPT. 7, 1996")}),
 ("Tupac dies in the hospital six days later. Prosecutors say four men were in that Cadillac.",
  [F("PC")], {"gap": 1.2, "speed": 0.97}),
 ("He was twenty-five. His fourth solo album, All Eyez on Me, had sold about five million copies, and he had six Grammy nominations.",
  [F("PC")], {"gap": 1.0, "speed": 1.0}),
 ("About six months later, in March nineteen ninety-seven, the rapper Biggie Smalls is fatally shot. The Associated Press describes the feud as an East Coast, West Coast rivalry.",
  [F("PC")], {"gap": 1.1, "speed": 1.0}),
 ("Suge Knight was on parole at the time. When a videotape of the lobby beating surfaced, he went back to prison to serve a nine-year sentence.",
  [G("stat", a="9 YEARS", b="SUGE KNIGHT RETURNED TO PRISON AFTER THE LOBBY VIDEOTAPE SURFACED", c="SOURCE: HISTORY.COM")], {"gap": 1.0, "speed": 1.0}),
 ("And Orlando Anderson? Some people suspected him. He denied it. In May nineteen ninety-eight, he was shot to death outside a car wash in Los Angeles.",
  [F("PC")], {"gap": 1.4, "speed": 0.97}),

 ("Tupac's mother had sued Anderson over her son's death. That lawsuit ended when Anderson was killed, before it could be resolved.",
  [F("PC")], {"gap": 1.2, "speed": 1.0}),
 # ---- II THE MAN IN THE CAR
 ("The case goes cold. For decades.",
  [G("chapter", case="028", n="II", t="THE MAN IN THE CAR")], {"gap": 0.5, "speed": 1.0}),
 ("Duane Davis is described by the Associated Press as a former leader of the South Side Compton Crips. By his own account, he was in that white Cadillac, in the front passenger seat.",
  [F("PC")], {"gap": 0.8, "speed": 1.0}),
 ("He has said the driver was a man named Terrence Brown. In the back seat, his nephew Anderson, and a man known as Dre Smith. All three are dead now.",
  [G("list", kicker="DAVIS'S OWN ACCOUNT · NOT A COURT FINDING", title="THE WHITE CADILLAC", items=["Front passenger: Duane Davis (alive)", "Driver: Terrence Brown (dead)", "Back seat: Orlando Anderson (dead)", "Back seat: DeAndrae (Dre) Smith (dead)"], footer="DAVIS'S 2018 TV INTERVIEW AS SUMMARIZED BY WIKIPEDIA · AP/CBS: FOUR MEN, THREE DEAD")], {"gap": 1.0, "speed": 1.0}),
 ("Davis has told the story many times, and the details moved. A prosecutor would later admit that in court. But three things never changed: the white Cadillac, Davis's seat, and a gun passed to the back.",
  [F("PC")], {"gap": 0.9, "speed": 1.0}),
 ("Why? Davis says he wanted revenge. His nephew had just been beaten by Tupac's group, and Davis went looking for payback.",
  [F("PC")], {"gap": 1.0, "speed": 1.0}),
 ("Davis alleges, in his book and public statements, that Sean Diddy Combs offered him money to kill Tupac and Knight. Combs has repeatedly denied any involvement.",
  [F("PC")], {"gap": 1.3, "speed": 0.97}),

 # ---- III THE LONG SILENCE
 ("Twenty-seven years pass before anyone is charged. Why so long?",
  [G("chapter", case="028", n="III", t="THE LONG SILENCE")], {"gap": 0.5, "speed": 1.0}),
 ("In twenty ten, Davis is facing life in prison on drug charges. He meets privately with federal and local authorities, and offers information about the Tupac killing, and about the killing of Biggie Smalls in March nineteen ninety-seven.",
  [F("PC")], {"gap": 0.8, "speed": 1.0}),
 ("According to the Associated Press, he says he was promised his charges would be dropped if he cooperated. The AP reports he avoided prosecution for years through an agreement with law enforcement.",
  [F("PC")], {"gap": 0.9, "speed": 1.0}),
 ("Greg Kading, a former LAPD detective who investigated the case and wrote a book about it, has said that before Davis started talking in public, the cases were unprosecutable.",
  [G("quote", q="Prior to Keffe D's public declarations, the cases were unprosecutable as they stood.", w="GREG KADING, FORMER LAPD DETECTIVE · AS REPORTED BY THE AP")], {"gap": 1.1, "speed": 1.0}),
 ("And then Davis starts talking. In twenty eighteen, in a televised documentary interview, he says he was in the front passenger seat of the car with the shooter.",
  [F("PC")], {"gap": 0.9, "speed": 1.0}),
 ("He declines to name the shooter, citing street code. In twenty nineteen he publishes a memoir. It's called Compton Street Legend.",
  [F("PC")], {"gap": 1.4, "speed": 0.97}),

 # ---- IV THE RAID AND THE ARREST
 ("A man who confesses to being in the car, on camera and in print, is not hard to find.",
  [G("chapter", case="028", n="IV", t="THE RAID AND THE ARREST")], {"gap": 0.5, "speed": 1.0}),
 ("In July twenty twenty-three, Las Vegas police raid a home in Henderson, Nevada, tied to Davis. The search warrant lists items related to Tupac's murder.",
  [F("RAID")], {"gap": 0.8, "speed": 1.0}),
 ("The Associated Press reported what they took: computers, a cellphone, a hard drive, a copy of Vibe magazine with Tupac on the cover, several forty-caliber bullets, two tubs of photographs, and a copy of Davis's own memoir.",
  [G("list", kicker="SEARCH OF A HENDERSON HOME · JULY 2023 · PER THE AP", title="WHAT POLICE TOOK", items=["Computers, a cellphone, a hard drive", "A Vibe magazine featuring Tupac", "Several .40-caliber bullets", "Two tubs of photographs", "A copy of Davis's memoir"], footer="SOURCE: AP / NPR, SEPT. 29, 2023")], {"gap": 1.0, "speed": 1.0}),
 ("Police body camera video from the raid became public. This is part of it.",
  [F("RAID"), F("BODY")], {"gap": 0.9, "speed": 1.0}),
 ("Two months later, on Friday, September twenty-ninth, twenty twenty-three, Davis is arrested, walking near his home. A Nevada grand jury has indicted him on one count: murder with use of a deadly weapon. He is sixty.",
  [F("PC")], {"gap": 0.9, "speed": 1.0}),
 ("At the news conference, prosecutor Marc DiGiacomo calls him the on-ground, on-site commander who ordered the killing. The judge denies bail.",
  [F("PC")], {"gap": 0.9, "speed": 1.0}),
 ("According to prosecutors, Davis is the only man from that Cadillac still alive. And he pleads not guilty.",
  [F("BODY")], {"gap": 1.4, "speed": 0.97}),

 ("In January twenty twenty-four, a judge grants Davis seven hundred fifty thousand dollars bail, and house arrest. His trial is set for February twenty twenty-six. Then it is pushed back. In August twenty twenty-five, he changes defense attorneys.",
  [F("BODY")], {"gap": 1.0, "speed": 1.0}),
 ("Before trial, the defense tries to keep the memoir out of evidence. Prosecutors oppose it. At trial, the memoir is part of the case.",
  [F("PC")], {"gap": 1.1, "speed": 1.0}),
 # ---- V THE TRIAL
 ("It takes almost three more years to get to a jury.",
  [G("chapter", case="028", n="V", t="THE TRIAL")], {"gap": 0.5, "speed": 1.0}),
 ("The trial runs in August twenty twenty-six. Nine days of testimony. Twenty-four witnesses for the prosecution, three for the defense. Sixteen jurors, four of them alternates.",
  [G("stat", a="24 vs 3", b="PROSECUTION VS DEFENSE WITNESSES · NINE DAYS OF TESTIMONY", c="SOURCE: CBS NEWS")], {"gap": 0.9, "speed": 1.0}),
 ("Chief Deputy District Attorney Binu Palal tells the jury that Davis got a gun and went hunting for Tupac and Suge Knight, because his nephew was beaten.",
  [F("OPEN")], {"gap": 0.8, "speed": 1.0}),
 ("Quote: it's a plan, not an impulse. End quote. And the line that defines the whole case: quote, who fired is not the question. End quote.",
  [G("quote", q="“It's a plan, not an impulse.” · “Who fired is not the question.”", w="BINU PALAL, CHIEF DEPUTY DISTRICT ATTORNEY · CLOSING · VIA CBS NEWS")], {"gap": 1.0, "speed": 1.0}),
 ("There's a point of law here that matters. Palal told jurors that corroboration wasn't required, if they believed what Davis himself had said. That is the whole case in one sentence.",
  [F("OPEN")], {"gap": 1.0, "speed": 1.0}),
 ("The prosecution never says Davis fired. It says he planned it, armed it, and rode along. And Palal says Davis's accounts changed over time, but always put him in the white Cadillac.",
  [F("OPEN")], {"gap": 1.0, "speed": 1.0}),
 ("Their evidence is, mostly, Davis. What he told police. What he told documentary makers. The memoir. A scrapbook of articles about Tupac. A Las Vegas hotel bill, with an unclear date, found at his home.",
  [F("OPEN")], {"gap": 0.9, "speed": 1.0}),
 ("The defense, led by attorney Michael Sanft, says nothing beyond Davis's own statements put him in Las Vegas that night. No surveillance footage. No phone records. No physical evidence. He argues Davis's words were braggadocio meant to make him money, not the truth.",
  [F("OPEN")], {"gap": 0.9, "speed": 1.0}),
 ("The jury deliberates for under three hours. On August thirty-first, they find Duane Davis guilty of murder with a deadly weapon, with intent to promote a criminal gang. Prosecutors said they would drop the gang part, citing witness logistics.",
  [F("VER")], {"gap": 0.9, "speed": 1.0}),
 ("In the courtroom: Davis's son. And Tupac's sister, Sekyiwa Shakur, who cried when the verdict was read.",
  [F("VER")], {"gap": 1.4, "speed": 0.97}),

 ("In rebuttal, prosecutor Marc DiGiacomo tells jurors, quote, this guy's scrapbooking his murder, for God's sake. End quote.",
  [F("VER")], {"gap": 1.1, "speed": 1.0}),
 # ---- VI FORTY TO LIFE
 ("On October thirteenth, Davis faces the judge.",
  [G("chapter", case="028", n="VI", t="FORTY TO LIFE")], {"gap": 0.5, "speed": 1.0}),
 ("District Judge Carli Kierny sentences him to forty years to life in prison, with credit for time served. According to the Associated Press, he won't be eligible for parole until at least age one hundred.",
  [F("SEN")], {"gap": 0.9, "speed": 1.0}),
 ("The judge says: quote, the world never forgot about him and his death, and neither did Las Vegas. End quote.",
  [G("quote", q="“The world never forgot about him and his death and neither did Las Vegas.”", w="JUDGE CARLI KIERNY · SENTENCING · OCT. 13, 2026 · VIA AP")], {"gap": 1.0, "speed": 1.0}),
 ("Davis speaks briefly. He asks for the photographs and other belongings police took from his house. He says he has nothing more to say.",
  [F("SEN")], {"gap": 0.9, "speed": 1.0}),
 ("District Attorney Steve Wolfson: quote, today, justice has been served for Tupac Shakur and his loved ones. End quote. His office says it doesn't have enough evidence to charge anyone else, but could, if new information emerges.",
  [F("SEN")], {"gap": 0.9, "speed": 1.0}),
 ("Tupac's sister, Sekyiwa Shakur, says, quote, this man's life mattered. End quote. She says their mother raised Tupac to be a human rights activist, and she believes he would have done that work. His brother Maurice calls the killing devastating, heartbreaking and sad.",
  [F("SEN")], {"gap": 1.0, "speed": 1.0}),
 ("Davis is expected to appeal. And the defense argument remains: take Davis's own words away, and what's left?",
  [G("phases", kicker="WHAT THE CASE RESTED ON", title="HIS OWN WORDS", left=["Police statements", "Documentary interviews", "2019 memoir"], right=["Surveillance video", "Phone records", "Physical evidence"], active="left", total="", footer="PER THE DEFENSE AND CBS NEWS · AN APPEAL IS EXPECTED")], {"gap": 1.0, "speed": 1.0}),
 ("For a long time, a case this old looked impossible. A rapper shot in a car, a gang rivalry, a street code of silence. In the end, it wasn't a witness who broke the silence. It was the man himself, in his own words.",
  [F("SEN")], {"gap": 1.2, "speed": 0.97}),
 ("That was case file zero two eight.",
  [G("end", case="028", label="KEEFE D: THE MAN WHO TALKED")], {"gap": 2.0}),
]

def _L(prefix):
    return [i for i, l in enumerate(LINES, 1) if l[0].startswith(prefix)][0]

DISPLAY = [
 ("August thirty-first, twenty twenty-six", "August 31, 2026"), ("September nineteen ninety-six", "September 1996"), ("September seventh, nineteen ninety-six", "September 7, 1996"),
 ("September twenty-ninth, twenty twenty-three", "September 29, 2023"), ("May nineteen ninety-eight", "May 1998"), ("March nineteen ninety-seven", "March 1997"),
 ("twenty twenty-three", "2023"), ("twenty twenty-six", "2026"), ("twenty eighteen", "2018"), ("twenty nineteen", "2019"), ("twenty ten", "2010"),
 ("forty years to life", "40 years to life"), ("forty-caliber", ".40-caliber"), ("nine-year", "9-year"), ("sixty-three-year-old", "63-year-old"),
 ("one minute and forty-nine seconds", "1 minute 49 seconds"), ("zero two eight", "028"), ("October thirteenth", "October 13"), ("August thirty-first", "August 31"),
 ("Suge Knight", "Suge Knight"),
]

META = dict(
    case="028", label="KEEFE D: THE MAN WHO TALKED",
    title="Keefe D: The Gangster Who Talked Himself Into 40 Years to Life",
    imgs={},
    mute_nat=[],
    credit=("Footage: news-conference, courtroom and police body-camera video of the Las Vegas Metropolitan Police Department / Clark County District Attorney / Eighth Judicial District Court proceedings as broadcast by Law&Crime, CBS News, ABC, USA TODAY, CNN, AP, KTNV and NewsNation, used with commentary. "
            "Convicted at trial; an appeal is expected."),
    shorts=[],
)
