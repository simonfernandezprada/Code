print("           ____________________________\n          |  ________________________  |\n          | |                        | |\n          | |                        | |\n          | |       * * * * *        | |\n          | |       Welcome to       | |\n          | |                        | |\n          | |         CHULIO         | |\n          | |        Customs         | |\n          | |         Agency         | |\n          | |                        | |\n          | |       * * * * *        | |\n          | |                        | |\n          | |________________________| |\n          |____________________________|")

X = int(input("\n\n\nPor favor, introduzca los mt3 de carga que desea transportar: "))
Y = int(input("\nIntroduzca el valor declarado en dólares: USD$"))
costo = 0

if (X >= 5):
    costo += 100 * X
else:
    costo += 150 * X
print(f"\nLa carga a transportar es de {X}mt3")
print(f"El costo de transporte de USD${costo}.-")

subtotal = Y + costo

print(f"\nEl costo de transporte más el valor declarado en dolares suman USD${subtotal}")

if (Y >= 5000):
    subtotal += subtotal * 0.1
    print(f"\nEl valor declarado en dolares es igual o superior a los USD$5.000 \nSe aplicará un 10% de impuesto sobre el valor declarado más el costo de transporte")
else:
    subtotal += subtotal * 0.19
    print(f"\nEl valor declarado en dolares es inferior a los USD$5.000 \nSe aplicará un 19% de impuesto sobre el valor declarado más el costo de transporte")
print(f"\nValor total a pagar USD$ {subtotal}")
