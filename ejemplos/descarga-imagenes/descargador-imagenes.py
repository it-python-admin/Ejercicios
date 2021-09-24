import requests

URL_IMAGEN = "https://m.media-amazon.com/images/M/MV5BMjNkMzc2N2QtNjVlNS00ZTk5LTg0MTgtODY2MDAwNTMwZjBjXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SX300.jpg"

with open("imagen.jpg","wb") as fichero:
    rq = requests.get(URL_IMAGEN)
    fichero.write(rq.content)