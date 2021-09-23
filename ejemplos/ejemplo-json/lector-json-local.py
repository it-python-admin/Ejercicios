import json
titulo = input("Introduce título de película:")
texto_plano=""
with open(titulo+".json","r") as fichero:
    linea = fichero.readline()
    while linea!="":
        texto_plano+=linea
        linea = fichero.readline()
#En este punto tenemos un str que contiene el json en texto_plano
diccionario = json.loads(texto_plano)
#En este punto tenemos un diccionario con la información (diccionario)
print("El director de {} es {}".format(diccionario["Title"],diccionario["Director"]))
for rating in diccionario["Ratings"]:
    print(f"La valoración en {rating['Source']} es {rating['Value']}")