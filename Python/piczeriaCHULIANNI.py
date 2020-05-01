print('           ╔═══════════════════════════╗\n           ║                           ║\n           ║    Piczería  CHULIANNI    ║\n           ║                           ║\n           ║                           ║\n           ║          M E N U          ║\n           ║                           ║\n           ║ a.Pizza Fiorina    $6.500 ║\n           ║ b.Pizza Napolitana $6.000 ║\n           ║ c.Pizza Firenze    $7.500 ║')
print('           ║ d.Pizza Simple     $5.000 ║\n           ║                           ║\n           ╚═══════════════════════════╝\n')

quantity = int(input("Por favor, ingrese la cantidad de picsas que desea llevar: "))
total = 0
while quantity > 0:
    pizza = input("\nEscribe la letra (a, b, c ó d) de la picsa que quieres: ")
    if pizza == "a":
        total += 6500
        print("\nHas seleccionado una Pizza Fiorina $6.500")
    elif pizza == "b":
        total += 6000
        print("\nHas seleccionado una Pizza Napolitana $6.000")
    elif pizza == "c":
        total += 7000
        print("\nHas seleccionado una Pizza Firenze $7.000")
    elif pizza == "d":
        total += 5000
        print("\nHas seleccionado una Pizza Simple $5.000")
    quantity -= 1


print (f'\n\n     .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.\n    (                                                             )\n     )             El total de su compra es ${total}         \n    (                                                             )\n     "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"\n\n\n')
