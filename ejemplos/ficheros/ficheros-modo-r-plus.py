fichero = open("datos.txt","r+")
linea = fichero.readline()
print("Linea 1:"+linea)
fichero.write("Nueva linea")
fichero.flush()
fichero.seek(0+len(linea)+1)
linea2 = fichero.readline()
print("Linea 2:"+linea2+":")
fichero.write("Nueva linea 2")
fichero.close()