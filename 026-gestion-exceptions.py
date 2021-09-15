"""
Construir una lista con los números [3,8,10,23,0]
Pedir al usuario dos números entre 0 y 4.
Dividir los números que están en la lista en la posiciones indicadas.
Hay que controlar el error de número (índice) fuera de rango.
Hay que controlar el error de división entre cero.
Hay que controlar que los valores introducidos sean números.
"""
lista = [3,8,10,23,0]
try:
    n1 = int(input("Introduce el primer indice:"))
    n2 = int(input("Introduce el segundo indice:"))
    resultado = lista[n1]/lista[n2]
except ValueError:
    print ("El valor introducido no es un número entero")
except IndexError:
    print ("El indice esta fuera de rango")
except ZeroDivisionError:
    print ("Error División entre cero")
except:
    print ("Ha ocurrido un error inesperado... Contacte con el administrador")
else:
    print("Resultado:",resultado)
finally:
    print("Final del proceso")