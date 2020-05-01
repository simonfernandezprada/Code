preg1 = ("\nAl realizar viajes largos es aconsejable que el conductor descanse 10 min por cada 2 horas. \nSi el tiempo de viaje sin descansar entre 2 ciudades es de 8 horas ¿qué tiempo ocuparía acogiendo la sugerencia?")
alte1 = ("\n\na  8h\nb  8h 30 min\nc  8h 40 min\nd  9h 20 min")
preg2 = ("\n¿Cuál de estas alternativas es un sustantivo colectivo?")
alte2 = ("\n\na  privilegio\nb  banco\nc  esrella\nd  alamoso")
preg3 = ("\n¿Qué es UMAMI?")
alte3 = ("\n\na  el apellido de Kin Jong Un\nb  la capital de Mongolia\nc  una palabra ninja\nd  un sabor")

print ("Bienvenido a tu evaluación")
print ("\nItem I. Selección múltiple. \nEscribe la letra a, b, c, ó d de la alternativa que consideres correcta. \t\t\t__ / 9pts")

p1 = input(f"{preg1}{alte1}\n\nPresiona a, b, c o d y luego enter: ")
r = 0
if p1 == "c":
    r = r + 3
else:
    r = r + 0

p2 = input(f"{preg2}{alte2}\n\nPresiona a, b, c o d y luego enter: ")
if p2 == "b":
    r = r + 3
else:
    r = r + 0

p3 = input(f"{preg3}{alte3}\n\nPresiona a, b, c o d y luego enter: ")
if p3 == "d":
    r = r + 3
else:
    r = r + 0

if r == 0:
    print(f"\nSu puntaje obtenido es {r}. Su calificación es 1.0")
elif r == 3:
    print(f"\nSu puntaje obtenido es {r}. Su calificación es 2.7")
elif r == 6:
    print(f"\nSu puntaje obtenido es {r}. Su calificación es 4.5")
elif r == 9:
    print(f"\nSu puntaje obtenido es {r}. Su calificación es 7.0. ¡Felicitaciones!")
