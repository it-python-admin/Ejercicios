vehiculo1 = ["Seat","Toledo","Azul"]
vehiculo2 = ["Renault","4","Amarillo"]
vehiculo3 = ["BMW","314i","Rojo"]
vehiculos = {"M-7797-HH":vehiculo1, "B-1144-BB":vehiculo2,"CC-3432-F":vehiculo3}
matricula = input("Introduce la matricula a buscar:")

# SOLUCION 1 - VICTOR
if matricula in vehiculos:
    print(vehiculos[matricula])
else:
    print("La matricula no existe")

"""
#SOLUCION PANIAGUA
vehiculo_buscado = vehiculos.get(matricula,-1)
if vehiculo_buscado==-1:
    print("No existe")
else:
    print(vehiculo_buscado)
"""

"""
#SOLUCION JUANRA
vehiculo_buscado = vehiculos.get(matricula,"No existe")
print(vehiculo_buscado)
"""

"""
#SOLUCION 2
vehiculo_buscado = vehiculos.get(matricula)
if vehiculo_buscado==None:
    print("No existe")
else:
    print(vehiculo_buscado)
"""

"""
#SOLUCION TRY-EXCEPT
try:
  vehiculo_buscado = vehiculos[matricula]
  print(vehiculo_buscado)
except:
  print("El vehiculo no se encuentra")
"""