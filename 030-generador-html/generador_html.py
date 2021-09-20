datos = (("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000))

NOMBRE_FICHERO = "salida.html"
fichero = open(NOMBRE_FICHERO, "w")
fichero.write("<!DOCTYPE html>")
fichero.write("<html lang=\"es\">")
fichero.write("<head>")
fichero.write("<title>Tabla de ventas</title>\n")
fichero.write("</head>")
fichero.write("\n")
fichero.write("<body>")
fichero.write("\n")
fichero.write("    <h1>Ventas anuales</h1>")
fichero.write("\n")
fichero.write("    <table>")
fichero.write("\n")
fichero.write("        <tr>")
fichero.write("\n")
fichero.write("            <td>Mes</td>")
fichero.write("\n")
fichero.write("            <td>Ventas</td>")
fichero.write("\n")
fichero.write("        </tr>")
fichero.write("\n")
#COMIENZA LA PARTE VARIABLE

for fila in datos:
    fichero.write("<tr>")
    fichero.write(f"<td>{fila[0]}</td>")
    fichero.write(f"<td>{fila[1]}</td>")
    fichero.write("</tr>")

#FIN DE LA PARTE VARIABLE
fichero.write("    </table>")
fichero.write("\n")
fichero.write("</body>")
fichero.write("\n")
fichero.write("</html>")

fichero.close()
print("FIN DE LA EJECUCIÓN")