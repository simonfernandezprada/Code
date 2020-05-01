i=0
while i<5: 
      u = input("Ingresa tu nombre de usuario: ")
      i+=i
      if u == "pedro" or u == "angel":
          print("Usuario correcto")  
          p = input("ingresa tu contraseña: ")
          if p == "1234" or p == "a4s1":
                print(f"Bienvenido {u}")  
                break
          else:
                print("Clave incorrecta")
                if i==5:
                    print("Demasiados intentos, no es na la feria")
                    break
      else:
            print("Usuario incorrecto")
            if i==5:
                print("Demasiados intentos, no es na la feria")
