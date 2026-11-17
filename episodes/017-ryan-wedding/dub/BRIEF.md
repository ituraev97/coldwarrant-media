# Translation brief — COLD WARRANT 017 (Ryan Wedding) dub

Source: /home/claude/dub/017/tr/en.txt — 153 lines, one narration line per line. Output: /home/claude/dub/017/tr/<lang>.txt with EXACTLY 153 lines, same order, line N = translation of English line N. No blank lines, no numbering, no comments.

It is a voiced documentary narration (TTS reads it). The English is spoken fast; translations run longer, so write TIGHT, natural spoken narration — cut words, never facts.

Rules:
- Own natural words in the target language, no new facts, nothing lost: keep every number, date, place, name, hedge ("about", "prosecutors say", "according to", "allegedly", "reputed", "quote"), legal caveats (pleaded not guilty, presumed innocent, sanctions are not criminal charges).
- Numbers, years, money, weights: write as WORDS in the target language (no digits). Keep units as in English but you may convert pounds to kilos only where English gives both; otherwise keep the same unit (say "pounds" in the target language's word for it).
- es/pt/fr/it/de: English/foreign proper names, agencies, outlets, brands go in double square brackets so the voice reads them in English: [[FBI]], [[DEA]], [[Ryan Wedding]], [[Andrew Clark]], [[Associated Press]], [[CBC News]], [[CTV News]], [[ABC News]], [[ABC7]], [[Fox Eleven]], [[The Bureau]], [[The Dirty News]], [[WhatsApp]], [[Signal]], [[Telegram]], [[Thunder Bay]], [[Ontario]], [[Caledon]], [[Salt Lake City]], [[Kash Patel]], [[Pam Bondi]], [[Akil Davis]], [[Matthew Allen]], [[John Hurley]], [[Jim McDonnell]], [[Joseph McNally]], [[Bill Essayli]], [[Anthony Colombo]], [[Santa Ana]], [[Los Angeles]] (Spanish speakers may write Los Ángeles without brackets), [[Mercedes CLK GTR]]. Spanish/Mexican names stay in normal Spanish spelling WITHOUT brackets: Luis Benítez Alcántara, Edgar Aarón Vázquez Alvarado, Omar García Harfuch, Milton Morales, Roberto Gómez, Rafael Caro Quintero, Kiki Camarena, Naucalpan, Medellín, Cártel Nuevo Imperio, El General, Cártel de Sinaloa, Cártel Jalisco Nueva Generación, El Chapo, Pablo Escobar, Excélsior.
- ru and hi: NO brackets at all. Write every name/place/agency in the established form of that language, inflected (ru: ФБР, Управление по борьбе с наркотиками (DEA → УБН), Райан Уэддинг, Онтарио, Лос-Анджелес, Медельин, Пэм Бонди, Кэш Патель; hi: एफ़बीआई, डीईए, रायन वेडिंग, लॉस एंजेलिस, मेडेलिन, etc.).
- The English contains phonetic respellings for the English voice — restore the real spelling: "Meh-deh-yeen" = Medellín; "Beh-nee-tez Al-kahn-tah-rah" = Benítez Alcántara; "Vahz-kez" = Vázquez; "Har-fooch" = Harfuch; "Es-say-lee" = Essayli; "Now-kal-pahn" = Naucalpan; "D-E-A" = DEA; "C-L-K G-T-R" = CLK GTR.
- "Ontario International Airport, east of Los Angeles" is in California (not the Canadian province) — keep that clear.
- "Case file zero one seven." = channel tag: es "Expediente cero uno siete." pt "Arquivo zero um sete." fr "Dossier zéro un sept." it "Fascicolo zero uno sette." de "Akte null eins sieben." ru "Дело ноль один семь." hi "केस फ़ाइल शून्य एक सात।"
- "quote" before a quotation: translate naturally ("cita", "palavras dele:", «цитата:», etc.) or use a colon — keep that it is a direct quote.
- Line 109 "a rooster emoji": translate meaning (an emoji of a rooster).
- Spanish = neutral Latin American; Portuguese = Brazilian.
- Target length: no more than ~15% more syllables than the English line. If a line gets long, simplify phrasing.
When done, verify: `wc -l` = 153 and no line empty, and print the first 5 and last 5 lines.
