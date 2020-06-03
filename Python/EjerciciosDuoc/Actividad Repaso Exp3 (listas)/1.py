#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
palabras = []
n=0
n = int(input("Crearemos un listado de palabras. Ingresa el número de palabras que quieras escribir: "))
while n > 0:
    nuevaPalabra = input("Escribe tu palabra: ")
    palabras.append(nuevaPalabra)
    n=n-1
print(palabras)
