for i in range(0,10):
    if (i==5):
        break
    print(i)
print("A partir de aquí continua el programa")

for i in range(0,10):
    print("Antes del procesar",i)
    if (i==5):
        continue
    print("Despues de procesar",i)
print("A partir de aquí continua el programa")