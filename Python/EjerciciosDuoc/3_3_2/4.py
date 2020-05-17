"""
Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la opción de eliminar
usuarios usando su nombre de usuario para hacerlo, para confirmar la eliminación deberán escribir
la contraseña correspondiente a cada usuario.
1) Inicio sesión.
2) Registrar usuario
3) Eliminar usuario.
4) Salir.
La opción 1 sólo deberá mostrar un mensaje exitoso en caso de haber iniciado correctamente, o un
mensaje de error de caso contrario.
"""

usuario = []
contrasena = []
opcion = 0
while opcion != 4:
    opcion = int(input("""
    \tM E N U

    1) Inicio sesión.
    2) Registrar usuario
    3) Eliminar usuario.
    4) Salir.

Selecciona una opción del 1 al 4: """))
    if opcion == 1:
        i = 0
        while i<5:
            ingresoUsuario = input("USUARIO: ")
            i=i+1
            if ingresoUsuario in usuario:
                ingresoContrasena = input ("CONTRASEÑA: ")
                if ingresoContrasena in contrasena:
                    print (f"¡Bienvenido {ingresoUsuario}, enhorabuena, éxito!")
                    opcion = 0
                else:
                    print ("Acceso denegado")
                    if i>=5:
                        print("Demasiados intentos. Vuelve al menú.")
                        opcion = 0
            else:
                print(f"Usuario {ingresoUsuario} no existe")
                if i>=5:
                    print("Demasiados intentos. Vuelve al menú.")
                    opcion = 0
    if opcion == 2:
        registroUsuario = input("Ingrese el nombre de usuario a registrar: ")
        registroContrasena = input("Ingrese la contraseña a registrar: ")
        usuario.append(registroUsuario)
        contrasena.append(registroContrasena)
        print(f"El usuario {registroUsuario} y su contraseña han sido registrados con éxito")
        opcion = 0
    if opcion == 3:
        i = 0
        while i<5:
            eliminaUsuario = input("Ingresa el nombre de usuario a eliminar: ")
            i=i+1
            if eliminaUsuario in usuario:
                eliminaContrasena = input ("Ingrese contraseña: ")
                if eliminaContrasena in contrasena:
                    print (f"El nombre de usuario {eliminaUsuario} y su contraseña han sido eliminadas")
                    usuario.remove(eliminaUsuario)
                    contrasena.remove(eliminaContrasena)
                    opcion = 0
                else:
                    print ("Contraseña inválida")
                    if i>=5:
                        print("Demasiados intentos. Vuelve al menú.")
                        opcion = 0
            else:
                print(f"Usuario {eliminaUsuario} no existe")
                if i>=5:
                    print("Demasiados intentos. Vuelve al menú.")
                    opcion = 0

    if opcion == 4:
        print("Adios, amigo")
        exit()
    if opcion >= 5 or opcion <0:
        print("\nSeleciona una opción del 1 al 4")
