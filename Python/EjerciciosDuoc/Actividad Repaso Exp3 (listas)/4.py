#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.
programa = True
palabras = []
print("Primero crearemos una Lista de palabras")
nuevaPalabra = input("ingrese una palabra: ")
palabras.append(nuevaPalabra)
while programa == True:
    opcion = int(input("\t\tM E N U\n1. Agregar nueva palabra\n2. Eliminar palabra\n3. Salir\nIngrese 1, 2 o 3: "))
    if opcion == 1:
        nuevaPalabra = input("ingrese una palabra: ")
        palabras.append(nuevaPalabra)
        programa == True
    elif opcion == 2:
        print(palabras)
        elimina = input("Escriba la palabra a eliminar:")
        palabras.remove(elimina)
        print("Ahora la lista luce así: ")
        print(palabras)
    elif opcion == 3:
        print("Hasta luego")
        exit()
    elif opcion >= 4 or opcion < 1:
        print("Solo números del 1 al 3. Vuelve al menú.")
