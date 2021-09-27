from typing import Type

class AnyoNacimientoError(Exception):
    pass

class AnyoNacimientoNoCreibleError(Exception):
    def __init__(self):
        self.mensaje="Ningún humano vivo en este momento puede nacer después del momento actual"
        super().__init__(self.mensaje)
    def solucionar(self):
        print("Solucionando...")


def calcular_edad(anyo_nacimiento, anyo_actual):
    #anyo_nacimiento ¿qué validaciones hay que hacer? Sea entero, 1900, anyo anterior al actual
    if type(anyo_nacimiento) is not int:
        raise TypeError
    if anyo_nacimiento<1900:
        raise AnyoNacimientoError
    if anyo_nacimiento>=anyo_actual:
        raise AnyoNacimientoNoCreibleError()
    if type(anyo_actual) is not int:
        raise TypeError
    #A partir de este punto valor de anyo_nacimiento puede provocar error
    edad = anyo_actual - anyo_nacimiento
    return edad

try:
    edad = calcular_edad(2022,2021)
    print("Edad:",str(edad))
except TypeError:
    print("Hay un error en los datos de entrada: los valores deben ser números enteros")
except ValueError:
    print("Hay un error en los datos de entrada: los valores deben estar dentro de los rangos aceptados")
except AnyoNacimientoError:
    print("El anyo de nacimiento no puede ser inferior a 1900")
except AnyoNacimientoNoCreibleError as annce:
    print("Error:"+annce.mensaje)
    annce.solucionar()
except:
    print("Ha ocurrido un error imprevisto")



