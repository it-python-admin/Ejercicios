"""
https://www.gutenberg.org/files/2000/2000-0.txt
1.Descargar el quijote del enlace.
2.Convertir el texto a string
3.Guardarlo en una lista (utilizando split)
4. Pedir al usuario una palabra y le vamos a decir cuantas veces aparece la palabra en el libro.
Tiene que ser independiente de si está escrito en mayúsculas o minúsculas (utilizando count de string)
5. Indicar si la palabra está o no (utilizando la lista) (utilizando in de la lista)
"""
#PRIMER PUNTO
import urllib.request
print("Leyendo URL")
webUrl  = urllib.request.urlopen('https://www.gutenberg.org/files/2000/2000-0.txt')
texto_bruto = webUrl.read()
#SEGUNDO PUNTO
print("Convirtiendo el array de bytes a texto y a mayusculas")
texto_bruto=str(texto_bruto) #convertir el array de bytes a string
texto_mayusculas = texto_bruto.upper() #convertir el texto string a mayusculas
#TERCER PUNTO
print("Obteniendo la lista de palabras")
lista_palabras = texto_mayusculas.split()
#CUARTO PUNTO
palabra_clave = input("Introduce una palabra a buscar:")
numero_apariciones = texto_mayusculas.count(palabra_clave.upper())
print("La palabra",palabra_clave,"ha aparecido",numero_apariciones,"veces")
#CUARTO PUNTO UTILIZANDO COUNT DE LA LISTA
numero_apariciones_en_lista = lista_palabras.count(palabra_clave.upper())
print("La palabra",palabra_clave,"ha aparecido",numero_apariciones_en_lista,"veces en la lista")
#QUINTO PUNTO
if palabra_clave.upper() in lista_palabras:
    print(palabra_clave, "existe en el Quijote")
else:
    print(palabra_clave, "no existe en el Quijote")