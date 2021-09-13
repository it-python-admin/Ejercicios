"""
Nombre completo - Longitud mínima de 10 caracteres.
Año de nacimiento - Mayor de edad.
Dirección de correo electrónico - Debe tener una @.
El número de teléfono - Es numérico.
"""
import datetime as dt
anyo_actual = dt.date.today().year

nombre="Fernando Paniagua"
anyo_nacimiento=1971
email="fernandopaniagua@itti.es"
numero_telefono="55538372"

longitud_minima_nombre = len(nombre)>=10 #Validacion nombre
edad = anyo_actual-anyo_nacimiento
edad_valida = edad>=18 #Validacion edad
email_valido = "@" in email #Validacion email
telefono_valido = numero_telefono.isnumeric() #Validacion numero de telefono

#Solucion SENCILLA
"""
if longitud_minima_nombre and edad_valida and email_valido and telefono_valido:
    print("El formulario es correcto")
else:
    print("El formulario es erroneo")
"""

#Solucion ACEPTABLE
"""
if not longitud_minima_nombre:
    print("El nombre no tienen la longitud adecuada (al menos 10 caracteres)")
elif not edad_valida:
    print("Tiene que ser mayor de edad")
elif not email_valido:
    print("Tiene que introducir una dirección de correo electrónico válida")
elif not telefono_valido:
    print("El número de teléfono es incorrecto")
else:
    print("El formulario es correcto")
"""

#Solucion COMPLETA
hayError=False #Flag
if not longitud_minima_nombre:
    print("El nombre no tienen la longitud adecuada (al menos 10 caracteres)")
    hayError=True
if not edad_valida:
    print("Tiene que ser mayor de edad")
    hayError=True
if not email_valido:
    print("Tiene que introducir una dirección de correo electrónico válida")
    hayError=True
if not telefono_valido:
    print("El número de teléfono es incorrecto")
    hayError=True
if not hayError:
    print("Todo ok.")

