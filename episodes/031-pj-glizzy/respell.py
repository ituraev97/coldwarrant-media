RS = [("Chii Wvttz","Chee Watts"),("CHII WVTTZ","Chee Watts"),("Chii","Chee"),("Wvttz","Watts"),("Jayquan","Jay-kwahn"),("McKenley","Muh-ken-lee"),("Glizzy","Gliz-zee"),
 ("Marrero","Muh-rair-oh"),("Bedford-Stuyvesant","Bed-furd Sty-vuh-sent"),("Gulotta","Guh-lot-ah"),("Tahjay","Tah-jay"),("Katharine","Kath-rin")]
def respell(t):
    for a,b in RS: t=t.replace(a,b)
    return t
