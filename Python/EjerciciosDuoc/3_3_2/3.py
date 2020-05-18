# Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre nuevo, el sistema
# preguntará si desea agregar otro nombre, deberá agregar nombres hasta que la respuesta sea “no”,
# “No”, “nO” o “NO” (use funciones lower() y upper() ) .
# Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.

nombres = []
mas = False
while mas == False:
    x = input("Escribe un nombre: ")
    nombres.append(x)
    respuesta = input("¿Desea agregar otro nombre? \nPara continuar presione enter \nPara dejar de ingresar nombres escribe NO: ")
    negacion = respuesta.upper()
    negacion = respuesta.lower()
    if negacion == "no":
        mas = True
n = len(nombres)
print(f" n es igual a {n}, por eso eliminaremos el nombre con la menor cantidad de caracteres")
print(f"Los nombres ingresados son: {nombres}")
nombres.remove(min(nombres, key=len))
print(f"El nombre más corto ha sido eliminado. \nLos nombres ahora son: {nombres}")
