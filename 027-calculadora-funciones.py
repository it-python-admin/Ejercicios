"""
Hacer una calculadora con funciones
Sumar dos números, Restar dos números, Multiplicar dos números, Dividir dos números
1. Sumar
2. Restar
3. Multiplicar
4. Dividir.
¿0. Salir.?
Introduce la operación que quieras realizar.
"""
def sumar(s1, s2):
    resultado = s1 + s2
    return resultado

def restar(r1, r2):
    resultado = r1 - r2
    return resultado

def multiplicar(m1, m2):
    return m1 * m2

def dividir(d1, d2):
    return d1 / d2

def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")

def gestionar_operaciones(opcion, operando1, operando2):
    if opcion == 1:
        resultado = sumar(operando1, operando2)
    elif opcion == 2:
        resultado = restar(operando1, operando2)
    elif opcion == 3:
        resultado = multiplicar(operando1, operando2)
    elif opcion == 4:
        resultado = dividir(operando1, operando2)
    return resultado

def main():
    opcion=-1
    while opcion!=0:
        mostrar_menu()
        try:
            opcion = int(input("Introduce una opción [0-4]:"))
            if opcion in (1, 2, 3, 4):
                operando1 = int(input("Introduce el primer operando:"))
                operando2 = int(input("Introduce el segundo operando:"))
                resultado = gestionar_operaciones(opcion, operando1, operando2)
                print("El resultado de la operación es", resultado)
        except:
            print("Ha ocurrido un error")

main()
print ("Fin de la ejecución")