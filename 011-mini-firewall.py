#Cuando se detecten 3 veces la misma IP se incluye a la misma en una lista negra.
#A partir de entonces, cuando se introduzca esa dirección IP se le muestra un mensaje de rechazo.
NUMERO_INTENTOS = 3
IP_SALIDA = "0"
ip="-1"
lista_ip = []
lista_negra_ip = []
while ip!=IP_SALIDA:
    ip=input("Introduce una direccion IP:")
    if (ip in lista_negra_ip):
        print("La direccion",ip,"esta atacando mi sistema")
    elif (ip!=IP_SALIDA):
        lista_ip.append(ip)
        print(lista_ip)
        if (lista_ip.count(ip)==NUMERO_INTENTOS):
            lista_negra_ip.append(ip)