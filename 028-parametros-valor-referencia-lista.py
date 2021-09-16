"""
Dos funciones
[x] Resolver con el paso de parámetros por referencia
[x] Resolver con el "paso de parámetros por valor" (No modificar la lista pasada como parámetro en la función)
agregar_item
	Recibe como parámetro una lista y un elemento a agregar

La versión por refencia modifica la lista original
La versión por valor hay que conseguir que modifique la lista original
"""
lista_base = [2,4,6,8,10]

def agregar_item_referencia(lista, item):
    lista.append(item)

def agregar_item_valor(lista, item):
    lista_local = lista[:]
    lista_local.append(item)
    return lista_local

agregar_item_referencia(lista_base,12)
print(lista_base)
lista_base = agregar_item_valor(lista_base,14)
print(lista_base)