import requests

def get_image_from_url(url: str, file_name: str):
    """
    Obtiene una imagen (como array de bytes) de la URL proporcionada y
    almacena dicha imagen el fichero indicado en el segundo parámetro.

    url: URL de la imagen
    file_name: Nombre del fichero de destino.
    """
    with open(file_name, "wb") as fichero:
        # TODO Mejorar control de excepciones
        try:
            rq = requests.get(url)
            fichero.write(rq.content)
        except:
            print("Ha ocurrido un error")
