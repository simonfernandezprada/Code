from itertools import cycle

personas = []

def digito_verificador(rut):
    try:
        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        return (-s) % 11
    except Exception as e:
        print(e)

def valida_usuario(nombre, apellido, edad, rut):
    try:
        errores = []
        if nombre != '':
            estado_nombre = True
        else:
            estado_nombre = False
            errores.append("El nombre no tiene valor")

        if apellido != '':
            estado_apellido = True
        else:
            estado_apellido = False
            errores.append("El Apellido no tiene valor")

        if int(edad) > 0:
            estado_edad = True
        else:
            estado_edad = False
            errores.append("La edad debe ser mayor a 0")

        if rut != '':
            RUTSNDV = rut[0:-2]
            DV = rut[-1:]
            print(DV, type(DV))
            if DV == 'K' or DV == 'k':
                DV = 10
            DV = int(DV)
            DV_verificado = int(digito_verificador(RUTSNDV))

            if DV == DV_verificado:
                estado_rut = True
            else:
                estado_rut = False
                errores.append("RUT INVALIDO")
        else:
            estado_rut = False
            errores.append("RUT INVALIDO")

        if estado_rut and estado_nombre and estado_edad and estado_apellido:
            return [True, nombre,apellido,edad,rut.lower()]
        else:
            return [False, errores]
    except Exception as e:
        print(e)

def ingresar_persona():
    try:
        nombre = input("Ingrese NOMBRE de la persona >> ")
        apellido = input("Ingrese APELLIDO de la persona >> ")
        edad = int(input("Ingrese EDAD de la persona >> "))
        rut = input("Ingrese RUT de la persona >> ")

        response = valida_usuario(nombre,apellido,edad,rut)
        if response[0] == True:
            persona.append([response[1],response[2],response[3],response[4]])
            print("\n**** Usuario Agregado ****\n")
        else:
            print("Hubieron Errores:")
            for error in response[1]:
                print(error)
    except Exception as e:
        print(e)

def buscar_persona(rut):
    try:
        head = ["Nombre:", "Apellido:", "Edad:", "RUT:"]
        contar = 0
        for i in range(0,len(persona)):
            try:
                encuentra = persona[i].index(rut.lower())

                if encuentra > 0 :
                    print(encuentra)
                    print(f"\nEncontrado en la posicion [{i}][{encuentra}]")
                    print("*****************")
                    count = 0
                    for datos in persona[i]:

                        print(head[count], datos)
                        count += 1

            except ValueError:
                errors = len(persona)
                contar += 1
                if contar == errors:
                    print("Persona no encontrada")
    except Exception as e:
        print(e)

salir = 0
while salir != 3:
    try:
        print("\n\nSeleccione una opcion:")
        opcion = input("""
        \t1. Ingresar Persona\n
        \t2. Buscar Persona\n
        \t3. Salir
        >> """)

        if opcion == '1':
            ingresar_persona()
        elif opcion == '2':
            rut = input("Ingrese RUT de la persona (ej 9999999-1): >> ")
            buscar_persona(rut)
        elif opcion == '3':
            salir = 3
    except Exception as e:
        print("Error Encontrado:",e)
