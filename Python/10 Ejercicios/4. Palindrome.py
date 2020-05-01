print("Bienvenido a Palíndromo. Un Palíndromo es una palabra que se lee igual tanto de izquierda a derecha como en la dirección contraria. Por favor, ingresa una palabra ")

cadena = input()

print(f"Así se ve tu palabra al reves: {cadena[::-1]}")

if cadena == (cadena[::-1]):
    print(f"¡Felicitaciones, \"{cadena}\" es palíndroma!")
else:
    print(f"Es evidente entonces que la palabra \"{cadena}\" no es palíndroma!")

