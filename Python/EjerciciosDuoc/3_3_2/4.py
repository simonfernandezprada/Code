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

def denegado():
    print ("Acceso denegado")
    if i>=5:
        print("Demasiados intentos. Vuelve al menú.")
        opcion = 0

while opcion != 4:
    try:
        opcion = int(input("""
        \tM E N U

        1) Inicio sesión.
        2) Registrar usuario
        3) Eliminar usuario.
        4) Salir.

        Selecciona una opción del 1 al 4: """))
    except:
        print("\nOpción inválida. Intente nuevamente")
    if opcion == 1:
        i = 0
        while i<5:
            ingresoUsuario = input("USUARIO: ")
            i=i+1
            if ingresoUsuario in usuario:
                indexUsuario = usuario.index(ingresoUsuario)
                ingresoContrasena = input("CONTRASEÑA: ")
                if ingresoContrasena in contrasena:
                    indexContrasena = contrasena.index(ingresoContrasena)
                    if indexUsuario == indexContrasena:
                        print (f"¡Bienvenido {ingresoUsuario}, enhorabuena, éxito!")
                        opcion = 0
                        break
                    else:
                        denegado()
                else:
                    denegado()
            else:
                print(f"Usuario {ingresoUsuario} no existe")
                if i>=5:
                    print("Demasiados intentos. Vuelve al menú.")
                    opcion = 0
    elif opcion == 2:
        registroUsuario = input("Ingrese el nombre de usuario a registrar: ")
        utilizado = False
        if registroUsuario in usuario:
            utilizado = True
        while utilizado == True:
            print("Usuario ya existe, intente con otro nombre de usuario.")
            registroUsuario = input("Ingrese el nombre de usuario a registrar: ")
            if registroUsuario not in usuario:
                utilizado = False
        registroContrasena = input("Ingrese la contraseña a registrar: ")
        usuario.append(registroUsuario)
        contrasena.append(registroContrasena)
        print(f"El usuario {registroUsuario} y su contraseña han sido registrados con éxito")
        opcion = 0
    elif opcion == 3:
        i = 0
        while i<5:
            eliminaUsuario = input("Ingresa el nombre de usuario a eliminar: ")
            i=i+1
            if eliminaUsuario in usuario:
                indexUsuario = usuario.index(eliminaUsuario)
                eliminaContrasena = input ("Ingrese contraseña: ")
                if eliminaContrasena in contrasena:
                    indexContrasena = contrasena.index(eliminaContrasena)
                    if indexUsuario == indexContrasena:
                        print (f"El nombre de usuario {eliminaUsuario} y su contraseña han sido eliminadas")
                        usuario.remove(eliminaUsuario)
                        contrasena.remove(eliminaContrasena)
                        opcion = 0
                    else:
                        denegado()
                else:
                    denegado()
            else:
                print(f"Usuario {eliminaUsuario} no existe")
                if i>=5:
                    print("Demasiados intentos. Vuelve al menú.")
                    opcion = 0

    elif opcion == 4:
        print("Adios, amigo")
        exit()
    elif opcion >= 5 or opcion <0:
        print("\nSeleciona una opción del 1 al 4")
