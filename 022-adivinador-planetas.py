"""
Mostramos lista y pedimos planeta.
Si acierta: indicamos cuantos intentos ha realizado.
Si no acierta, se borra el planeta el planeta de la lista, se muestra la lista y se vuelve a intentar.
"""
import random
numeroIntentos = 1
lista = ["Mercurio","Venus","Marte","Jupiter","Saturno","Urano","Neptuno","Pluton"]
planeta_secreto = random.choice(lista)
print(lista)
candidato = input("Averigua en qué planeta estoy pensando:")
while candidato!=planeta_secreto:
    print("No has acertado")
    lista.remove(candidato)
    print(lista)
    candidato = input("Averigua en qué planeta estoy pensando:")
    numeroIntentos+=1
else:
    print("Enhorabuena. Eres un adivino. Lo has adivinado en",numeroIntentos,"intentos")