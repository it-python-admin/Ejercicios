edad=17
origen="Huesca"
altura=178

#FILTRO: edad entre 18 y 24, origen es Huesca o Huelva, altura < 205 cm.
#Opcin 1
if (edad>18 and edad<24) and (origen=="Huesca" or origen=="Huelva") and (altura<205):
    print("Cumple")
else:
    print("No cumple")
#Opcion 2 - Anidando
if (edad>18 and edad<24):
    if (origen=="Huesca" or origen=="Huelva"):
        if (altura<205):
            print("Cumple")
        else:
            print("No cumple por la altura")
    else:
        print("No cumple por el origen")
else:
    print("No cumple por la edad")
#Opcion 3 - Refactorización
edad_es_valida = edad>18 and edad<24
origen_es_valido = origen=="Huesca" or origen=="Huelva"
altura_es_adecuada = altura<205

if edad_es_valida and origen_es_valido and altura_es_adecuada:
    print("Cumple")
else:
    print("No cumple")