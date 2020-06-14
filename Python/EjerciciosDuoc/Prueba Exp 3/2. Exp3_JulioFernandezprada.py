palabras = []
ingreso = True
print("Crearemos una lista con nombres")
nuevoNombre = input("Ingrese un nombre: ")
palabras.append(nuevoNombre)
while ingreso == True:
    try:
        deseo = int(input("\n\n¿Desea ingresar otro nombre?\n1. Sí\n2. No\n\nSelecione una opción del 1 al 2: "))
    except:
        print("\nOpción no válida. Intenta nuevamente")
    if deseo == 1:
        nuevoNombre = input("Ingrese un nombre: ")
        palabras.append(nuevoNombre)
        ingreso = True
    elif deseo == 2:
        ingreso = False
    else:
        print("Opción no válida")
        ingreso = True
print("Nuestra lista con nombres es la siguiente:")
print(palabras)
