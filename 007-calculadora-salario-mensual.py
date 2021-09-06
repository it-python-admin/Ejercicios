salarioBruto = input("Introduce tu salario anual:")
if salarioBruto.isdigit()==True:
    salarioBruto = int(salarioBruto)
    pagas = int(input("Introduce el número de pagas(12/14):"))
    salarioMensual = salarioBruto / pagas
    print("Tu salario mensual es ", salarioMensual, "€ en", pagas, "pagas")
elif salarioBruto[0]=="-":
    print("EL SALARIO BRUTO NO PUEDE SER NEGATIVO")
else:
    print("EL SALARIO BRUTO ES ERRONEO")