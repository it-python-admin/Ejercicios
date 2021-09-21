fichero = open("ficheros_basico.py","r")
c = fichero.read(1)
while c!="":
    print(c,end="")
    c = fichero.read(1)
fichero.close()
print("\nFin de la lectura")
