from xml.dom import minidom
doc = minidom.parse("ejemplo.xml")
nombres = doc.getElementsByTagName("nombre")
nombre = nombres[0]
print(nombre.firstChild.data)
libros = doc.getElementsByTagName("libros")
libro = libros[1]
print(type(libro))
titulo = libro.getElementsByTagName("titulo")
print(titulo[0].firstChild.data)