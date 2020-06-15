# Mostrar el elemento menor.

import random

vector = [0]*100

menor = 100000
for i in range(0,100):
    x = random.randint(0,100000)
    vector[i] = x
    i=i+1
    if menor>x:
         menor=x
print (vector)
print ("El elemento menor es: ", + menor)
