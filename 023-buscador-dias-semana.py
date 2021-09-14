dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
diaBuscado = input("Introduce un dia de la semana:")
for dia in dias:
    if dia==diaBuscado:
        print("Es el",dia.capitalize())
        break
    else:
        print(dia.capitalize(),"no es")