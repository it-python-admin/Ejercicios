"""
Mostramos lista y pedimos planeta.
Si acierta: indicamos cuantos intentos ha realizado.
Si no acierta, se borra el planeta el planeta de la lista, se muestra la lista y se vuelve a intentar.
"""
import random
lista = ["Mercurio","Venus","Marte","Jupiter","Saturno","Urano","Neptuno","Pluton"]
planeta_secreto = random.choice(lista)
print(lista)
