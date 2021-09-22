LIMITE_VELOCIDAD=120
capturas = []
with open("radar.txt","r") as fichero:
    #Matricula, fecha y velocidad
    matricula = fichero.readline()
    while matricula!="":
        matricula = matricula.replace("\n","")
        fecha = fichero.readline().replace("\n","")
        velocidad = int(fichero.readline().replace("\n",""))
        capturas.append((matricula,fecha,velocidad))        
        matricula = fichero.readline()
print(capturas)

for captura in capturas:
    if (captura[2]>LIMITE_VELOCIDAD):
        print("Denuncia al canto:",captura[0],"el día",captura[1],"iba a",captura[2])