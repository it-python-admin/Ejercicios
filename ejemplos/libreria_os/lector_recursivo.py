import os
def get_contenido(ruta):
    try:
        contenido = os.listdir(ruta)
        for c in contenido:
            c=ruta+"/"+c
            if os.path.isdir(c):
                get_contenido(c)
            else:
                if c.endswith(".jpg"):
                    print(c)
    except PermissionError:
        pass
get_contenido("D:/")