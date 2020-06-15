# Mostrar el índice (posición) del elemento mayor.

import random

vector = [0]*100

mayor = 0
for i in range(0,100):
    x = random.randint(0,100000)
    vector[i] = x
    i=i+1
    if mayor<x:
         mayor=x
print (vector)
print ("El elemento mayor es: ", + mayor)
print ("Su posicion en la lista es la número: ", + vector.index(mayor))
