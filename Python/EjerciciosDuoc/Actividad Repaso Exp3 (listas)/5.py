#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

palabras = []
print("Crearemos una lista e ingresaremos 2 palabras")
palabra1 = input("ingrese la primera palabra: ")
palabras.append(palabra1)
palabra2 = input("ingrese la segunda palabra: ")
palabras.append(palabra2)
palabras[0] = palabras[1]
print("Y ahora sustituiremos la primera por la segunda en la lista")
print(palabras)
