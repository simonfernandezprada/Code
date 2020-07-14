def sumar(var1, var2):
    var3=var1+var2
    return(var3)

resultado=sumar(4,3)
print(resultado)

def restar(var1,var2):
    print(var1-var2)

restar(2,1)

def multiplicar():
    var1 = int(input(">>>"))
    var2 = int(input(">>>"))
    var3 = var1*var2
    return(var3)

resultado = multiplicar()
print(f"Resultado: {resultado}")

def dividir():
    var1 = int(input(">>>"))
    var2 = int(input(">>>"))
    print(var1/var2)

dividir()
