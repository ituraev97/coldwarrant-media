import re
RS = [('Ojeda', 'Oh-hay-dah'), ('Sana', 'Sah-nah'), ('Eme', 'Eh-meh'), ('Muñoz', 'Moon-yohs'), ('Aguilar', 'Ah-ghee-lar'), ('Aguirre', 'Ah-gheer-ray'), ('Agustin', 'Ah-goos-teen'), ('Navarro', 'Nah-vah-roh'), ('Moreno', 'Moh-ray-noh'), ('Moriel', 'Mor-yell'), ('Birotte', 'Bih-rot-ee'), ('Essayli', 'Ess-eye-lee'), ('Rackauckas', 'Rah-kows-kus'), ('Placentia', 'Pluh-sen-shuh'), ('Calipatria', 'Cal-ih-pat-ree-uh'), ('Capistrano', 'Cap-ih-strah-noh'), ('Cardenas', 'Kar-day-nahs'), ('Valenzuela', 'Vah-len-zway-lah'), ('Velasquez', 'Veh-lahs-kez'), ('Cordova', 'Kor-doh-vah'), ('Ysrael', 'Iz-ray-el'), ('Ortiz', 'Or-teez'), ('Duarte', 'Doo-ar-tay'), ('Selna', 'Sel-nah'), ('Wilke', 'Will-kee'), ('Habra', 'Hah-bruh'), ('Lewisburg', 'Loo-iss-burg'), ('Quinones', 'Keen-yoh-nes'), ('Chino', 'Chee-noh'), ('Bernardino', 'Ber-nar-dee-noh'), ('Juan', 'Wahn'), ('Tigre', 'Tee-gray'), ('Rodriguez', 'Rod-ree-gez'), ('Deuel', 'Dool')]
def respell(t):
    for a, b in RS:
        t = re.sub(r'\b' + re.escape(a) + r'\b', b, t)
    return t
