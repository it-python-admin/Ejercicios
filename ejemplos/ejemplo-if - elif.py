DIASTOLICA_LIMITE_ALTA = 84
SISTOLICA_LIMITE_ALTA = 129
DIASTOLICA_LIMITE_PELIGRO = 99
SISTOLICA_LIMITE_PELIGRO = 159

estado = ""
diastolica = int(input("Introduce la presion baja (diastolica):"))
sistolica = int(input("Introduce la presion alta (sistolica):"))

if diastolica<=DIASTOLICA_LIMITE_ALTA and sistolica<=SISTOLICA_LIMITE_ALTA:
    estado="NORMAL"
elif diastolica>DIASTOLICA_LIMITE_PELIGRO or sistolica>SISTOLICA_LIMITE_PELIGRO:
    estado="EN PELIGRO"
else:
    estado="HIPERTENSO"

print("El estado del paciente es:",estado)

