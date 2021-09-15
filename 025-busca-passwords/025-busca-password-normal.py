import hashlib
def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    return resumen.hexdigest()

fichero = input("Introduce el nombre del fichero con las hash:")
password = input("Introduce una contraseña:")
password_hash = obtener_hash(password)
fichero = open(fichero)
current_hash = fichero.readline().replace("\n","")
while current_hash:
    if current_hash==password_hash:
        print("NO SIRVE")
        break
    current_hash = fichero.readline().replace("\n","")
else:
    print("NO PROBLEMO")
fichero.close()
