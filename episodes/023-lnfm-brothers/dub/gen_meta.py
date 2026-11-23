# -*- coding: utf-8 -*-
import os
EP="/home/claude/coldwarrant-media/episodes/023-lnfm-brothers"
src=open(f"{EP}/youtube_description.txt",encoding="utf-8").read()
SOURCES=src.split("Sources\n",1)[1].split("\n\nFootage and images",1)[0]
CH_T=["0:00","1:04","3:59","6:27","8:49","11:11","12:54","15:23"]
L={
"es":dict(title="Hasta $8 millones por 2 hermanos que, según EE. UU., dirigen un cártel",
 p1="Washington ofrece hasta 8 millones de dólares por información sobre dos hermanos que, según fiscales de EE. UU., encabezan La Nueva Familia Michoacana. El 20 de noviembre de 2026, la Fiscalía Federal del Distrito Oeste de Texas anunció una acusación por crimen organizado (RICO) contra 21 personas, presentada en Del Rio: armas chapadas en oro, 33 armas detenidas en Eagle Pass rumbo a México, cocaína escondida en el motor de un vehículo y un choque en 2021 que dejó 8 muertos.",
 p2="Los 21 acusados están imputados, no condenados. Una acusación formal es solo una acusación: todos se presumen inocentes hasta que se demuestre su culpabilidad. Cinco están bajo custodia federal; dieciséis, incluidos los dos hermanos, siguen prófugos y se cree que están en México.",
 ch="Capítulos", chs=["Hasta $8 millones por dos hermanos","I. La Familia","II. El Pez y El Fresa","III. La ruta","IV. Armas hacia el sur","V. Carretera 277","VI. La acusación","VII. Qué significa"],
 so="Fuentes", cr="Rueda de prensa: Fiscalía Federal del Distrito Oeste de Texas, San Antonio, 20 de noviembre de 2026 (vía NTD y Forbes Breaking News). Imágenes y pruebas de la acusación: Departamento de Justicia de EE. UU. Material de archivo (dominio público, vía DVIDS; no muestra este caso): CBP, Ejército, Guardia Costera, Marina, ICE/HSI y FBI de EE. UU. La aparición de información visual del gobierno de EE. UU. no implica ni constituye respaldo.",
 cf="EXPEDIENTE 023", tags="#truecrime #fbi #cartel"),
"pt":dict(title="Até US$ 8 milhões por 2 irmãos que, segundo os EUA, comandam um cartel",
 p1="Washington oferece até 8 milhões de dólares por informações sobre dois irmãos que, segundo promotores dos EUA, lideram La Nueva Familia Michoacana. Em 20 de novembro de 2026, a Procuradoria Federal do Distrito Oeste do Texas anunciou uma acusação por crime organizado (RICO) contra 21 pessoas, apresentada em Del Rio: armas banhadas a ouro, 33 armas barradas em Eagle Pass a caminho do México, cocaína escondida no motor de um veículo e um acidente em 2021 que deixou 8 mortos.",
 p2="Os 21 réus foram acusados, não condenados. Uma acusação formal é apenas uma acusação: todos são presumidos inocentes até que se prove o contrário. Cinco estão sob custódia federal; dezesseis, incluindo os dois irmãos, estão foragidos e, acredita-se, no México.",
 ch="Capítulos", chs=["Até US$ 8 milhões por dois irmãos","I. La Familia","II. O Peixe e o Morango","III. A rota","IV. Armas rumo ao sul","V. Rodovia 277","VI. A acusação","VII. O que isso significa"],
 so="Fontes", cr="Coletiva de imprensa: Procuradoria Federal do Distrito Oeste do Texas, San Antonio, 20 de novembro de 2026 (via NTD e Forbes Breaking News). Imagens e provas da acusação: Departamento de Justiça dos EUA. Imagens de arquivo (domínio público, via DVIDS; não mostram este caso): CBP, Exército, Guarda Costeira, Marinha, ICE/HSI e FBI dos EUA. O uso de material visual do governo dos EUA não implica endosso.",
 cf="ARQUIVO 023", tags="#truecrime #fbi #cartel"),
"fr":dict(title="Jusqu'à 8 M$ pour 2 frères qui dirigeraient un cartel, selon les USA",
 p1="Washington offre jusqu'à 8 millions de dollars pour des informations sur deux frères qui, selon les procureurs américains, dirigent La Nueva Familia Michoacana. Le 20 novembre 2026, le bureau du procureur fédéral du district ouest du Texas a annoncé un acte d'accusation pour racket (RICO) visant 21 personnes, déposé à Del Rio : des armes plaquées or, 33 armes interceptées à Eagle Pass en route vers le Mexique, de la cocaïne cachée dans le moteur d'un véhicule et un accident en 2021 qui a fait 8 morts.",
 p2="Les 21 accusés sont inculpés, pas condamnés. Un acte d'accusation n'est qu'une accusation : tous sont présumés innocents jusqu'à preuve du contraire. Cinq sont détenus ; seize, dont les deux frères, sont en fuite et se trouveraient au Mexique.",
 ch="Chapitres", chs=["Jusqu'à 8 M$ pour deux frères","I. La Familia","II. Le Poisson et la Fraise","III. La filière","IV. Des armes vers le sud","V. Autoroute 277","VI. L'acte d'accusation","VII. Ce que ça change"],
 so="Sources", cr="Conférence de presse : bureau du procureur fédéral du district ouest du Texas, San Antonio, 20 novembre 2026 (via NTD et Forbes Breaking News). Images et pièces de l'acte d'accusation : ministère de la Justice des États-Unis. Images d'archives (domaine public, via DVIDS ; elles ne montrent pas cette affaire) : CBP, armée, garde côtière, marine, ICE/HSI et FBI. L'utilisation d'images du gouvernement américain n'implique aucune approbation de sa part.",
 cf="DOSSIER 023", tags="#truecrime #fbi #cartel"),
"it":dict(title="Fino a 8 mln $ per 2 fratelli che, per gli USA, guidano un cartello",
 p1="Washington offre fino a 8 milioni di dollari per informazioni su due fratelli che, secondo i procuratori americani, guidano La Nueva Familia Michoacana. Il 20 novembre 2026 la procura federale del distretto occidentale del Texas ha annunciato un atto d'accusa per associazione a delinquere (RICO) contro 21 persone, depositato a Del Rio: armi placcate d'oro, 33 armi bloccate a Eagle Pass dirette in Messico, cocaina nascosta nel motore di un veicolo e un incidente nel 2021 con 8 morti.",
 p2="I 21 imputati sono accusati, non condannati. Un atto d'accusa è solo un'accusa: tutti sono presunti innocenti fino a prova contraria. Cinque sono in custodia federale; sedici, compresi i due fratelli, sono latitanti e si ritiene si trovino in Messico.",
 ch="Capitoli", chs=["Fino a 8 milioni $ per due fratelli","I. La Familia","II. Il Pesce e la Fragola","III. La rotta","IV. Armi verso sud","V. Autostrada 277","VI. L'atto d'accusa","VII. Cosa significa"],
 so="Fonti", cr="Conferenza stampa: procura federale del distretto occidentale del Texas, San Antonio, 20 novembre 2026 (via NTD e Forbes Breaking News). Immagini e prove dell'atto d'accusa: Dipartimento di Giustizia degli Stati Uniti. Immagini d'archivio (pubblico dominio, via DVIDS; non mostrano questo caso): CBP, Esercito, Guardia costiera, Marina, ICE/HSI e FBI. La presenza di materiale visivo del governo degli Stati Uniti non implica approvazione.",
 cf="FASCICOLO 023", tags="#truecrime #fbi #cartel"),
"de":dict(title="Bis zu 8 Mio. $ für 2 Brüder, die laut USA ein Kartell führen",
 p1="Washington bietet bis zu 8 Millionen Dollar für Hinweise auf zwei Brüder, die laut US-Anklägern La Nueva Familia Michoacana anführen. Am 20. November 2026 gab die Bundesanwaltschaft für den westlichen Bezirk von Texas eine RICO-Anklage gegen 21 Personen bekannt, eingereicht in Del Rio: vergoldete Waffen, 33 Waffen auf dem Weg nach Mexiko in Eagle Pass gestoppt, Kokain im Motor eines Fahrzeugs versteckt und ein Unfall 2021 mit 8 Toten.",
 p2="Alle 21 sind angeklagt, nicht verurteilt. Eine Anklage ist nur ein Vorwurf: Alle gelten als unschuldig, bis ihre Schuld bewiesen ist. Fünf sind in Bundeshaft; sechzehn, darunter beide Brüder, sind flüchtig und halten sich vermutlich in Mexiko auf.",
 ch="Kapitel", chs=["Bis zu 8 Mio. $ für zwei Brüder","I. La Familia","II. Der Fisch und die Erdbeere","III. Die Route","IV. Waffen nach Süden","V. Highway 277","VI. Die Anklage","VII. Was es bedeutet"],
 so="Quellen", cr="Pressekonferenz: Bundesanwaltschaft für den westlichen Bezirk von Texas, San Antonio, 20. November 2026 (via NTD und Forbes Breaking News). Bilder und Beweisfotos der Anklage: US-Justizministerium. Archivmaterial (gemeinfrei, via DVIDS; zeigt nicht diesen Fall): CBP, US Army, US-Küstenwache, US Navy, ICE/HSI und FBI. Die Verwendung von Bildmaterial der US-Regierung bedeutet keine Billigung.",
 cf="FALLAKTE 023", tags="#truecrime #fbi #kartell"),
"ru":dict(title="До $8 млн за двух братьев, которых США называют главарями картеля",
 p1="Вашингтон предлагает до 8 миллионов долларов за информацию о двух братьях, которых американские прокуроры называют лидерами картеля «Новая Семья Мичоакана». 20 ноября 2026 года федеральная прокуратура Западного округа Техаса объявила об обвинении по закону RICO против 21 человека, поданном в Дель-Рио: позолоченное оружие, 33 ствола, задержанные в Игл-Пассе по пути в Мексику, кокаин, спрятанный в двигателе машины, и авария 2021 года, в которой погибли 8 человек.",
 p2="Все 21 обвиняемый лишь обвинены, а не осуждены. Обвинительное заключение — это только обвинение: все считаются невиновными, пока вина не доказана в суде. Пятеро под стражей; шестнадцать, включая обоих братьев, в розыске и, предположительно, находятся в Мексике.",
 ch="Главы", chs=["До $8 млн за двух братьев","I. «Семья»","II. Рыба и Клубника","III. Маршрут","IV. Оружие на юг","V. Шоссе 277","VI. Обвинение","VII. Что это значит"],
 so="Источники", cr="Пресс-конференция: федеральная прокуратура Западного округа Техаса, Сан-Антонио, 20 ноября 2026 года (через NTD и Forbes Breaking News). Фото и улики из обвинительного заключения: Министерство юстиции США. Архивные кадры (общественное достояние, через DVIDS; не относятся к этому делу): CBP, армия, Береговая охрана, ВМС, ICE/HSI и ФБР США. Использование визуальных материалов правительства США не означает их одобрения.",
 cf="ДЕЛО 023", tags="#truecrime #фбр #картель"),
"hi":dict(title="2 भाइयों पर 80 लाख डॉलर तक का इनाम — अमेरिका के मुताबिक़ कार्टेल सरगना",
 p1="वॉशिंगटन उन दो भाइयों के बारे में जानकारी के लिए 80 लाख डॉलर तक का इनाम दे रहा है, जिन्हें अमेरिकी अभियोजक ला नुएवा फ़ामिलिया मिचोआकाना कार्टेल का सरगना बताते हैं। 20 नवंबर 2026 को टेक्सास के पश्चिमी ज़िले के अमेरिकी अटॉर्नी कार्यालय ने डेल रियो में दायर 21 लोगों के ख़िलाफ़ RICO अभियोग की घोषणा की: सोने की परत चढ़े हथियार, ईगल पास में मेक्सिको जाते हुए रोके गए 33 हथियार, एक गाड़ी के इंजन में छिपी कोकीन, और 2021 का एक हादसा जिसमें 8 लोग मारे गए।",
 p2="सभी 21 लोगों पर सिर्फ़ आरोप हैं, उन्हें दोषी नहीं ठहराया गया है। अभियोग केवल एक आरोप है: दोष साबित होने तक सभी निर्दोष माने जाते हैं। पाँच संघीय हिरासत में हैं; दोनों भाइयों समेत सोलह फ़रार हैं और माना जाता है कि वे मेक्सिको में हैं।",
 ch="अध्याय", chs=["दो भाइयों पर 80 लाख डॉलर तक","I. ला फ़ामिलिया","II. मछली और स्ट्रॉबेरी","III. रास्ता","IV. दक्षिण की ओर हथियार","V. हाईवे 277","VI. अभियोग","VII. इसका मतलब"],
 so="स्रोत", cr="प्रेस कॉन्फ़्रेंस: टेक्सास के पश्चिमी ज़िले का अमेरिकी अटॉर्नी कार्यालय, सैन एंटोनियो, 20 नवंबर 2026 (NTD और Forbes Breaking News के ज़रिए)। अभियोग की तस्वीरें और सबूत: अमेरिकी न्याय विभाग। फ़ाइल फ़ुटेज (पब्लिक डोमेन, DVIDS के ज़रिए; यह केस नहीं): CBP, अमेरिकी सेना, कोस्ट गार्ड, नौसेना, ICE/HSI और FBI। अमेरिकी सरकार की दृश्य सामग्री के इस्तेमाल का मतलब उसका समर्थन नहीं है।",
 cf="केस फ़ाइल 023", tags="#truecrime #fbi #cartel"),
}
for k,d in L.items():
    assert len(d["title"])<=70,(k,len(d["title"]))
    os.makedirs(f"{EP}/dub/{k}",exist_ok=True)
    open(f"{EP}/dub/{k}/title.txt","w",encoding="utf-8").write(d["title"]+"\n")
    chap="\n".join(f"{t} {n}" for t,n in zip(CH_T,d["chs"]))
    desc=f"{d['p1']}\n\n{d['p2']}\n\n{d['ch']}\n{chap}\n\n{d['so']}\n{SOURCES}\n\n{d['cr']}\n\n{d['cf']}\n\n{d['tags']}\n"
    assert len(desc)<5000,(k,len(desc))
    open(f"{EP}/dub/{k}/description.txt","w",encoding="utf-8").write(desc)
    print(k,len(d["title"]),len(desc))
