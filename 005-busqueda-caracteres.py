frase = "En un lugar de La Mancha, La Mancha es una región"
fraseMayusculas = frase.upper()
textoABuscar = input("Introduzca el texto a buscar:")
textoABuscarMayusculas = textoABuscar.upper()
numeroOcurrencias = fraseMayusculas.count(textoABuscarMayusculas)
print("El texto",textoABuscar,"ha aparecido",numeroOcurrencias,"veces")