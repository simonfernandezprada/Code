import re

print("Crashy Calculator")
print("Escribe 'salir' para terminar este programa\n")
print("Usa + para sumar, - para restar, * para multiplicar, / para dividir y ** para potencias")
previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Ingresa una operación: ")
    else:
        equation = input(str(previous))
    if equation == 'salir':
        print ("\n¡Adios amigo!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()
