# CASE FILE 027 — Colonel Henry Richard Crespo-Guzman, ex-Bolivian Air Force colonel, extradited to SDNY (release 26-338, Nov. 20, 2026)
# CHARGED, NOT CONVICTED. Allegation framing + presumption-of-innocence lines in cold open, ch. II, ch. VI.
# SOURCE script: footage shots are pool placeholders ("pool:NAME") resolved by alloc.py -> episode.py
# shot: ("clip_id", start_sec, {opts}) | ("g:<graphic_name>", 0, {opts}) | ("img:<key>", 0, {kb})
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)
F = lambda pool: ("pool:" + pool, 0, {})

REL = "SDNY PRESS RELEASE 26-338 · NOV. 20, 2026"
T_PHOTO = ("DOJ PHOTO · CHARGED, NOT CONVICTED", "IMAGE FROM THE SDNY RELEASE · THE RELEASE SAYS IT WAS CAPTURED DURING THE MEETING IT DESCRIBES")
T_FACE = ("DOJ PHOTO · CHARGED, NOT CONVICTED", "HENRY RICHARD CRESPO-GUZMAN · IMAGE FROM THE SDNY RELEASE, NOV. 20, 2026")

LINES = [
 # ---------- COLD OPEN ----------
 ("A Bolivian Air Force base. A colonel, in full uniform, at a meeting, prosecutors say.",
  [I("still", kb="in")], {"tag": T_PHOTO, "gap": 0.7, "speed": 0.97}),
 ("Behind him, they say, his subordinates stood guard with automatic weapons. He explained how long it takes to load cocaine onto an airplane.",
  [I("face", kb="in"), I("still", kb="in")], {"tag": T_FACE, "gap": 0.8, "speed": 1.0}),
 ("That is what federal prosecutors in New York allege. On November nineteenth, that colonel was flown out of Bolivia to face the charges.",
  [I("still", kb="pan"), I("face", kb="pan")], {"tag": T_PHOTO, "gap": 0.9, "speed": 0.97}),
 ("Henry Richard Crespo-Guzman is charged, not convicted. Under American law, he is presumed innocent.",
  [I("face", kb="pan")], {"tag": T_FACE, "gap": 0.6, "speed": 0.98, "big": ("CHARGED, NOT CONVICTED", "PRESUMED INNOCENT · EVERYTHING HERE IS AN ALLEGATION")}),
 ("He faces three counts. One of them carries a mandatory minimum of thirty years in prison.",
  [I("still", kb="in")], {"tag": T_PHOTO, "gap": 1.1, "speed": 0.95, "big": ("30-YEAR MINIMUM", "ON ONE OF THREE COUNTS · IF CONVICTED · " + REL)}),
 ("What does the indictment actually say? And what does it leave out?",
  [F("AIR"), F("AIR")], {"gap": 1.1, "speed": 0.96}),
 ("Case file zero two seven.",
  [G("title", case="027", title='THE <span class="red">COLONEL</span> EXTRADITED', sub="HENRY RICHARD CRESPO-GUZMAN · CHARGED, NOT CONVICTED · SDNY · NOV. 20, 2026", size=130)], {"gap": 1.8}),

 # ---------- I. THE MEETING ----------
 ("First, the meeting.", [G("chapter", case="027", n="I", t="THE MEETING")], {"gap": 0.5, "speed": 1.0}),
 ("Start with the photograph. It sits in the middle of the Justice Department's press release, and the release says it shows the defendant in his official uniform, captured during one of these meetings.",
  [I("still", kb="in"), I("face", kb="in")], {"tag": T_PHOTO, "gap": 0.7, "speed": 1.0}),
 ("The wording around it is specific. Quote: the defendant conducted meetings at the Bolivian Air Force Base while dressed in his official Bolivian Air Force Uniform, while subordinate members of the Bolivian Air Force stood guard with automatic weapons. End quote.",
  [G("doc", header="SDNY PRESS RELEASE 26-338 · NOV. 20, 2026", title="ACCORDING TO THE SUPERSEDING INDICTMENT",
     body="“…the defendant conducted meetings at the Bolivian Air Force Base while dressed in his official Bolivian Air Force Uniform, while subordinate members of the Bolivian Air Force stood guard with automatic weapons.”",
     stamp="ALLEGATION", source="SOURCE: U.S. ATTORNEY'S OFFICE, S.D.N.Y.")], {"gap": 1.0, "speed": 0.98}),
 ("At one such meeting, the release says, he described the base. He explained that it was part of a restricted military zone. He discussed the types of aircraft it could accommodate. And he detailed the quantities, and the time needed, to load cocaine onto aircraft there.",
  [F("AIR"), F("AIR"), F("AIR")], {"gap": 0.9, "speed": 1.0}),
 ("The base is in a place the release spells Cuatro Canadas, in Bolivia. Prosecutors say he had access to it as part of his duties as a colonel, and that he used it to safeguard cocaine loads on their way to several countries, including the United States.",
  [F("AIR"), F("AIR")], {"gap": 0.8, "speed": 1.0}),
 ("That is the allegation, in the prosecutors' words. What the release does not say matters just as much.",
  [I("face", kb="in")], {"tag": T_FACE, "gap": 0.7, "speed": 1.0}),
 ("It gives no number of kilograms. It names no aircraft. It gives no flight date, and it does not say how many weapons were involved.",
  [G("list", kicker="NOT IN THE JUSTICE DEPARTMENT RELEASE", title="WHAT THE RELEASE LEAVES OUT", items=["Kilograms of cocaine", "Type of aircraft", "Flight dates", "Number of weapons"], footer="SOURCE: SDNY PRESS RELEASE 26-338 · NOV. 20, 2026")],
  {"gap": 1.0, "speed": 0.97}),
 ("Some Bolivian news outlets have reported a figure of about one thousand kilograms. That number is not in the Justice Department's release, so this video does not treat it as established.",
  [F("BOAT")], {"gap": 0.8, "speed": 1.0}),
 ("One more thing about the picture. The release does not say who took it, or how. That is as much as the public record supports.",
  [I("still", kb="pan"), I("face", kb="in")], {"tag": T_PHOTO, "gap": 1.2, "speed": 0.97}),

 # ---------- II. THE CHARGES ----------
 ("Now, the charges.", [G("chapter", case="027", n="II", t="THE CHARGES")], {"gap": 0.5, "speed": 1.0}),
 ("The document behind the release is a superseding indictment. That means prosecutors in the Southern District of New York replaced an earlier charging document with a new one. The release does not say what changed.",
  [F("AIR"), F("AIR")], {"gap": 0.8, "speed": 1.04}),
 ("The new one has three counts.",
  [G("cards3", kicker="THE THREE COUNTS · ALL ALLEGATIONS", title="CHARGED, NOT CONVICTED",
     cards=[{"h": "COUNT ONE", "t": "10 YRS MIN", "s": "Conspiracy to import cocaine · max life"},
            {"h": "COUNT TWO", "t": "30 YRS MIN", "s": "Machineguns + destructive devices · max life · consecutive"},
            {"h": "COUNT THREE", "t": "LIFE MAX", "s": "Conspiracy to use and carry machineguns"}],
     footer="IF CONVICTED · SOURCE: SDNY PRESS RELEASE 26-338 · NOV. 20, 2026")], {"gap": 0.9, "speed": 1.0}),
 ("Count one is conspiracy to import cocaine into the United States. If he is convicted, the judge must sentence him to at least ten years, and can go as high as life.",
  [F("AIR"), F("AIR")], {"gap": 0.8, "speed": 1.0}),
 ("Count two is the one that changes the arithmetic. It charges using, carrying and possessing machineguns and destructive devices in connection with that conspiracy. The minimum on that count alone is thirty years. The maximum is life. And by law it has to run consecutively to any other sentence.",
  [F("AIR"), F("AIR"), F("AIR")], {"gap": 1.1, "speed": 0.97}),
 ("Count three is a conspiracy to use and carry machineguns. The release lists no minimum on that one. A maximum of life.",
  [F("AIR")], {"gap": 0.9, "speed": 1.0}),
 ("Two cautions, and both come from the Justice Department itself. The maximums are set by Congress and are given, in the release's words, for informational purposes only, because any sentence will be decided by the judge. And a mandatory minimum is a floor that applies only after a conviction. Nobody has been convicted of anything here.",
  [I("face", kb="in"), I("still", kb="pan")], {"tag": T_FACE, "gap": 1.2, "speed": 0.97}),
 ("Notice, too, what kind of case this is. It is a conspiracy: the allegation is that he agreed with other people. The release says that he and his co-conspirators, quote, agreed to, and did, manufacture cocaine intended for importation to the United States. End quote. It does not name those co-conspirators.",
  [F("BOAT"), F("BOAT")], {"gap": 1.0, "speed": 1.0}),
 ("Put the dates in a row, and one gap stands out. The alleged conduct runs from at least September twenty twenty to August twenty twenty-one. He was arrested in Bolivia on August twenty-eighth, twenty twenty-six. That is five years after the period in the indictment ends. The release does not say what happened in between.",
  [G("timeline", kicker="THE ALLEGED PERIOD VS. THE ARREST", title="2020 → 2026",
     events=[{"y": "SEPT. 2020", "t": "Alleged period begins"}, {"y": "AUG. 2021", "t": "Alleged period ends"}, {"y": "AUG. 28, 2026", "t": "Arrested in Bolivia"}, {"y": "NOV. 19, 2026", "t": "Extradited"}, {"y": "NOV. 20, 2026", "t": "Initial appearance scheduled"}])],
  {"gap": 1.3, "speed": 0.97}),

 # ---------- III. FROM SANTA CRUZ TO NEW YORK ----------
 ("From Santa Cruz to New York.", [G("chapter", case="027", n="III", t="SANTA CRUZ TO NEW YORK")], {"gap": 0.5, "speed": 1.0}),
 ("The arrest came on August twenty-eighth. Bolivian outlets, including El Deber, place it in the city of Santa Cruz. From there he was moved to San Roque prison, in Sucre, where, El Deber reports, he stayed while his situation was decided.",
  [G("map", map={"bounds": [[-70.5, -23.5], [-56.5, -8.5]], "topPad": 170, "highlight": {"068": "#3a2a2a"},
                 "cities": [{"ll": [-63.18, -17.78], "name": "SANTA CRUZ", "sub": "ARRESTED AUG. 28 · FLIGHT OUT NOV. 19", "d": 0.4, "size": 24},
                            {"ll": [-65.26, -19.03], "name": "SUCRE", "sub": "SAN ROQUE PRISON", "d": 1.0, "size": 24, "anchor": "end"}]},
     kicker="BOLIVIA", title="THE EXTRADITION ROUTE", footer="SOURCES: EL DEBER, NOV. 19, 2026 · EL DIARIO, NOV. 20, 2026")], {"gap": 0.9, "speed": 1.0}),
 ("Bolivia handles a request like this through its courts. In September, according to El Deber, the Supreme Court gave the request course. One Bolivian columnist describes this step as a limited check: the judges look at identity and whether the order is valid. Guilt is left to the court in New York.",
  [F("AIR"), F("AIR")], {"gap": 1.0, "speed": 1.02}),
 ("His family sees it differently. His wife told El Deber that no evidence had been shown in Bolivia, and that the United States had sent only a document asking for him. The Rio Times, an outlet produced by an automated AI newsroom, reported that she also said he has never traveled to the United States.",
  [I("face", kb="pan"), I("still", kb="pan"), I("face", kb="in")], {"tag": T_FACE, "gap": 0.8, "speed": 1.0}),
 ("Those are a family member's statements to the press, not court findings. And in the coverage reviewed for this video, no defense lawyer is quoted at all.",
  [F("AIR")], {"gap": 1.0, "speed": 0.97}),
 ("His status is also disputed. El Diario reported that the Air Force says he belonged to its active reserve, and that any actions of his were of a personal nature. Other Bolivian outlets call him retired. The Justice Department calls him a former colonel.",
  [F("AIR"), F("AIR")], {"gap": 0.9, "speed": 1.02}),
 ("On Wednesday, November eighteenth, he left the Sucre prison and was taken by road to Santa Cruz, El Diario reported. On Thursday the nineteenth, a charter flight carried him out of Viru Viru airport, with DEA agents on board.",
  [F("BOAT"), F("AIR")], {"gap": 1.0, "speed": 0.97}),
 ("In the release, U.S. Attorney Jamie McDonald thanks a long list of partners: Southern Command, the DEA's Lima office, the State Department, the U.S. embassy in La Paz, Homeland Security Investigations in Bolivia, Interpol Bolivia, the Bolivian National Police, and a Bolivian anti-narcotics intelligence and special operations group, known by the initials FELCN-GIOE.",
  [G("list", kicker="THANKED IN THE RELEASE", title="WHO HELPED", items=["U.S. Southern Command", "DEA Lima Country Office", "U.S. Embassy, La Paz · HSI Bolivia", "INTERPOL Bolivia · Bolivian National Police", "FELCN-GIOE (Bolivian anti-narcotics unit)"], footer="SOURCE: SDNY PRESS RELEASE 26-338 · NOV. 20, 2026")],
  {"gap": 1.0, "speed": 1.04}),
 ("What the list does not tell you is how the case began. The release says only that this happened during the investigation. It does not say whether there were recordings, or who was in the room, or when the United States first learned of these meetings.",
  [F("AIR"), F("AIR")], {"gap": 1.0, "speed": 0.98}),
 ("And this same office has told a story like this before.",
  [F("BIG")], {"gap": 1.3, "speed": 0.95}),

 # ---------- IV. A COUNTRY WITHOUT THE DEA ----------
 ("A country without the DEA.", [G("chapter", case="027", n="IV", t="A COUNTRY WITHOUT THE DEA")], {"gap": 0.5, "speed": 1.0}),
 ("First, the politics, because the extradition lands in the middle of an argument. According to the Rio Times, a news site produced by an automated AI newsroom, Bolivia's government under Evo Morales expelled the DEA in two thousand eight.",
  [F("BIG"), F("BIG")], {"gap": 0.8, "speed": 1.04}),
 ("In November twenty twenty-five, after Rodrigo Paz took office, a Bolivian vice minister announced that the DEA would soon return. In February, the same official said the help would be informational and logistical, with no DEA bases in Bolivia.",
  [F("BIG"), F("AIR")], {"gap": 0.8, "speed": 1.04}),
 ("The DEA's own framing is different. Administrator Terrance Cole says in the release that the extradition sends, quote, a powerful message to those who abuse positions of public trust. End quote. He thanks Bolivian partners whose cooperation, he says, reflects, quote, our renewed commitment to confronting international drug trafficking. End quote.",
  [G("quote", q="“…no one is beyond the reach of American justice.”", w="DEA ADMINISTRATOR TERRANCE C. COLE · SDNY RELEASE 26-338 · NOV. 20, 2026")], {"gap": 1.1, "speed": 0.97}),
 ("Not everyone in Bolivia welcomes it. The same site notes that supporters of Morales call handovers like this a loss of sovereignty.",
  [F("AIR")], {"gap": 0.8, "speed": 1.0}),
 ("And a columnist in El Diario made a different point. Writing on November twenty-fourth, he argued that a colonel could not have acted alone, and that Bolivia's own authorities have not said what domestic investigations exist. That is an opinion column, not a finding. But it is the question a Bolivian reader is asking.",
  [F("AIR"), F("AIR")], {"gap": 1.3, "speed": 1.0}),

 # ---------- V. THE FIRST ONE ----------
 ("The first one.", [G("chapter", case="027", n="V", t="THE FIRST ONE")], {"gap": 0.5, "speed": 1.0}),
 ("To see where a case like this can go, look at one that has already finished. The Crespo-Guzman release does not mention it, and nothing in it ties the two men together. But it is the same office, the same unit, and some of the same prosecutors.",
  [F("AIR"), F("AIR")], {"gap": 0.9, "speed": 1.02}),
 ("Maximiliano Davila Perez, nicknamed Macho, was the director of FELCN, Bolivia's chief anti-narcotics agency, until November twenty nineteen. Charges against him were unsealed in Manhattan on February second, twenty twenty-two, along with a State Department reward of up to five million dollars. He was extradited on December thirteenth, twenty twenty-four.",
  [G("cards3", kicker="MAXIMILIANO DAVILA PEREZ · FORMER FELCN DIRECTOR", title="THE PRECEDENT",
     cards=[{"h": "CHARGED", "t": "FEB. 2022", "s": "Unsealed in Manhattan · $5M reward offered"},
            {"h": "EXTRADITED", "t": "DEC. 2024", "s": "Arrived in the U.S. Dec. 13, 2024"},
            {"h": "SENTENCED", "t": "25 YEARS", "s": "Convicted Oct. 23, 2025 · sentenced Mar. 19, 2026"}],
     footer="SOURCES: SDNY RELEASES, FEB. 2, 2022 · DEC. 13, 2024 · MAR. 19, 2026")], {"gap": 1.0, "speed": 1.0}),
 ("According to the Justice Department's sentencing release, the case against him rested on meetings and calls recorded by DEA confidential sources, in twenty nineteen and twenty twenty.",
  [F("BIG"), F("BIG")], {"gap": 0.8, "speed": 1.02}),
 ("On those recordings, the release says, he promised armed protection for a shipment of more than one ton of cocaine, leaving Bolivia, passing through the Dominican Republic, and ending up in New York. He suggested airports where he controlled security. He said that on the day of the shipment he would carry out an operation elsewhere and, quote, take out everyone, meaning that no investigative personnel would be around to interfere. And he committed to sending agents to guard the plane with their standard-issue machineguns as it was loaded.",
  [F("AIR"), F("AIR"), F("AIR")], {"gap": 1.0, "speed": 0.98}),
 ("He also said, according to the release, that he planned to make money from it.",
  [G("quote", q="“…you are also going to profit, I am going to win too.”", w="DAVILA PEREZ, ON A RECORDING DESCRIBED IN THE SDNY SENTENCING RELEASE · MAR. 19, 2026")], {"gap": 1.1, "speed": 0.97}),
 ("A ten-kilogram sample of cocaine was delivered in Lima, Peru, in December twenty nineteen, the earlier release says, ahead of the larger shipment.",
  [F("BOAT")], {"gap": 0.9, "speed": 1.0}),
 ("On October twenty-third, twenty twenty-five, after a one-week jury trial before Judge Denise Cote, Davila Perez was convicted. On March nineteenth, twenty twenty-six, she sentenced him to twenty-five years in prison, followed by five years of supervised release.",
  [F("AIR"), F("AIR")], {"gap": 1.1, "speed": 0.97}),
 ("When he was extradited, then-U.S. Attorney Damian Williams said, quote, our reach is global, our memory is long. End quote.",
  [G("quote", q="“…our reach is global, our memory is long…”", w="U.S. ATTORNEY DAMIAN WILLIAMS · SDNY · DEC. 13, 2024")], {"gap": 1.1, "speed": 0.97}),
 ("Now compare the charges. In the twenty twenty-four release, Davila Perez faced a ten-year minimum on the drug count, and the release lists no minimum on the weapons count. Crespo-Guzman's weapons count carries thirty years.",
  [F("AIR"), F("AIR")], {"gap": 0.9, "speed": 1.0}),
 ("That is not a prediction. The evidence is different, the man is different, and Crespo-Guzman has not had a trial. But it shows how much the weapons count changes the arithmetic.",
  [I("face", kb="in"), I("still", kb="pan")], {"tag": T_FACE, "gap": 1.3, "speed": 0.96}),

 # ---------- VI. WHAT HAPPENS NEXT ----------
 ("What happens next.", [G("chapter", case="027", n="VI", t="WHAT HAPPENS NEXT")], {"gap": 0.5, "speed": 1.0}),
 ("The public record so far is short. He was arrested on August twenty-eighth and extradited on November nineteenth. He was scheduled to make his first appearance on November twentieth before Magistrate Judge Gary Stein. The case is assigned to District Judge Victor Marrero.",
  [F("AIR"), F("AIR")], {"gap": 0.9, "speed": 1.0}),
 ("Beyond that, nothing in the sources reviewed says whether he has a lawyer in New York, what happened at that hearing, or when a trial might be held.",
  [I("still", kb="in"), I("face", kb="pan")], {"tag": T_PHOTO, "gap": 1.0, "speed": 0.98}),
 ("A federal case like this usually goes one of two ways: a trial, where a jury must be convinced beyond a reasonable doubt, or a guilty plea. Davila Perez went to trial. Which road Crespo-Guzman takes is the open question.",
  [F("AIR"), F("AIR")], {"gap": 1.0, "speed": 1.0}),
 ("Two things are worth watching. Whether prosecutors name the co-conspirators the release only describes. And whether a court filing finally puts a number on the cocaine.",
  [F("BIG"), F("AIR")], {"gap": 1.1, "speed": 1.0}),
 ("Until then, the sentence that governs everything above comes from the release itself. Quote: the charges in the Superseding Indictment are merely accusations, and the defendant is presumed innocent unless and until proven guilty. End quote.",
  [G("quote", q="“The charges in the Superseding Indictment are merely accusations, and the defendant is presumed innocent unless and until proven guilty.”", w="SDNY PRESS RELEASE 26-338 · NOV. 20, 2026")], {"gap": 1.3, "speed": 0.95}),
 ("That was case file zero two seven.", [G("end", case="027", label="THE COLONEL EXTRADITED")], {"gap": 2.0}),
]

def _L(prefix):
    return [i for i, l in enumerate(LINES, 1) if l[0].startswith(prefix)][0]

DISPLAY = [
 ("Kwah-troh Kah-nyah-dahs", "Cuatro Cañadas"), ("Cress-poh Goos-mahn", "Crespo-Guzman"), ("Cress-poh", "Crespo"),
 ("Dah-vee-lah Peh-res", "Dávila Pérez"), ("Dah-vee-lah", "Dávila"), ("Vee-roo Vee-roo", "Viru Viru"), ("Soo-kreh", "Sucre"),
 ("Mah-rare-oh", "Marrero"), ("F-E-L-C-N G-I-O-E", "FELCN-GIOE"), ("Fell-kin", "FELCN"), ("El Deh-ber", "El Deber"),
 ("El Dee-ah-ree-oh", "El Diario"), ("Pahs", "Paz"), ("Moh-rah-les", "Morales"), ("Coat", "Cote"), ("D-E-A's", "DEA's"), ("D-E-A", "DEA"), ("H-S-I", "HSI"),
 ("September twenty twenty", "September 2020"), ("August twenty twenty-one", "August 2021"), ("August twenty-eighth, twenty twenty-six", "August 28, 2026"),
 ("November twenty twenty-five", "November 2025"), ("November twenty nineteen", "November 2019"), ("December twenty nineteen", "December 2019"),
 ("February second, twenty twenty-two", "February 2, 2022"), ("December thirteenth, twenty twenty-four", "December 13, 2024"),
 ("October twenty-third, twenty twenty-five", "October 23, 2025"), ("March nineteenth, twenty twenty-six", "March 19, 2026"),
 ("twenty nineteen and twenty twenty", "2019 and 2020"), ("twenty twenty-four", "2024"), ("two thousand eight", "2008"),
 ("five million dollars", "$5 million"), ("twenty-five years", "25 years"), ("thirty years", "30 years"), ("ten-year", "10-year"), ("ten years", "10 years"),
 ("ten-kilogram", "10-kilogram"), ("one thousand kilograms", "1,000 kilograms"), ("five years", "5 years"), ("one-week", "one-week"),
 ("November eighteenth", "November 18"), ("November nineteenth", "November 19"), ("November twentieth", "November 20"), ("November twenty-fourth", "November 24"),
 ("August twenty-eighth", "August 28"), ("zero two seven", "027"), ("twenty twenty-six", "2026"),
]

META = dict(
    case="027", label="THE COLONEL EXTRADITED",
    title="Extradited: The Colonel Accused of Guarding Cocaine in Uniform",
    imgs={"still": "/home/claude/work/img/c027/crespo_still.jpg", "face": "/home/claude/work/img/c027/crespo_face.jpg"},
    mute_nat=["968690", "403639"],
    credit=("Photo: official U.S. Department of Justice image from SDNY press release 26-338 (Nov. 20, 2026), labeled as charged, not convicted. "
            "Footage: U.S. Customs and Border Protection and U.S. Coast Guard / Department of Defense video via DVIDS (public domain). ALL footage is labeled FILE FOOTAGE and is not from Bolivia and not from this case."),
    shorts=[
        dict(id="s1", note="DOJ PHOTO · CHARGED, NOT CONVICTED", lines=[2, 6], hook="30-YEAR MINIMUM<br>[ONE OF THREE COUNTS]",
             title="Colonel Accused of Holding Cocaine Meetings in Uniform", slot="15:00", template="document/photo-led trailer (DOJ release photo)",
             text="Prosecutors say a Bolivian Air Force colonel held cocaine meetings in uniform while armed subordinates stood guard. Charged, not convicted: three counts, one with a 30-year mandatory minimum. Full case on the channel."),
    ],
)
