dias_de_labor = ("lunes","martes","miercoles","jueves","viernes")
dia_a_buscar = input("Introduce un dia de la semana:")
if dia_a_buscar in dias_de_labor:
    print("Ese dia es laborable")
else:
    print("Ese dia es de festivo")
for dia in dias_de_labor:
    print(dia)