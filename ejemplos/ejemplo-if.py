DIASTOLICA_LIMITE = 84
SISTOLICA_LIMITE = 129

estado = ""
diastolica = int(input("Introduce la presion baja (diastolica):"))
sistolica = int(input("Introduce la presion alta (sistolica):"))
if diastolica<=DIASTOLICA_LIMITE and sistolica<=SISTOLICA_LIMITE:
    estado="NORMAL"
    #mas instrucciones
else:
    estado="HIPERTENSO"
    #mas instrucciones
print("El estado del paciente es:",estado)

