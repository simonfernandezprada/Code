# Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
# Lista de palabras que aparecen en las dos listas.
# Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# Lista de palabras que aparecen en la segunda lista, pero no en la primera.
# Lista de palabras que aparecen en ambas listas.
# Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.

palabras1 = []
palabras2 = []
n = 0
n = int(input("Crearemos dos listas de palabras.\nPara la primera lista de palabras, ingresa el número de palabras que quieras escribir: "))
while n > 0:
    nuevaPalabra = input("Escribe tu palabra: ")
    palabras1.append(nuevaPalabra)
    n=n-1
print("Estas son las palabras de tu primer listado  de palabras:")
print(palabras1)
m = 0
m = int(input("Para la segunda lista de palabras, ingresa el número de palabras que quieras escribir: "))
while n > 0:
    nuevaPalabra = input("Escribe tu palabra: ")
    palabras2.append(nuevaPalabra)
    n=n-1
print("Estas son las palabras de tu segundo listado  de palabras:")
print(palabras2)
