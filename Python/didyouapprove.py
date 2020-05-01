print("Ingresa 3 notas sin comas (ej: 70, 40, 63) y te diremos si aprobaste o reprobaste")
a1 = int(input("ingresa tu primera calificación: "))
a2 = int(input("ingresa tu primera calificación: "))
a3 = int(input("ingresa tu primera calificación: "))

average = (a1+a2+a3)/3
if average >= 40:
    print(f"Pasaste, puedes respiar tranquilo. Tu promedio es {average}")
else:
    print(f"Fracasaste, nos vemos el próximo semestre. Tu promedio es {average}")