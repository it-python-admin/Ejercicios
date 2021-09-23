import json
diccionario =  {
  "Saturno devorando a su hijo":["Francisco de Goya",1823],
  "La condesa de Vilches": ["Federico de Madrazo",1853],
  "La tentación de San Antonio": ["Salvador Dalí",1946],
  "Retrato de Encarna y su hija":["Antonio Ortiz Echagüe",1926]
}

with open("salida-json.json","w") as fichero:
    fichero.write(json.dumps(diccionario))

contenido_json = json.dumps(diccionario)
print(type(contenido_json))
print(contenido_json)
