print("Calculemos tu IMC! Ingresa tu estatura en centímetros. Ej: Si mides 1,82 ingresa: 1.82")
h = float(input())
print("Ahora ingresa tu peso en kilos:  ")
w = int(input())

imc = w/h**2

print(f"Tu IMC es {imc}.")