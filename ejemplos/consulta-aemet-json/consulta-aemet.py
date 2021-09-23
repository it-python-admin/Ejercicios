API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpdC5weXRob24uMjAyMS4wOUBnbWFpbC5jb20iLCJqdGkiOiJmMGEwNDAxYS1mZTdkLTRkYmEtODI2YS1hNjNjMjM5YjAzMjgiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTYzMjQyMjYyNCwidXNlcklkIjoiZjBhMDQwMWEtZmU3ZC00ZGJhLTgyNmEtYTYzYzIzOWIwMzI4Iiwicm9sZSI6IiJ9.2cSUT3ZyQBb_vQy04u___I4j4aJ0itV-_lxQua0qgMw"
import json
import urllib.request 
def get_dict_from_json_url(url):    
    webUrl  = urllib.request.urlopen(url)
    data = webUrl.read()
    diccionario = json.loads(data) #Convierte directamente los bytes
    return diccionario

fecha_inicio="2021-09-01"
fecha_final="2021-09-03"
url = ("https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{fecha_ini}T00:00:00UTC/fechafin/{fecha_fin}T23:59:59UTC/estacion/3195/?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpdC5weXRob24uMjAyMS4wOUBnbWFpbC5jb20iLCJqdGkiOiJmMGEwNDAxYS1mZTdkLTRkYmEtODI2YS1hNjNjMjM5YjAzMjgiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTYzMjQyMjYyNCwidXNlcklkIjoiZjBhMDQwMWEtZmU3ZC00ZGJhLTgyNmEtYTYzYzIzOWIwMzI4Iiwicm9sZSI6IiJ9.2cSUT3ZyQBb_vQy04u___I4j4aJ0itV-_lxQua0qgMw").format(fecha_ini=fecha_inicio, fecha_fin=fecha_final)

macro_datos = get_dict_from_json_url(url)
url_datos = macro_datos["datos"]
datos = get_dict_from_json_url(url_datos)
print(datos)

"""
{
  "descripcion" : "exito",
  "estado" : 200,
  "datos" : "https://opendata.aemet.es/opendata/sh/c62ec6c2",
  "metadatos" : "https://opendata.aemet.es/opendata/sh/b3aa9d28"
}
"""