# Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

palabras = []
sarbalap = []
n=0
n = int(input("Crearemos un listado de palabras. Ingresa el número de palabras que quieras escribir: "))
while n > 0:
    nuevaPalabra = input("Escribe tu palabra: ")
    palabras.append(nuevaPalabra)
    n=n-1
print(palabras)
print("Ahora crearemos una lista igual a la primera pero con los valores invertidos en su orden")
sarbalap = list(reversed(palabras))
print("La nueva lista es: ")
print(sarbalap)
