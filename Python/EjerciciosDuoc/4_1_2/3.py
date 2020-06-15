# Mostrar el elemento mayor, sólo 1 en caso de repetirse.

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
