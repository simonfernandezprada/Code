#Implemente el siguiente algoritmo representado en notación DFD en lenguaje Python
#Versión solicitada con aproximación de cifra utilizando round()

print("Bienvenido/a, por favor...")
p  = int(input("Ingrese el precio unitario: "))
q = int(input("Ingrese la cantidad de productos: "))
if q>100:
    p = p*0.95
    p = round(p)
s = p*q
print(f"El Subtotal es: ${s}")
ivaToRound = s * 0.19
iva = round(ivaToRound)
print(f"El IVA es: ${iva}")
total = s + iva
print(f"El Total es: ${total}")
