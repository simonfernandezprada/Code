i=1
while i<7:
      u = input("Ingresa tu nombre de usuario: ")
      i=i+1
      if u == "pedro" or u == "angel":
          print("Usuario correcto")
          p = input("ingresa tu contraseña: ")
          if p == "1234" or p == "a4s1":
                print(f"Bienvenido {u}")
                break
          else:
                print("Clave incorrecta")
                if i>=7:
                    print("Demasiados intentos, no es na la feria")
                    break
      else:
            print("Usuario incorrecto")
            if i>=7:
                print("Demasiados intentos, no es na la feria")
