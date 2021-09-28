import json
import urllib.request

class PeliculaOMDB:
    #atributos -> define el estado
    title = ""
    year = 0
    rated = ""
    released = ""
    genre = ""
    director = ""
    actors = []
    poster = ""
    complejidad = 0
    API_KEY = "8c290063"
    #constructor
    def __init__(self,id_pelicula):
        url = f"https://www.omdbapi.com/?apikey={self.API_KEY}&i={id_pelicula}"
        webUrl  = urllib.request.urlopen(url)
        data = webUrl.read()
        pelicula = json.loads(data) #Convierte directamente los bytes
        self.title = pelicula["Title"]
        self.year = pelicula["Year"]
        self.rated = pelicula["Rated"]
        self.released = pelicula["Released"]
        self.genre = pelicula["Genre"]
        self.director = pelicula["Director"]
        self.actors = pelicula["Actors"].split(",")
        for i in range(len(self.actors)):
            self.actors[i] = self.actors[i].strip()
        self.poster = pelicula["Poster"]
    #destructor
    def __del__(self):
        print("Destruyendo...")

    #método especial
    def __str__(self):
        cadena = "******" + self.title + "********"
        cadena+= "\n***" + self.director + "\n"
        return cadena

    #métodos
    def generarPDF(self):
        pass

    def muestrate(self):
        print(self)
    
    def generarHTML(self):
        with open(self.title+".html","w") as fichero:
            fichero.write("<html><head></head><body>")
            fichero.write("<h1>" + self.title + "</h1>")
            fichero.write("<br>")
            fichero.write(f"<img src='{self.poster}'>")
            fichero.write("</body></html>")

    def guarda(self):
        pass


titulo_pelicula = input("Introduce el título de la película:")
url = f"https://www.omdbapi.com/?apikey=8c290063&s={titulo_pelicula}"
webUrl  = urllib.request.urlopen(url)
data = webUrl.read()
peliculas = json.loads(data) #Convierte directamente los bytes
id_pelicula = peliculas["Search"][0]["imdbID"]
#Instanciación de un objeto Pelicula llamado peli (construcción del objeto)

peli = PeliculaOMDB(id_pelicula)
peli.generarHTML()
peli.muestrate()
print("Fin de la ejecución")