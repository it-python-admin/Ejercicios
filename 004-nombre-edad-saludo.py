nombre=input("Introduce tu nombre:")
edad=int(input("Introduce tu edad:"))
print("Hola",nombre,end="")
if edad>=18:
    print(", eres mayor de edad")
else:
    print(", eres menor de edad")