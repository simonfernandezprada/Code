print('           ╔═════════════════════════════╗\n           ║                             ║\n           ║    EAT LIKE NO TOMORROW!    ║\n           ║                             ║\n           ║           M E N U           ║\n           ║                             ║\n           ║ a.Carnívoro Satánico $7.500 ║\n           ║ b.Vegano Exorcista   $6.000 ║\n           ║ c.Vegetariano Hereje $7.500 ║')
print('           ║                             ║\n           ╚═════════════════════════════╝\n')

quantity = int(input("\n\tPor favor, ingrese la cantidad de platos que desea llevar: "))
total = 0
while quantity > 0:
    pizza = input("\n\tEscribe la letra (a, b ó c) del plato que quieres: ")
    if pizza == "a":
        total += 7500
        print("\nHas seleccionado un plato Carnívoro Satánico por $7.500")
    elif pizza == "b":
        total += 6000
        print("\nHas seleccionado un plato Vegano Exorcista por $6.000")
    elif pizza == "c":
        total += 4800
        print("\nHas seleccionado un plato Vegetariano Hereje por $4.800")
    quantity -= 1

dscto = int(input("\n\tSi posee código de descuento de 3 dígitos, por favor, ingréselo: "))
if dscto == 666:
    total -= total*0.15
    print ("\nSe le ha aplicado un 15% de descuento")
    print (f'\n\n     .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.\n    (                                                             )\n     )             El total de su compra es ${total}         \n    (                                                             )\n     "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"\n\n\n')
else:
    print ("\nEl código ingresado no tiene descuento")
    print (f'\n\n     .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.\n    (                                                             )\n     )             El total de su compra es ${total}         \n    (                                                             )\n     "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"\n\n\n')
