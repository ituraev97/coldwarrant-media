import re
RS = [("Sekyiwa","Seh-kee-wah"),("Palal","Pah-lahl"),("Binu","Bih-noo"),("DiGiacomo","Dee-Jah-koh-moh"),("Kierny","Keer-nee"),("Carli","Kar-lee"),
 ("Kading","Kay-ding"),("Suge","Shoog"),("Koval","Koh-vahl"),("Seldon","Sel-don"),("Keefe","Keef"),("Tupac","Too-pahk"),("Mopreme","Moh-preem"),("Biggie","Biggy"),
 ("DeAndre","Dee-Ahn-dray"),("Wolfson","Wulf-son"),("Sanft","Sanft"),("Compton","Komp-ton"),("Vibe","Vibe"),("Henderson","Hen-der-son")]
def respell(t):
    for a,b in RS: t=t.replace(a,b)
    return t
