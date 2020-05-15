usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None
opcion = 0

while opcion != 3:
    try:
        opcion = int(input("""
        M E N U

1) Iniciar sesión
2) Registrar usuario
3) Salir

Por favor, seleccione una opción: """))
    except:
        print ("\n\tOpción no válida")
    if opcion > 3:
        print ("\n\tElija una opcion del 1 - 3")
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
        elif usuario1 != None:
            usertry = input("\n\n\tPor favor, ingrese su nombre de usuario: ")
            if usertry == usuario1 or usuario2 or usuario3:
                passtry = input("\n\n\tPor favor, ingrese su contraseña: ")
                if passtry == contrasena1 or contrasena2 or contrasena3:
                    print ("\n\t¡Bienvenid@!")
                    eleccion = 0
                    while eleccion != 3:
                        try:
                            eleccion = int(input("""
                            M E N U

                    1) Realizar Llamada
                    2) Enviar correo electrónico
                    3) Cerrar sesión

                    Por favor, seleccione una opción: """))
                        except:
                            print ("\n\tOpción no válida")
                        if eleccion > 3:
                            print ("\n\tElija una opcion del 1 - 3")
                        elif eleccion == 1:
                            celular = None
                            while celular == None:
                                celular = input("\n\n\tPor favor, ingrese el número celular de 8 dígitos: +56 9 ")
                                if celular.isdigit() == False:
                                    print("\n\n\tPor favor, ingrese SOLO NUMEROS")
                                else:
                                    if len(celular) > 8:
                                        print ("\n\n\tIngrese hasta 8 dígitos")
                                    elif len(celular) < 8:
                                        print ("\n\n\tIngrese 8 dígitos")
                                    else:
                                        print (f"\n\n\tEl número +56 9 {celular} ha sido guardado y está listo para realizar llamadas.")
                                    break
                        elif eleccion == 2:
                            correo = input("\n\n\tPor favor, ingrese la dirección de email: ")
                            mensaje = input("\n\n\tEscriba su mensaje aquí. \n\n\t  ")
                            print(f"\n\n\tSu mensaje \n\t{mensaje} \n\n\t Ha sido guardado y está listo para ser enviado.")
                        elif eleccion == 3:
                            print(f"\n\n\tEstimado {usuario1}, su sesión ha sido cerrada con éxito")
                            print ("\n\n\tHasta luego")
                            exit()
                else:
                    print("\n\tContraseña no válida. Por favor, inténtelo otra vez.")
            else:
                print("\n\tUsuario no válido. Por favor, inténtelo otra vez.")
print ("Hasta luego")
