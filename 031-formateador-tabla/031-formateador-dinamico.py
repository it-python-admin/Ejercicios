def abrir_fichero(nombre_fichero):
    fichero = open(nombre_fichero,"a")
    return fichero
def escribir_linea(fd, linea):
    fd.write(linea)
    fd.write("\n")
def cerrar_fichero(fd):
    fd.close()
def calcular_ancho_columnas(lista):
    long=0
    for y,k in lista.items():
        if len(str(y))>long:
            long=len(str(y))
        for i in k:
            if len(str(i))>long:
                long=len(str(i))
    return long

fd = abrir_fichero("ventas-dinamicas.txt")

titulo = "VENTAS"
OFFSET = 2
ventas = {"Lunes":(2083,38), "Martes":(10,183), "Miércoles":(-283,19), "Jueves":(2023,11), "Viernes":(10,18), "Sábado sabadete":(200,100)}    
#ventas = {"L":(2083,38), "M":(10,183), "X":(-283,19), "J":(2023,11), "V":(10,18), "S":(200,100)}    
#ventas = {"Lunes":(2083,38,1), "Martes":(10,183,2), "Miércoles":(-283,19,3)}    

linea=""
numero_items = len(ventas)
ancho_columna = calcular_ancho_columnas(ventas)+OFFSET
linea=titulo.center(numero_items*ancho_columna)
escribir_linea(fd,linea)
linea=""
filas=[]
for k,v in ventas.items():
    linea = linea+k.ljust(ancho_columna) #Generamos la cabecera con los titulos de las columnas
    #Bloque de creación de lista de listas vacías [[],[],[]]
    for ventas in range(len(v)):
        if len(filas)<len(v):#Solo se ejecuta en la primera tupla
            filas.append([])
    #Fin de bloque de creación de lista de listas vacías
    i=0
    for ventas in v:
        filas[i].append(ventas)
        i=i+1
escribir_linea(fd,linea)
for fila in filas:
    linea=""
    for cantidad in fila:
        linea=linea+str(cantidad).rjust(ancho_columna)
    escribir_linea(fd,linea)
cerrar_fichero(fd)