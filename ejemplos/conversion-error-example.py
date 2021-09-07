entrada = input("Introduce un número entero positivo o negativo:")
try:
  valor = int(entrada)
  print(valor,"es un número entero")
except:
  print("ERROR:",entrada,"no es un número entero")