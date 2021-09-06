PALABRA_PROHIBIDA1 = "ADMIN"
PALABRA_PROHIBIDA2 = "123"
PALABRA_PROHIBIDA3 = "PASSWORD"

idUsuario = input("Introduzca su identificador:")
pwd = input("Introduzca su contraseña:")

if PALABRA_PROHIBIDA1 in pwd:
    print("Error")
elif PALABRA_PROHIBIDA2 in pwd:
    print("Error")
elif PALABRA_PROHIBIDA3 in pwd:
    print("Error")
else:
    print("OK")