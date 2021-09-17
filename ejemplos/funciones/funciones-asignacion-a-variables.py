#Pese a cambiar el código de f1, la función alias() ejecuta el código de la función f1 original.

def f1():
    print("UNO")

alias = f1
alias()

def f1():
    print("DOS")

alias()