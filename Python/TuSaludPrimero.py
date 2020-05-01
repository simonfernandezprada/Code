
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
hour = now.strftime("%H")
minute = now.strftime("%M")

habil = print("Hábil")
inhabil = print("Inhabil")
if now.strftime("%H") >= 8 and now.strftime("%H") < 20:
    schedule = habil()
else: 
    schedule = inhabil()

print(f"Bienvenidos a Clinica Tu Salud Primero. Son las {current_time}. Es horario de atención es {schedule} Por favor, ingrese la edad del paciente")
age = int(input())


