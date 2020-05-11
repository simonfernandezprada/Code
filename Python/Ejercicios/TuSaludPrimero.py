
print("Hola le tomo su orden disponemos de los siguientes tipos de pizzas son: (1)Fiorina, (2)Napolitana, (3)Firenze y (4)Simple")
Pizzas = int(input("Ingrese cuantas pizzas va a querer: "))
tipo = int(input("Okey, De que tipo 1 , 2 , 3 o 4?: "))
piza = tipo

if  piza == 1:
     A = 6500
else:
    A=0
if piza == 2:
    C = 6000
else:
    C = 0
if piza == 3:
    X = 7500
else:
    X = 0
if piza == 4:
      D = 5000
else:
      D = 0
Total = A + C + X + D
print(f"Su total es de {Total}")
