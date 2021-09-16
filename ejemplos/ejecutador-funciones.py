def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")

def ejecutador(*funciones_ejecutables):
    for f in funciones_ejecutables:
        f()

ejecutador(f1,f2,f3,f2,f1,f3,f2)