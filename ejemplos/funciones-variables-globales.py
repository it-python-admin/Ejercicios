x = 10
def incrementar():
    global x
    x = x + 5
    print("En la función",x)

incrementar()
print("En el ámbito global",x)

