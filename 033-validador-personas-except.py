class NombreCortoError(Exception):
    pass

class EdadInsuficienteError(Exception):
    pass

class MalGustoError(Exception):
    pass

def validar(nombre, edad, color):
    colores_horribles = ["NARANJA"]
    if len(nombre)<3:
        raise NombreCortoError()
    if edad<18:
        raise EdadInsuficienteError()
    if color in colores_horribles:
        raise MalGustoError()

nombre = input("Introduce tu nombre:")
edad = int(input("Introduce tu edad:"))
color = (input("Introduce tu color favorito:")).upper()

try:
    validar(nombre, edad, color)
except NombreCortoError:
    print("El nombre no es suficientemente largo")
except EdadInsuficienteError:
    print("No se admiten menores de edad")
except MalGustoError:
    print("Tienes un gusto pésimo para los colores")
else:
    print("Has pasado todos los filtros")