#Errores posibles
#Que no ponga un numero. ValueError
#Que ponga un numero fuera de rango. IndexError:
dias_laborales = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
try:
    numero = int(input("Introduce numero de la semana:"))
    print("El dia de la semana elegido es ", dias_laborales[numero])
except ValueError:
    print("Ha ocurrido un error. El número introducido no es un número")
except IndexError:
    print("Ha ocurrido un error. El índice introducido está fuera de rango")
except:
    print("Ha ocurrido un erro y no sé cuál es")