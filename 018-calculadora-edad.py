import datetime as dt
anyo_actual = dt.date.today().year
anyo_nacimiento = int(input("Introduce el año de nacimiento:"))
edad = anyo_actual - anyo_nacimiento
if edad>=65:
    franja="Jubilado"
elif edad>40:
    franja="Adulto"
elif edad>=18:
    franja="Joven"
else:
    franja="Menor de edad"
print("Franja:"+franja)