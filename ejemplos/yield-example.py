def calcular_dobles(parametro1, parametro2):
    resultado = parametro1
    for i in range(parametro2):
        resultado = resultado * 2
        yield resultado

print("Paso 1")
dobles = calcular_dobles(5,3)
print("Paso 2")
for d in dobles:
    print(d)
print("Paso 3")
