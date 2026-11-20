# -*- coding: utf-8 -*-
import os
EP = "/home/claude/coldwarrant-media/episodes/021-aryan-brotherhood"
src = open(f"{EP}/youtube_description.txt", encoding="utf-8").read()
SOURCES = src.split("Sources\n", 1)[1].split("\n\nFootage:", 1)[0]
CH_T = ["0:00", "0:54", "2:39", "4:31", "6:23", "7:40", "8:59", "10:34", "13:07", "16:07"]
L = {
"es": dict(title="Jefe de la Hermandad Aria traficaba heroína desde su celda: la DEA oía",
 p1="Un líder de la Hermandad Aria ([[Aryan Brotherhood]]) dirigía el tráfico de heroína y metanfetamina desde su celda con teléfonos de contrabando, y la DEA lo estaba escuchando. La historia de la pandilla carcelaria, de Ronald \"Renegade\" Yandell, de las escuchas de la DEA y de los casos federales RICO que llevaron a sus líderes a cadena perpetua: desde San Quentin hacia 1964 hasta el doble asesinato de Lomita, ordenado desde una prisión, cuyo pistolero será sentenciado el 23 de noviembre de 2026.",
 p2="Cinco acusados del caso de Fresno siguen esperando juicio: están acusados, no condenados, y se les presume inocentes hasta que se demuestre su culpabilidad en un tribunal.",
 ch="Capítulos", chs=["Dos hombres, una orden desde una celda", "I. La Marca", "II. Los teléfonos", "III. Renegade", "IV. Las órdenes", "V. Las escuchas", "VI. La redada", "VII. El veredicto", "VIII. Las nuevas órdenes", "IX. El lunes"],
 so="Fuentes", cr="Imágenes: Ejército, Guardia Nacional, Fuerza Aérea y Armada de EE. UU., ICE/HSI y CBP vía DVIDS — dominio público. Todo es MATERIAL DE ARCHIVO: no muestra estos casos ni a ninguna persona mencionada. La aparición de información visual del gobierno de EE. UU. no implica ni constituye respaldo. Narración: voz sintética.",
 cf="EXPEDIENTE 021", tags="#truecrime #hermandadaria #prisiones"),
"pt": dict(title="Chefe da Irmandade Ariana traficava heroína da cela, e a DEA ouvia",
 p1="Um líder da Irmandade Ariana ([[Aryan Brotherhood]]) comandava o tráfico de heroína e metanfetamina de dentro da cela com celulares contrabandeados, e a DEA estava ouvindo. A história da gangue prisional, de Ronald \"Renegade\" Yandell, das escutas da DEA e dos processos federais RICO que levaram seus líderes à prisão perpétua: de San Quentin, por volta de 1964, até o duplo homicídio de Lomita, ordenado de dentro de um presídio, cujo atirador será sentenciado em 23 de novembro de 2026.",
 p2="Cinco réus do caso de Fresno ainda aguardam julgamento: são acusados, não condenados, e presumidos inocentes até que a culpa seja provada na Justiça.",
 ch="Capítulos", chs=["Dois homens, uma ordem vinda de uma cela", "I. A Marca", "II. Os celulares", "III. Renegade", "IV. As ordens", "V. A escuta", "VI. A operação", "VII. O veredicto", "VIII. As novas ordens", "IX. Segunda-feira"],
 so="Fontes", cr="Imagens: Exército, Guarda Nacional, Força Aérea e Marinha dos EUA, ICE/HSI e CBP via DVIDS — domínio público. Tudo é IMAGEM DE ARQUIVO: não mostra estes casos nem nenhuma pessoa citada. O uso de material visual do governo dos EUA não implica endosso. Narração: voz sintética.",
 cf="ARQUIVO 021", tags="#truecrime #irmandadeariana #prisao"),
"fr": dict(title="Fraternité aryenne : un chef dealait de l'héroïne depuis sa cellule",
 p1="Un chef de la Fraternité aryenne ([[Aryan Brotherhood]]) dirigeait un trafic d'héroïne et de méthamphétamine depuis sa cellule avec des téléphones de contrebande — et la DEA écoutait. L'histoire du gang carcéral, de Ronald « Renegade » Yandell, des écoutes de la DEA et des procès fédéraux RICO qui ont envoyé ses chefs en prison à perpétuité : de San Quentin vers 1964 jusqu'au double meurtre de Lomita, ordonné depuis une prison, dont le tireur doit connaître sa peine le 23 novembre 2026.",
 p2="Cinq accusés du dossier de Fresno attendent encore leur procès : ils sont accusés, pas condamnés, et présumés innocents jusqu'à ce que leur culpabilité soit prouvée devant un tribunal.",
 ch="Chapitres", chs=["Deux hommes, un ordre venu d'une cellule", "I. La Marque", "II. Les téléphones", "III. Renegade", "IV. Les ordres", "V. Les écoutes", "VI. Le coup de filet", "VII. Le verdict", "VIII. Les nouveaux ordres", "IX. Lundi"],
 so="Sources", cr="Images : armée, garde nationale, armée de l'air et marine américaines, ICE/HSI et CBP via DVIDS — domaine public. Tout est IMAGES D'ARCHIVE : elles ne montrent ni ces affaires ni aucune personne citée. L'utilisation d'images du gouvernement américain n'implique aucune approbation. Narration : voix de synthèse.",
 cf="DOSSIER 021", tags="#truecrime #fraternitearyenne #prison"),
"it": dict(title="Boss della Fratellanza Ariana spacciava dalla cella: la DEA ascoltava",
 p1="Un capo della Fratellanza Ariana ([[Aryan Brotherhood]]) gestiva un traffico di eroina e metanfetamina dalla sua cella con telefoni di contrabbando, e la DEA ascoltava. La storia della gang carceraria, di Ronald \"Renegade\" Yandell, delle intercettazioni della DEA e dei processi federali RICO che hanno mandato i suoi capi all'ergastolo: da San Quentin intorno al 1964 fino al duplice omicidio di Lomita, ordinato da un carcere, il cui killer conoscerà la pena il 23 novembre 2026.",
 p2="Cinque imputati del caso di Fresno sono ancora in attesa di processo: sono accusati, non condannati, e presunti innocenti fino a prova contraria in tribunale.",
 ch="Capitoli", chs=["Due uomini, un ordine da una cella", "I. Il Marchio", "II. I telefoni", "III. Renegade", "IV. Gli ordini", "V. Le intercettazioni", "VI. La retata", "VII. Il verdetto", "VIII. I nuovi ordini", "IX. Lunedì"],
 so="Fonti", cr="Immagini: Esercito, Guardia Nazionale, Aeronautica e Marina degli Stati Uniti, ICE/HSI e CBP via DVIDS — pubblico dominio. Tutto è MATERIALE D'ARCHIVIO: non mostra questi casi né alcuna persona citata. La presenza di materiale visivo del governo USA non implica approvazione. Narrazione: voce sintetica.",
 cf="FASCICOLO 021", tags="#truecrime #fratellanzaariana #carcere"),
"de": dict(title="Arische Bruderschaft: Boss dealte aus der Zelle – die DEA hörte mit",
 p1="Ein Anführer der Arischen Bruderschaft ([[Aryan Brotherhood]]) steuerte mit geschmuggelten Handys aus seiner Zelle einen Heroin- und Meth-Handel – und die DEA hörte mit. Die Geschichte der Gefängnisgang, von Ronald \"Renegade\" Yandell, den DEA-Abhörmaßnahmen und den RICO-Bundesverfahren, die ihre Anführer lebenslang hinter Gitter brachten: von San Quentin um 1964 bis zum Doppelmord von Lomita, befohlen aus einem Gefängnis, dessen Schütze am 23. November 2026 sein Strafmaß erhalten soll.",
 p2="Fünf Angeklagte im Fresno-Verfahren warten noch auf ihren Prozess: Sie sind angeklagt, nicht verurteilt, und gelten als unschuldig, bis ihre Schuld vor Gericht bewiesen ist.",
 ch="Kapitel", chs=["Zwei Männer, ein Befehl aus der Zelle", "I. Die Marke", "II. Die Handys", "III. Renegade", "IV. Die Befehle", "V. Die Abhöraktion", "VI. Der Zugriff", "VII. Das Urteil", "VIII. Die neuen Befehle", "IX. Montag"],
 so="Quellen", cr="Aufnahmen: US Army, Nationalgarde, US Air Force, US Navy, ICE/HSI und CBP via DVIDS – gemeinfrei. Alles ist ARCHIVMATERIAL: Es zeigt weder diese Fälle noch genannte Personen. Die Verwendung von Bildmaterial der US-Regierung bedeutet keine Billigung. Sprecher: synthetische Stimme.",
 cf="AKTE 021", tags="#truecrime #arischebruderschaft #gefängnis"),
"ru": dict(title="Главарь «Арийского братства» торговал героином из камеры. УБН слушало",
 p1="Лидер тюремной банды «Арийское братство» руководил торговлей героином и метамфетамином прямо из своей камеры по контрабандным телефонам — а УБН (DEA) его слушало. История банды, Рональда «Ренегата» Янделла, прослушки УБН и федеральных дел по закону РИКО, отправивших её лидеров за решётку пожизненно: от Сан-Квентина около 1964 года до двойного убийства в Ломите, приказ о котором отдали из тюрьмы; приговор стрелку должны огласить 23 ноября 2026 года.",
 p2="Пятеро обвиняемых по делу из Фресно ещё ждут суда: им предъявлены обвинения, они не осуждены и считаются невиновными, пока их вина не доказана в суде.",
 ch="Главы", chs=["Двое мужчин, один приказ из камеры", "I. «Бренд»", "II. Телефоны", "III. «Ренегат»", "IV. Приказы", "V. Прослушка", "VI. Облава", "VII. Приговор", "VIII. Новые приказы", "IX. Понедельник"],
 so="Источники", cr="Видео: армия, Национальная гвардия, ВВС и ВМС США, ICE/HSI и CBP через DVIDS — общественное достояние. Все кадры — АРХИВНЫЕ (FILE FOOTAGE): на них нет этих дел и упомянутых людей. Использование материалов правительства США не означает их одобрения. Озвучка: синтезированный голос.",
 cf="ДЕЛО 021", tags="#truecrime #арийскоебратство #тюрьма"),
"hi": dict(title="आर्यन ब्रदरहुड बॉस जेल की कोठरी से हेरोइन बेचता था — डीईए सुन रही थी",
 p1="आर्यन ब्रदरहुड जेल गिरोह का एक सरगना तस्करी किए गए फ़ोनों से अपनी कोठरी से हेरोइन और मेथ का धंधा चलाता था — और डीईए सुन रही थी। गिरोह की कहानी, रोनाल्ड \"रेनेगेड\" यांडेल, डीईए की वायरटैपिंग और उन संघीय RICO मुक़दमों की कहानी जिन्होंने इसके सरगनाओं को उम्रक़ैद दिलाई: 1964 के आसपास सैन क्वेंटिन से लेकर लोमिटा के दोहरे हत्याकांड तक, जिसका आदेश जेल से दिया गया था; बंदूकधारी को 23 नवंबर 2026 को सज़ा सुनाई जानी है।",
 p2="फ़्रेस्नो मामले के पाँच आरोपी अभी मुक़दमे का इंतज़ार कर रहे हैं: उन पर आरोप हैं, वे दोषी नहीं ठहराए गए हैं और अदालत में दोष साबित होने तक निर्दोष माने जाते हैं।",
 ch="अध्याय", chs=["दो आदमी, कोठरी से एक आदेश", "I. 'ब्रैंड'", "II. फ़ोन", "III. रेनेगेड", "IV. आदेश", "V. वायरटैप", "VI. छापेमारी", "VII. फ़ैसला", "VIII. नए आदेश", "IX. सोमवार"],
 so="स्रोत", cr="फ़ुटेज: अमेरिकी सेना, नेशनल गार्ड, वायुसेना और नौसेना, ICE/HSI और CBP, DVIDS के ज़रिए — पब्लिक डोमेन। सारी फ़ुटेज फ़ाइल फ़ुटेज है: इसमें ये मामले या नामित लोग नहीं हैं। अमेरिकी सरकार की दृश्य सामग्री के उपयोग का अर्थ समर्थन नहीं है। आवाज़: सिंथेटिक।",
 cf="केस फ़ाइल 021", tags="#truecrime #aryanbrotherhood #prison"),
}
for k, d in L.items():
    assert len(d["title"]) <= 70, (k, len(d["title"]))
    od = f"{EP}/dub/{k}"; os.makedirs(od, exist_ok=True)
    open(f"{od}/title.txt", "w", encoding="utf-8").write(d["title"] + "\n")
    p1 = d["p1"].replace("[[", "").replace("]]", "")
    chs = "\n".join(f"{t} {c}" for t, c in zip(CH_T, d["chs"]))
    body = f"{p1} {d['tags']}\n\n{d['p2']}\n\n{d['ch']}\n{chs}\n\n{d['so']}\n{SOURCES}\n\n{d['cr']}\n\n{d['cf']} · COLD WARRANT"
    open(f"{od}/description.txt", "w", encoding="utf-8").write(body + "\n")
    print(k, len(d["title"]), len(body))
