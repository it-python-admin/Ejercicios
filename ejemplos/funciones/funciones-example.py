def saludar_generico():
    print("Hola")
    print("Holahola")
    print("¿Qué tal estás?")

def saludar(nombre):
    print("Hola",nombre)

def dame_un_numero():
    return 2

def dame_el_doble(numero):
    return numero*2

def suma(s1, s2):
    resultado = s1 + s2
    return resultado

saludar_generico()
saludar("Fernando")
dame_un_numero() #No recogemos el valor devuelto
numero = dame_un_numero() #Recogemos el valor devuelto en una variable
saludar(dame_un_numero()) #Usamos el retorno sin asignación
doble = dame_el_doble(2)
doble_automatico = dame_el_doble(dame_un_numero())

#Hola
#holahola
#que tal estas
#Hola Fernando
#Hola 2





