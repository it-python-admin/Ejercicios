def procesar(linea):
    print(linea)

#Lectura línea a línea
def procesar_fichero(nombre_fichero):
    with open(nombre_fichero,"r") as fichero:
        linea = fichero.readline().replace("\n","")
        while linea!="":
            procesar(linea)
            linea = fichero.readline().replace("\n","")

"""
#Lectura del fichero completo, devuelve una lista de str con cada línea
def procesar_fichero(nombre_fichero):
    with open(nombre_fichero,"r") as fichero:
        contenido = fichero.readlines()
        print(contenido)
"""

procesar_fichero("lectura-linea-a-linea.py")