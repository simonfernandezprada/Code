# Escriba	un	programa	que	despliegue	el	sguiente	menú:
# Venta
# Totalizar
# Salir
opcion = 0
while opcion == 0:
    try:
        opcion = int(input("\t\tM E N U\n1. Venta\n2. Totalizar\n3. Salir\n\nSeleccione una opción del 1 al 3:"))
    except:
        print("\nLa opción seleccionada no es válida. Por favor intente nuevamente \n")
while opcion != 3:
    if opcion == 1:
        venta = int(input("Por favor ingrese el valor de su venta: "))
        
