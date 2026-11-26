import re
RS = [("El Ingeniero","El In-hen-yeh-roh"),("El Inge","El In-heh"),("Otay Mesa","Oh-tie Mesa"),("Guadalajara","Gwah-dah-lah-hah-rah"),("Jalisco","Hah-lees-koh"),
 ("Tijuana","Tee-wah-nah"),("Nueva","Nway-vah"),("CJNG","C-J-N-G"),("HSI","H-S-I"),("HIDTA","Hy-dah"),("DEA","D-E-A"),("FBI","F-B-I"),("DHS","D-H-S"),("USNI","U-S-N-I"),
 ("Escalante","Ess-kah-lahn-tay"),("Coolidge","Coo-lidge")]
def respell(t):
    for a,b in RS: t=t.replace(a,b)
    return t
