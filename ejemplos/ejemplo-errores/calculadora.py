from typing import Type


def calcular_edad(anyo_nacimiento, anyo_actual):
    #anyo_nacimiento ¿qué validaciones hay que hacer? Sea entero, 1900, anyo anterior al actual
    if type(anyo_nacimiento) is not int:
        raise TypeError
    if anyo_nacimiento<1900:
        raise ValueError
    if anyo_nacimiento>=anyo_actual:
        raise ValueError()
    if type(anyo_actual) is not int:
        raise TypeError
    #A partir de este punto valor de anyo_nacimiento puede provocar error
    edad = anyo_actual - anyo_nacimiento
    return edad

try:
    edad = calcular_edad("abc",2021)
    print("Edad:",str(edad))
except TypeError:
    print("Hay un error en los datos de entrada: los valores deben ser números enteros")
except ValueError:
    print("Hay un error en los datos de entrada: los valores deben estar dentro de los rangos aceptados")
except:
    print("Ha ocurrido un error imprevisto")



