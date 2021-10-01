import urllib.request
from bs4 import BeautifulSoup #Analizador HTML y XML

def get_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})#Para evitar error 403
    conexion = urllib.request.urlopen(req)
    html_code = conexion.read()
    conexion.close()
    return html_code

def get_listado_entidades(data):
    page_soup = BeautifulSoup(data, "html.parser")
    elementos = page_soup.findAll("td",{"class":"tdOrganoContratacionBusqPerfil"})
    return elementos

url = "https://contrataciondelestado.es/wps/portal/!ut/p/b0/04_Sj9CPykssy0xPLMnMz0vMAfIjU1JTC3Iy87KtClKL0jJznPPzSooSSxLzSlL1w_Wj9KNKkzKTE5OByv2L0hPzgGz9SLfgzJSy8gwTVYNkX1v9gtxcRwDgNu--/"
html = get_url(url)
elementos = get_listado_entidades(html)

for e in elementos:
    entidad = e.find("span").text
    print(entidad)
