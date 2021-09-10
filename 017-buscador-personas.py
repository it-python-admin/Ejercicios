"""
ESTRUCTURA CON 5 ELEMENTOS
Fernando, 1971, Francisco, 1988, Javier, 1990, Jose, 1973, Federica, 1999
Nombre
	-- Año de nacimiento
	-- Ciudad de nacimiento

Introducir primera letra del nombre
Año de nacimiento

Mostrar todos los items cuya letra coincida con la introducida y hayan nacido antes del año indicado

F, 1980 --> Fernando
F, 1990 --> Fernando y Francisco
F, 2000 --> Fernando, Francisco y Federica
"""
personas = [
    ["Fernando",1971,"Madrid"],
    ["Francisco",1988,"Badajoz"],
    ["Javier",1990,"Tarragona"],
    ["Jose",1973,"Guadalajara"],
    ["Federica",1999,"Lugo"]
    ]
inicial = input("Introduce inicial:")
edad = int(input("Introduce edad:"))
for persona in personas:
    if (persona[0][0]==inicial):#BUSCAR UN MÉTODO DE str QUE ME DIGA SI LA CADENA EMPEZA POR UNA LETRA DETERMINADA
        print(persona[0])
#PENDIENTE DE TERMINAR
