#pip install cryptography
from cryptography.fernet import Fernet
def crear_clave():
    key = Fernet.generate_key()
    with open("clave.sec","wb") as fichero:
        fichero.write(key)
def leer_clave():
    with open("clave.sec","rb") as fichero:
        clave = fichero.read()
    return clave

def cifrar_y_guardar_texto(texto, key):
    f = Fernet(key)
    token = f.encrypt(bytes(texto,'utf-8'))
    with open("datos_cifrados.sec","bw") as fichero:
        fichero.write(token)

def leer_y_descifrar_texto(key):
    f = Fernet(key)
    with open("datos_cifrados.sec","br") as fichero:
        datos = fichero.read()
        print(f.decrypt(datos).decode('utf-8'))

#crear_clave()
key = leer_clave()
#cifrar_y_guardar_texto("Por las mañanas huele a jazmín",key)
leer_y_descifrar_texto(key)