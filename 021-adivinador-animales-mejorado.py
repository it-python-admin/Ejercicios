animales = ["Dog","Cat","Bird","Cow","Snake"]
animal_candidato = input("Introduce el nombre de un animal en inglés:")
while animal_candidato not in animales:
    print("Ese animal no está en la lista")
    animal_candidato = input("Introduce el nombre de un animal en inglés:")
else:
    print("Has acertado, eres un visionario")
print("Has terminado el juego")