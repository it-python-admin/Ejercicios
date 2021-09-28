class Pelicula:
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
    #constructor
    def __init__(self, titulo, year, calificacion, released, genre, director, actores, poster):
        self.title = titulo
        self.year = year
        self.rated = calificacion
        self.released = released
        self.genre = genre
        self.director = director
        self.actors = actores.split(",")
        for i in range(len(self.actors)):
            self.actors[i] = self.actors[i].strip()
        self.poster = poster
    #destructor
    def __del__(self):
        print("Destruyendo...")
    #métodos
    def generarPDF(self):
        pass

    def mostrarPorPantalla(self):
        pass
    
    def generarHTML(self, nombre_fichero):
        with open(nombre_fichero,"w") as fichero:
            fichero.write("<html><head></head><body>")
            fichero.write("<h1>" + self.title + "</h1>")
            fichero.write("</body></html>")

    def guarda(self):
        pass

#Instanciación de un objeto Pelicula llamado peli (construcción del objeto)
peli = Pelicula("Titulo de prueba",1980,"+18","12/05/1980","Comedia","Director de prueba","Actor 1, Actor 2","url del poster")
#peli.generarHTML("pelicula.html")
print("Fin de la ejecución")