

cadena = input("""

\tBienvenido a Palíndromo.

\tUn Palíndromo es una palabra que se lee igual tanto de izquierda a derecha como en la dirección contraria.
\tPor favor, ingresa una palabra: """)

print(f"\n\tAsí se ve tu palabra al reves: {cadena[::-1]}")

if cadena == (cadena[::-1]):
    print(f"\n\t¡Felicitaciones, \"{cadena}\" es palíndroma!")
else:
    print(f"\n\t¡Es evidente entonces que la palabra \"{cadena}\" no es palíndroma!")
