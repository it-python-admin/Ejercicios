#pip install beautifulsoup4
#pip install win10toast
import urllib.request
from win10toast import ToastNotifier
from bs4 import BeautifulSoup #Analizador HTML y XML
import time

precio_inicial = 0
URL="https://coinmarketcap.com/coins/"

url_concurrencies="https://coinmarketcap.com/currencies/"

def show_toast(mensaje):
    toaster = ToastNotifier()
    toaster.show_toast("¡Atención!", mensaje)

def get_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})#Para evitar error 403
    conexion = urllib.request.urlopen(req)
    html_code = conexion.read()
    conexion.close()
    return html_code

def get_monedas_y_precios(data):
    page_soup = BeautifulSoup(data, "html.parser")
    moneda = page_soup.find("h2",{"class":"sc-1q9q90x-0 jCInrl h1"})
    precio = page_soup.find("div",{"class":"priceValue"})
    return (moneda, precio)

while True:
    moneda = (input("Introduce moneda:")).upper()
    codigo = (get_url(URL)).upper()
    page_soup = BeautifulSoup(codigo, "html.parser")
    monedas_candidatas = page_soup.body.findAll(text=moneda)
    if len(monedas_candidatas)==0:
        print("No hay ninguna moneda candidata. Prueba de nuevo.")
    else:
        moneda_candidata = monedas_candidatas[0]
        print("La moneda candidata es:",moneda_candidata)
        continuar = (input("¿Deseas continuar (s/n)?")).upper()
        if (continuar=="S"):
            url_concurrencies+=moneda_candidata.replace(" ","-")
            break

print(url_concurrencies)
incremento_positivo = float(input("Introduce diferencia de alarma de subida (%):"))
incremento_negativo = float(input("Introduce diferencia de alarma de bajada (-%):"))
pausa = int(input("Introduce tiempo entre muestras (segundos):"))

while True:
    data = get_url(url_concurrencies)
    monedas_y_precios = get_monedas_y_precios(data)
    if (precio_inicial==0):
        precio_inicial=float(monedas_y_precios[1].text[1:].replace(",",""))
        print(("Precio inicial ({}):${}").format(moneda_candidata, str(precio_inicial)))
        continue
    precio_actual = float(monedas_y_precios[1].text[1:].replace(",",""))
    diferencia_precio = (precio_actual-precio_inicial)
    pct_diferencia = diferencia_precio*100/precio_inicial
    print(("Precio actual ({}):${}:{}%").format(moneda_candidata, str(precio_actual), round(pct_diferencia,2)))
    if (pct_diferencia > incremento_positivo):
        show_toast("Aviso de subida: {} % de subida".format(str(round(pct_diferencia,2))))
    elif (pct_diferencia < incremento_negativo):
        show_toast("Aviso de bajada: {} % de bajada".format(str(round(pct_diferencia,2))))
    time.sleep(pausa)#Pausa de 'pausa' segundos