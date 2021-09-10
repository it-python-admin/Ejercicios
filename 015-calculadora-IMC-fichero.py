import winsound
DURACION_PITIDO = 1000
EXTENSION_FICHERO = ".txt"
nombre_paciente = input("Introduce tu nombre:")
altura = float(input("Altura(en metros):"))
peso = float(input("Peso(en kg.):"))
imc = peso/altura**2
print("IMC:",imc)
winsound.Beep(int(imc)*10,DURACION_PITIDO)
if (imc>=40):
    rango="Obesidad muy severa"
elif (imc>=35):
    rango="Obesidad severa"
elif (imc>=30):
    rango="Obesidad moderada"
elif (imc>=25):
    rango="Sobrepeso"
elif (imc>=18.5):
    rango="Peso saludable"
elif (imc>=16):
    rango="Delgadez"
elif (imc>=15):
    rango="Delgadez severa"
else:
    rango="Delgadez muy severa"
print("Tu estado es:",rango)
#Creamos el nombre del fichero
nombre_fichero = nombre_paciente.replace(" ","_").lower() + EXTENSION_FICHERO
#Escribir el resultado en un fichero
fichero = open(nombre_fichero,"w")
fichero.write("El IMC de " + nombre_paciente + " es " + str(imc))
fichero.write("\n")
fichero.write("El estado de " + nombre_paciente + " es " + rango)
fichero.close()
