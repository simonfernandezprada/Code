print("Ahorra ahora! \nTe diremos en cuanto rentará tu dinero\nIngresa el monto a ahorrar")
cantidad = int(input())
print("Ingresa la tasa de interés sin el porcentaje. \nPor ejemplo, si la tasa de interés es de un 1.40%. Ingresa 1.40: ")
intere = float(input())
interes = float(intere/100)
c1a = cantidad+(cantidad*interes)
c2a = c1a+(c1a*interes)
c3a = c2a+(c2a*interes)
print(f"Tu ahorro es de ${cantidad} \nEl primer año tendrás ${c1a}\nEl segundo año tendrás ${c2a}\nEl tercer año tendrás ${c3a}")
