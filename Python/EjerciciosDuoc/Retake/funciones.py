#Filtra el rut omitiendo cualquier otro caracter que no incluido en 'caracteres'.
def filtra(rut):
    caracteres = "1234567890k"
    rutx = ""
    for cambio in rut.lower():
        if cambio in caracteres:
            rutx += cambio
    return rutx

# Esta funcion cumple el trabajo de validar el rut utilizando el mod 11
def valida(rut):
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
        retorno = "Valido"
    else:
        retorno = "Invalido"
    return retorno

def menu():
    paci = [[],[],[],[],[]]
    opc = 0
    sys = True
    while sys == True:
        try:
            opc = int(input("""
          M  E  N  U

    1. Registrar Paciente
    2. Consultar Pacientes
    3. Salir

    Seleccione un opción 1-3: """))
        except:
            print("\n* * * Opción no válida * * *")
        if opc > 3 or opc <1:
            print("* ¡Sólo números del 1 al 3!*\n*  *  *  *  *  *  *  *  *  * ")
        elif opc == 1:
            try:
                n = input("Ingrese primer y segundo nombre del paciente: ")
            except:
                print("Solo letras")
            paci[0].append(n)
            a = input("Ingrese apellidos paterno y materno del paciente: ")
            paci[1].append(a)
            r = input("Ingrese el rut del paciente CON digito verificador: ")
            #Checar si rut es válido
            valida(r)
            paci[2].append(r)
            e = int(input("Ingrese edad del paciente en numeros: "))
            #Checar que edad sea un numero entero mayor a cero
            while e<1:
                try:
                    print("Edad del paciente debe ser un numero mayor a cero")
                    e = int(input("Ingrese edad del paciente en numeros: "))
                except:
                    print("¡Ingresa solo números!")
            paci[4].append(e)
        elif opc == 2:
            b = int(input("Ingrese el rut del paciente SIN digito verificador: "))
            d = input("Ingrese el digito verificador del rut del paciente: ")
            #Buscar rut en lista
        elif opc == 3:
            sys = False
    print("¡Hasta pronto!")
