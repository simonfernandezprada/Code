# Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el
# sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida
# por pantalla.

nombres = []

while len(nombres) < 3:
    x = input("Escribe tu nombre mi hermano banano: ")
    nombres.append(x)
print (max(nombres, key=len))
