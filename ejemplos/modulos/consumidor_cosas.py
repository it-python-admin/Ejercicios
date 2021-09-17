import generador_cosas_random 
from generador_cosas_random import generar_listado_personas as glp, generar_contrasenya as gc

nuevas_personas = glp(5)
print("Las nuevas personas son:",nuevas_personas)

nueva_password = gc(30)
print("La nueva contraseña es:",nueva_password)

otra_password = generador_cosas_random.generar_contrasenya(10)
print("La otra contraseña nueva es:",otra_password)