usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None
opcion = 0

while opcion != 3:
    opcion = int(input("""
        M E N U

1) Iniciar sesión
2) Registrar usuario
3) Salir

Por favor, seleccione una opción: """))
    if opcion != 1 or 2 or 3:
        print ("\n\tOpción no válida, elija una opcion del 1 - 3")
    if opcion == 3:
        print ("\n\tHasta luego")
        exit()
    if opcion == 2:
        usuario1 = input("\n\n\tIngrese su nombre de usuario: ")
        contrasena1 = input("\n\n\tIngrese su contrasena: ")
        print (f"\n\n\n\t¡Felicidades, su nombre de USUARIO: {usuario1} ha sido registrado!")
    while opcion == 1:
        if usuario1 == None:
            print ("\n\n\n\n\tEs necesario registrar un usuario antes. Por favor, registre un nombre de usuario")
            break
        if usuario1 != None:
            usertry = input("\n\n\tPor favor, ingrese su nombre de usuario: ")
            if usertry == usuario1 or usuario2 or usuario3:
                passtry = input("\n\n\tPor favor, ingrese su contraseña: ")
                if passtry == contrasena1 or contrasena2 or contrasena3:
                    print ("\n\t¡Bienvenid@!")
                    eleccion = 0
                    while eleccion != 3:
                        eleccion = int(input("""
                            M E N U

                    1) Realizar Llamada
                    2) Enviar correo electrónico
                    3) Cerrar sesión

                    Por favor, seleccione una opción: """))
                        if eleccion == 1:
                            celular = int(input("Por favor, ingrese el número celular de 8 dígitos: +56 9 "))
                        elif eleccion == 2:
                            correo = input("Por favor, ingrese la dirección de email: ")
                            mensaje = input("Escriba su mensaje aquí. \n\n\t  ")
                else:
                    print("\n\tContraseña no válida. Por favor, inténtelo otra vez.")
            else:
                print("\n\tUsuario no válido. Por favor, inténtelo otra vez.")

print("\n\n\tHasta luego")
