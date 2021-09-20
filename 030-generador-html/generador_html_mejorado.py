datos = (("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000))

primer_bloque = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <title>Tabla de ventas</title>
        </head>
        <body>
            <h1>Ventas anuales</h1>
            <table>
                <tr>
                    <td>Mes</td>
                    <td>Ventas</td>
                </tr>
    """
ultimo_bloque = """
        </table>
        </body>
        </html>
    """

NOMBRE_FICHERO = "salida_mejorada.html"
fichero = open(NOMBRE_FICHERO, "w")
fichero.write(primer_bloque)
#COMIENZA LA PARTE VARIABLE
for fila in datos:
    fichero.write("<tr>")
    fichero.write(f"<td>{fila[0]}</td>")
    fichero.write(f"<td>{fila[1]}</td>")
    fichero.write("</tr>")
#FIN DE LA PARTE VARIABLE
fichero.write(ultimo_bloque)

fichero.close()
print("FIN DE LA EJECUCIÓN")