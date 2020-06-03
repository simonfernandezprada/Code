#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
palabras = []
continuar = 1
while continuar == 1:
    nuevaPalabra = input("Ingrese una palabra: ")
    palabras.append(nuevaPalabra)
    existencia = palabras.count(nuevaPalabra)
    print(f"La palabra {nuevaPalabra} se encuentra {existencia} veces en la lista")
    continuar = int(input("Para seguir agregando palabras ingrese el 1, para dejar de ingresar palabras ingrese cualquier otro número: "))
