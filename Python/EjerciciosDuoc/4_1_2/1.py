# Se requiere crear un vector de tamaño 100, completar los valores del vector aleatoriamente con
# números enteros del 0 al 10, para ello deberá investigar la función que permita crear números
# aleatorios.
import random

vector = [0]*100

for i in range(0,100):
    x = random.randint(0,10)
    vector[i] = x
    i=i+1
print (vector)
