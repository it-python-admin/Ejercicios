#Función zip
dias = ("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo")
planetas=("Mercurio","Venus","La Tierra","Marte","Jupiter","Saturno","Urano","Plutón")
numeros=[3,4,5,3,8,10,15,20,20,20,20,20,20]
todo_junto = zip(dias,planetas,numeros)
print(tuple(todo_junto))



"""
#Función sorted
dias = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]

def funcion_orden(elemento):
    ne = elemento.count("e")
    return ne

dias_ordenados = sorted(dias, key=funcion_orden, reverse=True)
print(dias_ordenados)
"""

"""
#Función map
#Nombre, litros de agua totales, oxigeno True
planetas = [
    ["Mercurio",100,True],
    ["Venus",2000,False],
    ["Marte",0,False],
    ["Jupiter",1000,True],
    ["Urano",1500,True]]

def convertir_a_cc(planeta):
    planeta[1]*=100
    return planeta    

#Ejecución de la función sobre cada elemento de la lista
planetas = map(convertir_a_cc, planetas)

#Visualización del resultado
planetas = list(planetas)
for p in planetas:
    print(p[0],p[1])
"""

"""
#Función filter
#Nombre, litros de agua totales, oxigeno True
planetas = (
    ("Mercurio",100,True),
    ("Venus",2000,False),
    ("Marte",0,False),
    ("Jupiter",1000,True),
    ("Urano",1500,True))

def es_habitable(planeta):
    habitable = (planeta[1]>=1000) and (planeta[2]==True)
    return habitable

planetas_habitables = filter(es_habitable, planetas)

for p in planetas_habitables:
    print(p)
"""

"""
#Función exec
def saludar():
    print("Hola a todos")
    return "OK"

def despedir():
    print("Hasta mañana")
    return "OK"

lista_funciones = ["saludar()","despedir()"]

resultado = ""
for f in lista_funciones:
    resultado = exec(f)
    print("RESULTADO:", resultado)
"""

"""
#Función eval
def saludar():
    print("Hola a todos")
    return "OK"

def despedir():
    print("Hasta mañana")
    return "OK"

lista_funciones = ["saludar()","despedir()"]

for f in lista_funciones:
    resultado = eval(f)
    print("RESULTADO:", resultado)
"""

"""
#Función callable
class Arma:
    municion = 10
    cadencia = 1
    def __init__(self,nombre):
        print("En el __init__")
        self.nombre = nombre
    def recargar(self, incremento):
        self.municion+=incremento
    def mostrar(self):
        print(self.municion)
    def disparar(self):
        print("Disparando...")
    def __call__(self):
        print("En el __call__")
        self.disparar()
        self.recargar(-1)
        self.mostrar()


ak47 = Arma("AK-47")
if callable(ak47)==True:
    ak47()
else:
    pass
"""