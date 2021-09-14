nombreFichero = input("Introduce le nombre del fichero:")
fichero = open(nombreFichero, "r")
linea = fichero.read()
while linea:
    print(linea)
    linea = fichero.read()
else:
    fichero.close()