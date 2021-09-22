with open("datos-formato.dat") as f:
   #deporte = f.read(2)
   #anyo = f.read(4)
   #campeonato = f.read(15)
   f.seek(21)
   pais_ganador = f.read(3)

#print(deporte,anyo,campeonato,pais_ganador)
print(pais_ganador)