NOMBRE_FICHERO = "cotizacion.dat"
def get_cotizaciones(nombre_fichero):
    cotizaciones = []
    with open(nombre_fichero, "r") as fichero:
        nombre = fichero.readline()
        while (nombre!=""):
            nombre = nombre.replace("\n","")
            siglas = fichero.readline().replace("\n","")
            variacion = float(fichero.readline().replace("\n",""))
            cotizaciones.append((nombre, siglas, variacion))
            nombre = fichero.readline()
    return cotizaciones
def get_cotizaciones_negativas(cotizaciones):
    cotizaciones_negativas = []
    for cotizacion in cotizaciones:
        variacion = cotizacion[2]
        if (variacion<0):
            cotizaciones_negativas.append(cotizacion)
    return cotizaciones_negativas
def generar_ordenes_venta(cotizaciones_negativas):
    for c in cotizaciones_negativas:
        print(("Orden de venta de la criptomoneda {moneda} ({siglas}). Su variación es {variacion}").
        format(moneda=c[0],variacion=c[2],siglas=c[1]))

cotizaciones = get_cotizaciones(NOMBRE_FICHERO)
cotizaciones_negativas = get_cotizaciones_negativas(cotizaciones)
generar_ordenes_venta(cotizaciones_negativas)