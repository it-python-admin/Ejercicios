NOMBRE_FICHERO = "tabla.txt"

def abrir_fichero(nombre_fichero):
    fichero = open(nombre_fichero,"a")
    return fichero
def escribir_linea(fd, linea):
    fd.write(linea)
    fd.write("\n")
def cerrar_fichero(fd):
    fd.close()

ventas = {"Lunes":(2083,38), "Martes":(10,183), "Miércoles":(-283,19), "Jueves":(2023,11), "Viernes":(10,18)}
linea1 = "Ventas".center(50)
linea2 = ""
linea3 = ""
linea4 = ""
for k,v in ventas.items():
    linea2 = linea2+k.ljust(10)
    linea3 = linea3+str(v[0]).rjust(10)
    linea4 = linea4+str(v[1]).rjust(10)

try:
    fichero = abrir_fichero(NOMBRE_FICHERO)
    escribir_linea(fichero, linea1)
    escribir_linea(fichero, linea2)
    escribir_linea(fichero, linea3)
    escribir_linea(fichero, linea4)
    cerrar_fichero(fichero)
except:
    print("Ha ocurrido un error al escribir el fichero")