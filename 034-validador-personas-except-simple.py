class ValidacionError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar(nombre, edad, color):
    colores_horribles = ["NARANJA"]
    if len(nombre)<3:
        raise ValidacionError("Nombre corto")
    if edad<18:
        raise ValidacionError("Menor de edad")
    if color in colores_horribles:
        raise ValidacionError("Mal gusto")

nombre = input("Introduce tu nombre:")
edad = int(input("Introduce tu edad:"))
color = (input("Introduce tu color favorito:")).upper()

try:
    validar(nombre, edad, color)
except ValidacionError as error_validacion:
    print(error_validacion)
else:
    print("Has pasado todos los filtros")