referencias = [
    [0,"Delgadez muy severa"],
    [15,"Delgadez severa"],
    [16,"Delgadez"], 
    [18.5,"Peso Saludable"], 
    [25,"Sobrepeso"],
    [30,"Obesidad Moderada"], 
    [35,"Obesidad severa"], 
    [40,"Obesidad muy severa"]]
referencias.reverse()

altura = float(input("Altura(en metros):"))
peso = float(input("Peso(en kg.):"))
imc = peso/altura**2
print("IMC:",imc)

for referencia_actual in referencias:
    if (imc>=referencia_actual[0]):
        rango=referencia_actual[1]
        break        

print("Tu estado es:",rango)
