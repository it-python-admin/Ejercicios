import sys

def get_opcion():
    print("1. Sumar")
    print("2. Restar")
    print("0. Salir")
    opcion = input("Introduce una opcion:")
    return opcion        

while True:
    opcion = get_opcion()
    if (int(opcion)==0):
        sys.exit(0)
    elif (int(opcion)>2):
        sys.exit(-1)

    