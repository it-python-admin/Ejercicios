try:
    fichero_datos = open("datos.txt","r")
    texto = fichero_datos.read(512)
    print(texto)
    if fichero_datos.closed == True:
        fichero_datos.close()
except FileNotFoundError:
    print("Error el fichero no existe")
except IOError:
    print("Error en la escritura")