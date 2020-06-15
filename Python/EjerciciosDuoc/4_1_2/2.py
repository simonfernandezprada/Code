# Mostrar por pantalla sólo los valores que se encuentren en los índices pares

import random

vector = [0]*100

for i in range(0,100):
    x = random.randint(0,10)
    vector[i] = x
    if x % 2 ==0:
        print (x)
