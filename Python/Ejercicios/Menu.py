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
    if opcion == 1 and usuario1 or usuario2 or usuario3 == None:
        print("Es necesario registrar un usuario antes. Por favor, registre un nombre de usuario")
    if opcion == 1 and usuario1 or usuario2 or usuario3 != None:
        usertry = input("Por favor, ingrese su nombre de usuario:")
        if usertry == usuario1 or usuario2 or usuario3:
            passtry = input("Por favor, ingrese su contraseña: ")
        else:
            print("Usuario no válido. Por favor, inténtelo otra vez")
    if opcion == 2:
        usuario1 = input("Ingrese su nombre de usuario: ")
        contrasena1 = input("Ingrese su contrasena: ")

print("Hasta luego")
