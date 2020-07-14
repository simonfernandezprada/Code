import numpy as np
import random
np.pers = []

# Filtra el rut omitiendo cualquier otro caracter que no incluido en 'caracteres'.
def filtra(rut):
    caracteres = "1234567890k"
    rutx = ""
    for cambio in rut.lower():
        if cambio in caracteres:
            rutx += cambio
    return rutx

# Esta función revisa que el nombre tenga al menos 3 caracteres
def largo():
    global n
    while len(n) < 3:
        print("Nombre demasiado corto. Inténtalo una vez más.")
        n = input("Ingrese primer y segundo nombre: ")
    else:
        print(f"El nombre: {n} ha sido guardado con éxito")

# Esta Función revisa que la edad sea mayor que cero
def edadMayorQueCero():
    global e
    while e<=0:
        try:
            e = int(input("Ingrese edad de la persona en numeros: "))
        except:
            print("¡Ingresa solo números!\nEdad de la persona debe ser un numero igual o mayor a cero")

#Esta función registra personas al sistema
def registrar():
    global n
    global e
    validrut = False
    while validrut == False:
        rut = input("Ingrese rut SIN espacios ni puntos ni guión: ")
        if len(rut)<9:
            print("Rut inválido, Ingrese un Rut válido.")
            validrut = False
        elif len(rut)>8:
            rfiltro = filtra(rut)
            rutx = str(rfiltro[0:len(rfiltro)-1])
            digito = str(rfiltro[-1])
            multiplo = 2
            total = 0
            for reverso in reversed(rutx):
                total += int(reverso) * multiplo
                if multiplo == 7:
                    multiplo = 2
                else:
                    multiplo += 1
                modulus = total % 11
                verificador = 11 - modulus
                if verificador == 10:
                    div = "k"
                elif verificador == 11:
                    div = "0"
                else:
                    if verificador < 10:
                        div = verificador
            if str(div) == str(digito):
                validrut = True
            else:
                print(f"El rut ingresado {rutx} no es válido")
                validrut = False
    np.pers.append(rut)
    n = input("Ingrese primer y segundo nombre de la persona: ")
    largo()
    np.pers.append(n)
    a = input("Ingrese apellidos paterno y materno de la persona: ")
    np.pers.append(a)
    e = -1
    edadMayorQueCero()
    np.pers.append(e)
    print(f"El usuario {n} {a}, de rut {rut} y de {e} años de edad, ha sido registrado.")

def imprimir():
    search = input("Ingresa el rut SIN espacios ni puntos ni guión para imprimir certificado: ")
    search = str(search)

    if search in np.pers:
        xxx = random.randint(1,4)
        if xxx == 2:
            print("Certificado de Nacimiento: Usted nació.")
        elif xxx == 3:
            print("Certificado de Antecedentes: Usted no ha cometido delitos.")
        elif xxx == 4:
            print("Certificado de Defunción: Usted aún no ha muerto, váyase.")
        else:
            print("Certificado de Nacimiento: Felicidades, usted nació.")
    else:
        print("Rut no encontrado en los registros")

#Esta función busca a la persona registrada por rut
def buscar():
    bsq = input("Para buscar, ingrese el rut SIN espacios ni puntos ni guión: ")
    if bsq in np.pers:
        indice = np.pers.index(bsq)
        nobd = indice + 1
        nbd = np.pers[nobd]
        aobd = indice + 2
        abd = np.pers[aobd]
        eobd = indice + 3
        ebd = np.pers[eobd]
        if ebd > 17:
            print(f"{nbd} {abd} de {ebd} de edad puede obtener licencia de conducir")
        else:
            print(f"{nbd} {abd} de {ebd} de edad NO puede obtener licencia de conducir")
    else:
        print("Rut no encontrado en los registros")


# Esta función despliega el menu del programa
def menu():
    opc = 0
    sys = True
    while sys == True:
        try:
            opc = int(input("""
          M  E  N  U

    1. Registrar Persona
    2. Buscar Persona
    3. Imprimir certificado
    4. Salir

    Seleccione un opción 1-4: """))
        except:
            print("\n* * * Opción no válida * * *")
        if opc == 1:
            registrar()
        if opc == 2:
            buscar()
        if opc == 3:
            imprimir()
        if opc == 4:
            print("\n\t¡Hasta pronto!")
            sys = False
