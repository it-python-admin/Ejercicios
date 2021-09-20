"""
Utilizando generador_cosas_random.py, crear un fichero
con extensión csv que contenta 100 nombres y 100 contraseñas
mostradas en columnas separadas.

Las columnas tendrán como título: NOMBRE y CONTRASEÑA
"""
import generador_cosas_random as gcr
NUMERO_ELEMENTOS = 100
NOMBRE_FICHERO = "salida.csv"

fichero = open(NOMBRE_FICHERO, "w")
fichero.write("NOMBRE,PASSWORD\n")
personas = gcr.generar_listado_personas(NUMERO_ELEMENTOS)
for persona in personas:
    password = gcr.generar_contrasenya()
    fichero.write(persona + "," + password + "\n")
fichero.close()
print("Proceso terminado")



