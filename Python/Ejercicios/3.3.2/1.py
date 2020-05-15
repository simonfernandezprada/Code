lista = []
opcion = 0
while opcion != 3:
    try:
        opcion = int(input("""
        M E N U

1) Ingresar nombre
2) Revisar lista
3) Salir

Por favor, seleccione una opción: """))
    except:
        print ("\n\tOpción no válida")
    if opcion == 1:
        lista.append(input ("Escriba un nombre para almacenarlo en la lista: "))
    elif opcion == 2:
        print (lista)
    elif opcion == 3:
        print ("¡Gracias y hasta luego!")
        exit()
