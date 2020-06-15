# 7).- Crear un Vector de tamaño 10 que almacene nombres de personas.

vector = ["a"]*10
i = 0
if i != 10:
    for i in range(0,10):
        vector[i] = input("Ingresa el nombre de la persona: ")
        i=i+1
print(vector)
