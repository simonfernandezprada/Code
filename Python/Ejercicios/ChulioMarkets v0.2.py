print ("Bienvenid+ a ChulioMarkets. Nuestros productos son los siguientes")
print("\nAgua \t\t$600\nAzúcar \t\t$1200\nAceite \t\t$1500\nArroz \t\t$1250\nFideos \t\t$790\nBebida \t\t$1780\nChocolate \t$2500\nPan molde \t$1340\n")
tt = 0
q=0

ag = input("Desea llevar agua? s/n?: ")
if ag == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    ag = 600 * q
else:
    ag = 0
tt += ag

az = input("Desea llevar azucar? s/n?: ")
if az == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    az = 1200 * q
else:
    az = 0
tt += az

ac = input("Desea llevar aceite? s/n?: ")
if ac == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    ac = 1500 * q
else:
    ac = 0
tt += ac

ar = input("Desea llevar arroz? s/n?: ")
if ar == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    ar = 1250 * q
else:
    ar = 0
tt += ar

fi = input("Desea llevar fideos? s/n?: ")
if fi == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    fi = 790 * q
else:
    fi = 0
tt += fi

be = input("Desea llevar bebida? s/n?: ")
if be == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    be = 1780 * q
else:
    be = 0
tt += be

ch = input("Desea llevar chocolate? s/n?: ")
if ch == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    ch = 2500 * q
else:
    ch = 0
tt += ch

pm = input("Desea llevar pan de molde? s/n?: ")
if pm == "s":
    q = int(input("Ingrese el numero de unidades:  "))
    pm = 1340 * q
else:
    pm = 0
tt += pm

pref = input("¿Es usted cliente preferencial? s/n?: ")
if pref == "s":
    tt -= tt*0.25

print (f"\nEl total de su compra es ${tt}.-")

cash = int(input("\nIngrese el monto a pagar en efectivo: $ "))
change = cash - tt
if change < 0:
    print("\nDinero insuficiente, Guardias!")
else:
    print(f"\nSu vuelto es ${change}.- Gracias por visitar ChulioMarkets y gracias su compra!")
