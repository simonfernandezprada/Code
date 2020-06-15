# 8).- Crear un menú con las opciones:

#            1)Agregar persona
#            2)Ver Persona
# Donde agregar permita ingresar el nombre de una persona por pantalla mientras el vector no esté
# completo.
# Ver persona permite ver el nombre del índice ingresado por pantalla.

opcion = 0
opcion = int("1)Agregar persona\n2)Ver Persona\n\nSeleccione un número 1 ó 2: ")

while opcion <1 or opcion >2:
    if opcion == 1:
        vector = ["a"]*10
        i = 0
        if i != 10:
            for i in range(0,10):
                vector[i] = input("Ingresa el nombre de la persona: ")
                i=i+1
    if opcion == 2:
        x = int("Ingrese el número de índice de la persona del 1 al 10: ")
        x=x+1
        vector.index(x)
print("Hasta luego")
