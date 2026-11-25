import re
RS = [("Tumaco","Too-mah-koh"),("Estramonte","Ess-trah-mon-tay"),("Chavez-Aguirre","Chah-vez Ah-gee-ray"),("Caicedo Asprilla","Kai-say-doh Ahs-pree-yah"),
 ("Hurtado Vallecilla","Oor-tah-doh Vah-yeh-see-yah"),("Giraldo Santa","Hee-rahl-doh Sahn-tah"),("Quintero Rengifo","Keen-teh-roh Ren-hee-foh"),
 ("HITRON","Hy-tron"),("USNI","U-S-N-I"),("DEA","D-E-A"),("FBI","F-B-I"),("Alexander","Alexander")]
def respell(t):
    for a,b in RS: t=t.replace(a,b)
    return t
