alimento="Pienso"
categoria=""

if alimento=="Bellota":
    print("Está alimentado con bellotas")
    categoria="Iberico"
elif alimento=="Pienso":
    print("Está alimentado con pienso")
    categoria="Cebo"
elif alimento=="Cacahuete":
    print("Está alimentado con cacahuetes")
    categoria="Estadounidense"
else:
    print("No se sabe qué come")
    categoria="Desconocido"
print("Categoria:",categoria)