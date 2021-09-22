f_entrada=open("origen.pdf","rb")
f_salida=open("salida2.pdf","wb")
caracter=f_entrada.read(1)
while caracter:
    f_salida.write(caracter)
    caracter=f_entrada.read(1)
f_salida.close()
f_entrada.close()
