# -*- coding: utf-8 -*-
import os
src=open("youtube_description.txt",encoding="utf-8").read()
SOURCES=src.split("Sources\n",1)[1].split("\n\nFootage:",1)[0]
CH_T=["0:00","1:10","2:24","3:53","4:41","6:05","7:50","9:34"]
L={
"es":dict(title="La Guardia Costera salta a un narcosubmarino en marcha: 17.000 lb",
 p1="Un equipo de abordaje de la Guardia Costera de EE. UU. salta a un narcosubmarino que sigue en movimiento, golpea la escotilla y encuentra a cinco personas y casi 17.000 libras de cocaína. Esta es la historia completa del abordaje del [[M]] del 18 de junio de 2019: quién construye estos barcos, por qué el Congreso los declaró ilegales, el desembarco de 569 millones de dólares en San Diego y las condenas.",
 p2="Es un caso de 2019, no una noticia de última hora. Los tres hombres que se declararon culpables fueron sentenciados el 18 de diciembre de 2019; en este video no se nombra a nadie más. Las imágenes del abordaje y del desembarco son video de la Guardia Costera de EE. UU. publicado por DVIDS (dominio público). Todo lo demás está marcado como MATERIAL DE ARCHIVO y no es de este abordaje.",
 chs=["El abordaje","El guardacostas Munro","Narcosubmarinos: cómo funcionan","La ley de 2008","18 de junio de 2019","El desembarco","Los tribunales","Qué significa"],
 ch="Capítulos",so="Fuentes",cf="EXPEDIENTE 024",tags="#truecrime #guardiacostera #narcosub"),
"pt":dict(title="Guarda Costeira pula em narcossubmarino em movimento: 17 mil libras",
 p1="Uma equipe de abordagem da Guarda Costeira dos EUA pula em um narcossubmarino que ainda está em movimento, bate na escotilha e encontra cinco pessoas e quase 17 mil libras de cocaína. Esta é a história completa da abordagem do [[M]] em 18 de junho de 2019: quem constrói esses barcos, por que o Congresso os tornou ilegais, o descarregamento de 569 milhões de dólares em San Diego e as condenações.",
 p2="É um caso de 2019, não uma notícia de última hora. Os três homens que se declararam culpados foram sentenciados em 18 de dezembro de 2019; ninguém mais é citado neste vídeo. As imagens da abordagem e do descarregamento são vídeo da Guarda Costeira dos EUA divulgado pelo DVIDS (domínio público). Todo o resto está marcado como IMAGEM DE ARQUIVO e não é desta abordagem.",
 chs=["A abordagem","O navio Munro","Narcossubmarinos: como funcionam","A lei de 2008","18 de junho de 2019","O descarregamento","Os tribunais","O que isso significa"],
 ch="Capítulos",so="Fontes",cf="ARQUIVO 024",tags="#truecrime #guardacosteira #narcosub"),
"fr":dict(title="Les garde-côtes sautent sur un narco-sous-marin en marche : 17 000 lb",
 p1="Une équipe d'abordage des garde-côtes américains saute sur un narco-sous-marin toujours en mouvement, frappe sur l'écoutille et trouve cinq personnes et près de 17 000 livres de cocaïne. Voici toute l'histoire de l'abordage du [[M]] du 18 juin 2019 : qui construit ces bateaux, pourquoi le Congrès les a rendus illégaux, le déchargement à 569 millions de dollars à San Diego et les condamnations.",
 p2="C'est une affaire de 2019, pas une actualité. Les trois hommes qui ont plaidé coupable ont été condamnés le 18 décembre 2019 ; personne d'autre n'est nommé dans cette vidéo. Les images de l'abordage et du déchargement sont des vidéos des garde-côtes américains publiées par DVIDS (domaine public). Tout le reste est marqué IMAGES D'ARCHIVE et ne provient pas de cet abordage.",
 chs=["L'abordage","Le patrouilleur Munro","Narco-sous-marins : comment ils fonctionnent","La loi de 2008","18 juin 2019","Le déchargement","Les tribunaux","Ce que ça change"],
 ch="Chapitres",so="Sources",cf="DOSSIER 024",tags="#truecrime #garde-cotes #narcosub"),
"it":dict(title="La Guardia Costiera salta su un narcosommergibile in corsa: 17.000 lb",
 p1="Una squadra di abbordaggio della Guardia Costiera USA salta su un narcosommergibile ancora in movimento, bussa al portello e trova cinque persone e quasi 17.000 libbre di cocaina. Questa è la storia completa dell'abbordaggio del [[M]] del 18 giugno 2019: chi costruisce queste barche, perché il Congresso le ha rese illegali, lo scarico da 569 milioni di dollari a San Diego e le condanne.",
 p2="È un caso del 2019, non una notizia dell'ultima ora. I tre uomini che si sono dichiarati colpevoli sono stati condannati il 18 dicembre 2019; nessun altro è nominato in questo video. Le immagini dell'abbordaggio e dello scarico sono video della Guardia Costiera USA diffusi da DVIDS (pubblico dominio). Tutto il resto è contrassegnato come MATERIALE DI ARCHIVIO e non riguarda questo abbordaggio.",
 chs=["L'abbordaggio","Il cutter Munro","Narcosommergibili: come funzionano","La legge del 2008","18 giugno 2019","Lo scarico","I tribunali","Cosa significa"],
 ch="Capitoli",so="Fonti",cf="FASCICOLO 024",tags="#truecrime #guardiacostiera #narcosub"),
"de":dict(title="Küstenwache springt auf fahrendes Narco-U-Boot: fast 17.000 Pfund",
 p1="Ein Enterteam der US-Küstenwache springt auf ein Narco-U-Boot, das noch fährt, hämmert auf die Luke und findet fünf Menschen und fast 17.000 Pfund Kokain. Das ist die ganze Geschichte der [[M]]-Aktion vom 18. Juni 2019: Wer solche Boote baut, warum der Kongress sie verboten hat, die Entladung im Wert von 569 Millionen Dollar in San Diego und die Urteile.",
 p2="Es ist ein Fall von 2019, keine aktuelle Meldung. Die drei Männer, die sich schuldig bekannten, wurden am 18. Dezember 2019 verurteilt; sonst wird in diesem Video niemand genannt. Die Aufnahmen vom Entern und von der Entladung sind Videos der US-Küstenwache, veröffentlicht über DVIDS (gemeinfrei). Alles andere ist als ARCHIVMATERIAL markiert und stammt nicht von diesem Einsatz.",
 chs=["Das Entern","Der Kutter Munro","Narco-U-Boote: So funktionieren sie","Das Gesetz von 2008","18. Juni 2019","Die Entladung","Die Gerichte","Was es bedeutet"],
 ch="Kapitel",so="Quellen",cf="AKTE 024",tags="#truecrime #kuestenwache #narcosub"),
"ru":dict(title="Береговая охрана запрыгнула на ходу на нарколодку: 17 000 фунтов",
 p1="Абордажная группа Береговой охраны США запрыгивает на нарколодку, которая ещё идёт, стучит по люку и находит пятерых человек и почти 17 000 фунтов кокаина. Полная история абордажа катера «Манро» 18 июня 2019 года: кто строит такие лодки, почему Конгресс их запретил, выгрузка на 569 миллионов долларов в Сан-Диего и приговоры.",
 p2="Это дело 2019 года, а не свежая новость. Трое мужчин, признавших вину, были приговорены 18 декабря 2019 года; других людей в видео не называют. Кадры абордажа и выгрузки — видео Береговой охраны США, опубликованное DVIDS (общественное достояние). Всё остальное помечено как АРХИВНЫЕ КАДРЫ и не относится к этому абордажу.",
 chs=["Абордаж","Катер «Манро»","Нарколодки: как они устроены","Закон 2008 года","18 июня 2019 года","Выгрузка","Суды","Что это значит"],
 ch="Главы",so="Источники",cf="ДЕЛО 024",tags="#truecrime #береговаяохрана #нарколодка"),
"hi":dict(title="तट रक्षक चलती नार्को सबमरीन पर कूदे: लगभग 17,000 पाउंड कोकीन",
 p1="अमेरिकी तट रक्षक की बोर्डिंग टीम एक चलती नार्को सबमरीन पर कूदती है, हैच पर ठोकती है और पाँच लोगों तथा लगभग 17,000 पाउंड कोकीन को पकड़ती है। यह 18 जून 2019 को हुई मुनरो की बोर्डिंग की पूरी कहानी है: ऐसी नावें कौन बनाता है, कांग्रेस ने उन्हें अवैध क्यों किया, सैन डिएगो में 569 मिलियन डॉलर की उतराई और सज़ाएँ।",
 p2="यह 2019 का मामला है, ताज़ा ख़बर नहीं। जिन तीन लोगों ने अपराध स्वीकार किया, उन्हें 18 दिसंबर 2019 को सज़ा सुनाई गई; इस वीडियो में किसी और का नाम नहीं लिया गया है। बोर्डिंग और उतराई की फ़ुटेज DVIDS द्वारा जारी अमेरिकी तट रक्षक का वीडियो है (सार्वजनिक डोमेन)। बाक़ी सब कुछ आर्काइव फ़ुटेज के रूप में चिह्नित है और इस बोर्डिंग का नहीं है।",
 chs=["बोर्डिंग","कटर मुनरो","नार्को सबमरीन कैसे काम करती हैं","2008 का क़ानून","18 जून 2019","उतराई","अदालतें","इसका मतलब क्या है"],
 ch="अध्याय",so="स्रोत",cf="केस फ़ाइल 024",tags="#truecrime #coastguard #narcosub"),
}
MN={"es":"Munro","pt":"Munro","fr":"Munro","it":"Munro","de":"Munro","ru":"","hi":""}
CR="Footage: U.S. Coast Guard via DVIDS (dvidshub.net) — public domain. Boarding: https://www.dvidshub.net/video/695886 · Offload: https://www.dvidshub.net/video/696129"
for l,d in L.items():
    os.makedirs(l,exist_ok=True)
    p1=d["p1"].replace("[[M]]",MN[l])
    chap="\n".join(f"{t} {n}" for t,n in zip(CH_T,d["chs"]))
    desc=f"{p1}\n\n{d['p2']}\n\n{d['ch']}\n{chap}\n\n{d['so']}\n{SOURCES}\n\n{CR}\n{d['cf']}\n\n{d['tags']}\n"
    open(f"{l}/title.txt","w",encoding="utf-8").write(d["title"]+"\n"); open(f"{l}/description.txt","w",encoding="utf-8").write(desc)
    print(l,len(d["title"]))
