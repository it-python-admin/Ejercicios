MAYORIA_EDAD=18
edad = int(input("Introduzca su edad:"))
nacionalidad = input("Introduzca su nacionalidad:")
idioma1 = input("Introduzca su primer idioma:")
idioma2 = input("Introduzca su segundo idioma:")
#and, or not
#Mayor de edad
#NACIONALIDAD: Frances o Aleman Y no Ruso
#IDIOMAS 1 Y 2: Ingles y Chino
mayor_edad = edad>=MAYORIA_EDAD
nacionalidad_ok = (nacionalidad=="Frances" or nacionalidad=="Aleman") and nacionalidad!="Ruso"
idiomas_ok = idioma1=="Ingles" and idioma2=="Chino"

#es_apto = (edad>=MAYORIA_EDAD) and ((nacionalidad=="Frances" or nacionalidad=="Aleman") and nacionalidad!="Ruso") and (idioma1=="Ingles" and idioma2=="Chino")
es_apto = mayor_edad and nacionalidad_ok and idiomas_ok

if (es_apto):
    print("Contratado")
else:
    print("Lo siento, no cumple el perfil")