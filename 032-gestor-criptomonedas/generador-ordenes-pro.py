NOMBRE_FICHERO = "cotizacion.dat"
NOMBRE_FICHERO_VENTAS_POSITIVAS = "ventas_positivas.dat"
NOMBRE_FICHERO_VENTAS_NEGATIVAS = "ventas_negativas.dat"
def get_cotizaciones(nombre_fichero):
    cotizaciones = []
    with open(nombre_fichero, "r") as fichero:
        nombre = fichero.readline().replace("\n","")
        while (nombre!=""):
            siglas = fichero.readline().replace("\n","")
            variacion = float(fichero.readline().replace("\n",""))
            cotizaciones.append((nombre, siglas, variacion))
            nombre = fichero.readline().replace("\n","")
    return cotizaciones
def get_cotizaciones_negativas(cotizaciones):
    cotizaciones_negativas = []
    for cotizacion in cotizaciones:
        variacion = cotizacion[2]
        if (variacion<0):
            cotizaciones_negativas.append(cotizacion)
    return cotizaciones_negativas
def get_cotizaciones_positivas(cotizaciones):
    cotizaciones_positivas = []
    for cotizacion in cotizaciones:
        variacion = cotizacion[2]
        if (variacion>0):
            cotizaciones_positivas.append(cotizacion)
    return cotizaciones_positivas
def escribir_cotizaciones(nombre_fichero, cotizaciones):
    with open(nombre_fichero, "a") as fichero:
        for c in cotizaciones:
            fichero.write(("Orden de venta de la criptomoneda {moneda} ({siglas}). Su variación es {variacion}").
                format(moneda=c[0],variacion=c[2],siglas=c[1]))
            fichero.write("\n")
def get_cotizacion(cotizaciones, moneda):
    for c in cotizaciones:
        if (c[0]==moneda):
            return c[2]


cotizaciones = get_cotizaciones(NOMBRE_FICHERO)
#ALTERNATIVA 1
cotizaciones_negativas = get_cotizaciones_negativas(cotizaciones)
escribir_cotizaciones(NOMBRE_FICHERO_VENTAS_NEGATIVAS, cotizaciones_negativas)
#ALTERNATIVA 2
escribir_cotizaciones(NOMBRE_FICHERO_VENTAS_POSITIVAS, get_cotizaciones_positivas(cotizaciones))

#PROCESO DE CONSULTA:
moneda = input("Introduce el nombre de la moneda:")
cotizacion = get_cotizacion(cotizaciones, moneda)
print(("La cotizacion de {0} es {1}").format(moneda,cotizacion))