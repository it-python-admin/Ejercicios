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
webUrl  = urllib.request.urlopen('https://www.gutenberg.org/files/2000/2000-0.txt')
texto_bruto = webUrl.read()
#SEGUNDO PUNTO
texto_bruto=str(texto_bruto)
#TERCER PUNTO
lista_palabras = texto_bruto.split()
#CUARTO PUNTO

#QUINTO PUNTO
palabra = "Anna"
if palabra in lista_palabras:
    print(palabra, "existe en el Quijote")


