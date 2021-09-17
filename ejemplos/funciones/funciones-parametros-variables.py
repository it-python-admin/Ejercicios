def funcion1(parametro1, *items):
    print("**************")
    for item in items:
        print(str(item))

funcion1(1)
funcion1(1,"Palabra","Termino")
funcion1(1,"Palabra","Termino","Empleado")
funcion1(1,"Palabra","Termino","Empleado",["Item1","Item2"])

def funcion2(parametro1=3, *items):
    print("**************")
    for item in items:
        print(str(item))

funcion2()
funcion2(1)
funcion2(1,"Palabra","Termino")
funcion2(1,"Palabra","Termino","Empleado")
funcion2(1,"Palabra","Termino","Empleado",["Item1","Item2"])

def funcion3(*items):
    print("**************")
    for item in items:
        print(str(item))

funcion3()
funcion3(1)
funcion3(1,"Palabra","Termino")
funcion3(1,"Palabra","Termino","Empleado")
funcion3(1,"Palabra","Termino","Empleado",["Item1","Item2"])