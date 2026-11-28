# Kokoro FALLBACK only (Chatterbox uses real spellings). Apply via the pre.py pattern of episodes/028-keefe-d.
RS = [("Godbey","God-bee"),("Raybould","Ray-bold"),("Meacham","Mee-chum"),("Toliver","Toll-ih-ver"),("Bazaldua","Bah-zahl-doo-ah"),("Calvert","Cal-vert"),
      ("Wheatley","Weet-lee"),("Hewitt","Hugh-it"),("Brantley","Brant-lee"),("Garner","Gar-ner"),("Phillis","Fill-iss"),("caiman","kay-man"),("Crips","Crips"),("K2","K-two")]
def respell(t):
    for a,b in RS: t=t.replace(a,b)
    return t
