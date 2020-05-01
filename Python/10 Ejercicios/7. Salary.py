print("Calculemos cuanto dinero te corresponde. \nPara esto necesitaremos la cantidad de horas que has trabajado y el costo por hora. \nPor favor, ingresa tu cantidad de horas trabajadas ")
q = int(input())

print("Ahora ingresa el costo en pesos, por hora")
h = int(input())

t = h*q
print(f"La suma que te corresponde asciende a ${t}.-")