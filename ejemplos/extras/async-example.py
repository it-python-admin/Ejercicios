#ESTE EJERCICIO NO ESTÁ FUNCIONANDO - ESTÁ INCOMPLETO
import asyncio

async def temporizador(segundos):
    for s in range(segundos,0,-1):
        print(s)
        await asyncio.sleep(1)

print("Antes de pedir a JL el informe")
asyncio.run(temporizador(10))
print("Mientras JL realiza el informe")
