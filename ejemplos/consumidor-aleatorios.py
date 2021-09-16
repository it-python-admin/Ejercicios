#import generador_numeros
#numero = generadornumeros.dame_aleatorio_entre_0_100()
#print(numero)

#from generador_numeros import dame_aleatorio_entre_0_100
#numero = dame_aleatorio_entre_0_100()
#print(numero)

#import generador_numeros as gn
#numero = gn.dame_aleatorio_entre_0_100()
#print(numero)

from generador_numeros import dame_aleatorio_entre_0_100 as alias
numero = alias()
print(numero)