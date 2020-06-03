#Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

palabras1 = []
palabras2 = []
n=0
n = int(input("Crearemos un listado de palabras. Si hay palabas repetidas, serán eliminadas todas menos la primera en repetirse. Ingresa el número de palabras que quieras escribir: "))
while n > 0:
    nuevaPalabra = input("Escribe tu palabra: ")
    palabras1.append(nuevaPalabra)
    n=n-1
print(palabras1)
for elem in palabras1:
    if elem not in palabras2:
        palabras2.append(elem)
print(palabras2)
