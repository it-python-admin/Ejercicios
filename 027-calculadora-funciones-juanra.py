def sumar(s1, s2):
    resultado = s1 + s2
    return resultado

def restar(r1, r2):
    resultado = r1 - r2
    return resultado

def multiplicar(m1, m2):
    resultado = m1 * m2
    return resultado

def dividir(d1, d2):
    resultado = d1 / d2
    return resultado

calculadora = {
    "1":("Sumar",sumar), 
    "2":("Restar",restar),
    "3":("Multiplicar",multiplicar),
    "4":("Dividir",dividir),
    "0":("Salir",)}

opcion = -1
while opcion!=0:
    for opcion_menu in calculadora:
        print(opcion_menu+":"+calculadora[opcion_menu][0])
    opcion = input("Introduce una opcion:")
    if opcion=="0":
        break
    operando1 = float(input("Operando 1:"))
    operando2 = float(input("Operando 2:"))
    resultado = calculadora[opcion][1](operando1, operando2)
    print("Resultado:",resultado)
