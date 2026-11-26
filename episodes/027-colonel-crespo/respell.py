import re
RS = [("Cuatro Canadas","Kwah-troh Kah-nyah-dahs"),("Crespo-Guzman","Cress-poh Goos-mahn"),("Crespo","Cress-poh"),("Davila Perez","Dah-vee-lah Peh-res"),("Davila","Dah-vee-lah"),
 ("Viru Viru","Vee-roo Vee-roo"),("Sucre","Soo-kreh"),("Marrero","Mah-rare-oh"),("FELCN-GIOE","F-E-L-C-N G-I-O-E"),("FELCN","Fell-kin"),
 ("El Deber","El Deh-ber"),("El Diario","El Dee-ah-ree-oh"),("Paz","Pahs"),("Morales","Moh-rah-les"),("Cote","Coat"),("DEA","D-E-A"),("HSI","H-S-I")]
def respell(t):
    for a,b in RS: t=t.replace(a,b)
    return t
