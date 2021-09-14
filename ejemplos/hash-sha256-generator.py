import hashlib
def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    return resumen.hexdigest()

ficheroEntrada = input("Introduce el nombre del fichero de contraseñas en claro:")
ficheroSalida = input("Introduce el nombre del fichero de salida de los hash:")

fRead = open(ficheroEntrada,"r")
fOut = open(ficheroSalida,"w")

pwd=fRead.readline()
while pwd:
    pwdHash = obtener_hash(pwd)
    fOut.write(pwdHash)
    fOut.write("\n")
    pwd=fRead.readline()
fRead.close()
fOut.close()