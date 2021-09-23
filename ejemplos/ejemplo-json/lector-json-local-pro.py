import json
titulo = input("Introduce título de película:")
with open(titulo+".json","r") as fichero:
    diccionario = json.load(fichero)
#En este punto tenemos un diccionario con la información (diccionario)
print("El director de {} es {}".format(diccionario["Title"],diccionario["Director"]))
for rating in diccionario["Ratings"]:
    print(f"La valoración en {rating['Source']} es {rating['Value']}")