#https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

import hashlib
def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    return resumen.hexdigest()

password_secreta = '136c67657614311f32238751044a0a3c0294f2a521e573afa8e496992d3786ba'
candidatas = ["baseball","football","shadow","mustang","superman","jordan","soccer"]

for candidata in candidatas:
    if (obtener_hash(candidata)==password_secreta):
        print("La contraseña es " + candidata)
        break
else:
    print("La contraseña no ha sido encontrada")
    