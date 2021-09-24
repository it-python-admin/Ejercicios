import json
import urllib.request
def get_dict_from_json_url(url):    
    webUrl  = urllib.request.urlopen(url)
    data = webUrl.read()
    diccionario = json.loads(data)
    return diccionario

