""" Cree un sistema de ventas de supermercado en el cual se pueda agregar productos al carro de compras, las opciones del menú serán.
⮚ Agregar productos
⮚ Ver canasta
⮚ Ver total
⮚ Salir
En agregar productos deberá mostrar un menú con 5 productos y sus precios (creado por usted), cada vez que se seleccione un producto quedará agregado en la lista.
Ver canasta mostrará todos los productos seleccionados.
Ver total mostrará el total a pagar por el cliente
"""
opcion = 0
eleccion = False
canasta = []
total = 0

while opcion != 4:
    try:
        opcion = int(input("""
    F A R M A C I A S  C O V I D

    \t1. Agregar productos
    \t2. Ver canasta
    \t3. Ver total
    \t4. Salir

    Selecciona una opción del 1 al 4: """))
    except:
        print("\nOpción no válida. Intenta nuevamente")
    if opcion ==1:
        while eleccion == False:
            try:
                compra = int(input("""
                \t\tPRODUCTOS
                1. Bata quirurjica pack 50 unid\t\t $25000
                2. Mascarillas caja 50 unid\t\t $30000
                3. Protector facial caja 20 unid\t $20000
                4. Paracetamol caja 10 unid\t\t $20000
                5. Alcohol gel 10lt\t\t\t $50000

                Elige un producto del 1 al 5:          """))
            except:
                print("\nOpción no válida. Intenta nuevamente")
            if compra == 1:
                canasta.append("Bata quirurjica 50u")
                total = total + 25000
            elif compra == 2:
                canasta.append("Mascarillas 50u")
                total = total + 30000
            elif compra == 3:
                canasta.append("Protector facial 20u")
                total = total + 20000
            elif compra == 4:
                canasta.append("Paracetamol 10u")
                total = total + 20000
            elif compra == 5:
                canasta.append("Alcohol gel 10lt")
                total = total + 50000
            elif compra >= 6 or compra <0:
                print("\nPor Favor, sólo elige opción de 1 al 4")
            decision = int(input("¿Deseas seguir agregando productos a tu canasta?\n1. Sí\n2. No\tEscribe 1 ó 2: "))
            if decision == 1:
                eleccion = False
            else:
                decision == 2
                opcion = 0
                break
    elif opcion == 2:
        print ("\nLos productos elegidos son los siguientes:")
        print (*canasta, sep = "\n")
    elif opcion == 3:
        print ("El total de su compra es: ", + total)
    elif opcion == 4:
        print("Gracias por su visita a FARMACIAS COVID. ¡Hasta pronto!")
        exit()
    elif opcion >= 5 or opcion <0:
        print("\nPor Favor, sólo elija opción de 1 al 4")
