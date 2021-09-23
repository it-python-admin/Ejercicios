import json
import urllib.request
def get_dict_from_json_file(file_name):
    with open(file_name,"r") as fichero:
        diccionario = json.load(fichero)
    return diccionario

def get_dict_from_json_url(url):    
    webUrl  = urllib.request.urlopen(url)
    data = webUrl.read()
    diccionario = json.loads(data) #Convierte directamente los bytes
    return diccionario

#Obtenemos el diccionario desde un JSON almacenado en un fichero
#datos = get_dict_from_json_file("indiana.json")
#Obtenemos el diccionario desde un JSON almacenado en una URL
datos = get_dict_from_json_url("https://it-python-admin.github.io/peliculas/indiana-last-crusade.json")

#En este punto tenemos un diccionario con la información (diccionario)
print("El director de {} es {}".format(datos["Title"],datos["Director"]))
for rating in datos["Ratings"]:
    print(f"La valoración en {rating['Source']} es {rating['Value']}")
