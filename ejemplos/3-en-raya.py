def mostra_titulo():
    print(" ___         ___               ___   ___         ___  ")
    print("    |       |     |\  |       |   | |   |  \ /  |   | ")
    print(" -+-        |-+-  | + |       |-+-  |-+-|   +   |-+-| ")
    print("    |       |     |  \|       |  \  |   |   |   |   | ")
    print(" ---         ---                                      ")

def mostrar_tablero():
    for f in tablero:
        for c in f:
            print(str(c) + " ",end="")
        print()

PLAYER1 = 1
PLAYER2 = 2
f1 = [0,0,0]
f2 = [0,0,0]
f3 = [0,0,0]

tablero = [f1,f2,f3]

mostra_titulo()
mostrar_tablero()
while True:
    fila = int(input("P1: Introduce fila[0,2]:"))
    columna = int(input("P1: Introduce columna[0,2]:"))
    tablero[fila][columna]=1
    mostrar_tablero()
    fila = int(input("P2: Introduce fila[0,2]:"))
    columna = int(input("P2: Introduce columna[0,2]:"))
    tablero[fila][columna]=2
    mostrar_tablero()