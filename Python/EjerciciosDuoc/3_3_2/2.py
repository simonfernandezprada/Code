# Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para
# apellidos), el sistema deberá mostrar de forma ordenada los nombres y apellidos.

nombres = []
while len(nombres) < 3:
    x = input("Escribe un nombrecito: ")
    nombres.append(x)
apellidos = []
while len(apellidos) < 3:
    y = input("Escribe un apellidou: ")
    apellidos.append(y)

print (f"{nombres[0]} {apellidos[0]}\n{nombres[1]} {apellidos[1]}\n{nombres[2]} {apellidos[2]}")
