import random

def generar_listado_personas(numero):
    nombres = ("Fernando","Andres","Juan Luis", "Victor", "Emilio", "Antonio")
    apellidos = ("Paniagua","Martin","Roca","Ruiz","Perez","Arbelo","Gonzalo","Gutierrez","Olivieri")
    personas=[]
    for i in range(numero):
        nueva_persona = random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)
        personas.append(nueva_persona)
    return personas

def generar_contrasenya(numero_caracteres=20):
    password=""
    vocales_minusculas="aeiou"
    vocales_mayusculas=vocales_minusculas.upper()
    consonantes_minusculas="zyxwvtrsqpñnmlkjhgfdcb"
    consonantes_mayusculas=consonantes_minusculas.upper()
    digitos="0123456789"
    caracteres_especiales="@#_-$%&"
    opciones = [vocales_minusculas, vocales_mayusculas, consonantes_minusculas, consonantes_mayusculas, digitos, caracteres_especiales]
    for i in range(numero_caracteres):
        caracter_aleatorio = (random.choice(random.choice(opciones)))
        password=password+caracter_aleatorio
    return password
