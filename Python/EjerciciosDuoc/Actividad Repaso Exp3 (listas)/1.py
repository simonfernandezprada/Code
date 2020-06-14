#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
palabras = []
n=0
while n == 0:
    try:
        n = int(input("Crearemos un listado de palabras. Ingresa el número de palabras que quieras escribir: "))
    except:
        print("\nOpción no válida. Intenta nuevamente")
while n > 0:
    try:
        nuevaPalabra = input("Escribe tu palabra: ")
    except:
        print("\nOpción no válida. Intenta nuevamente")

    palabras.append(nuevaPalabra)
    n=n-1
print(palabras)
