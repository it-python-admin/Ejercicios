def calcular_doble(numero):
    numero = numero * 2
    print("En la función, la variable numero vale",numero)

def agregar_numero(numeros):
    numeros.append(5)

def agregar_caracteres(cadena):
    cadena = cadena + "sufijo"

numero = 5
calcular_doble(numero)
print(numero)

numeros = [1,4]
agregar_numero(numeros)
print(numeros)

cadena = "prefijo-"
agregar_caracteres(cadena)
print(cadena)