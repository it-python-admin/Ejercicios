#import paniagua.descargador_imagenes
import paniagua.descargador_imagenes as di

url = input("Introduce la URL del fichero gráfico:")
nombre_fichero = input("Introduce el nombre del fichero con su extensión:")

#paniagua.descargador_imagenes.get_image_from_url(url,nombre_fichero)
di.get_image_from_url(url, nombre_fichero)