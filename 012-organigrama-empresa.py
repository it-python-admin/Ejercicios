"""
UTILIZANDO LISTAS, CREAR LA SIGUIENTE ESTRUCTURA:
DOS DEPARTAMENTOS (primer dpto. 2 empleados, segundo dpto. 3 empleados)
Nombre
Empleados
Nombre
Categoría

Mostrar el segundo empleado del segundo departamento
¿Todos los empleados de todos los departamentos?
"""
empresa = []
dpto1 = []
dpto2 = []
empleados1 = []
empleados2 = []
e1 = ["Director/a","Juanra"]
e2 = ["Subdirector","Oscar"]
e3 = ["Director/a","Josefina"]
e4 = ["Gerente","Carlos"]
e5 = ["Coordinador","Victor"]
#Insertamos los departamentos a la empresa
empresa.append(dpto1)
empresa.append(dpto2)
#Asignamos el nombre al departamento
dpto1.append("Informatica")
#Asignamos los empleados al departamento
empleados1.append(e1)
empleados1.append(e2)
dpto1.append(empleados1)
#Asignamos el nombre al departamento
dpto2.append("Ventas")
#Asignamos los empleados al departamento
empleados2.append(e3)
empleados2.append(e4)
empleados2.append(e5)
dpto2.append(empleados2)
#Cambiamos el gerente del departamento de ventas
e4[1]="Antonio"
#Mostramos los datos
for departamento in empresa:
    print("*****",departamento[0],"*****")
    for empleado in departamento[1]:
        print("=======",empleado[0],":",empleado[1]) 
#Buscar la categoria profesional de un empleado
nombre_a_buscar = input("Introduce el nombre del empleado:")
for departamento in empresa:
    for empleado in departamento[1]:
        if empleado[1]==nombre_a_buscar:
            print(empleado[1],"trabaja como",empleado[0],"en el departamento de",departamento[0]) 
