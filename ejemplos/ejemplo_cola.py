import queue
cola = queue.Queue()
cola.put("Item 1")
cola.put("Item 2")
cola.put("Item 3")
cola.put("Item 4")
while cola.empty()==False:
    elemento = cola.get()
    print("Procesando elemento:",elemento)