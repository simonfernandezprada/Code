cant_prod = int(input("\n\tPor favor, ingrese la cantidad de productos: "))
monto = int(input("\n\tPor favor, ingrese el monto total de su compra: "))

if monto > 50000:
    total = monto
    print ("\n\tSu despacho es gratis")
elif monto <= 50000 and cant_prod >= 3:
    total = monto + (cant_prod * 1500)
    print ("\n\tSu despacho tiene un valor de $1500 por producto")
elif monto <= 50000 and cant_prod < 3:
    total = monto + (cant_prod * 2500)
    print ("\n\tSu despacho tiene un valor de $2500 por producto")

print(f"\n\tEl valor final a pagar es ${total}")
