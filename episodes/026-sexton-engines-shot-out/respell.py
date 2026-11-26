RS = [("Cartagena","Kar-tah-hay-nah"),("Fager","Fay-ger"),("HITRON","Hy-tron"),("Colucci","Koh-loo-chee"),("USCG","U-S-C-G"),("DEA","D-E-A"),("FBI","F-B-I")]
def respell(t):
    for a,b in RS: t=t.replace(a,b)
    return t
