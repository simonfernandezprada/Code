print ("\n\n                                  (* *)\n                          ---oOO-- (_) ----oOO---\n                     ╔════════════════════════════╗\n                     ║   Convertidor de Unidades  ║\n                     ╚════════════════════════════╝\n                           -----By Chulio-----\n                                 |__|__|\n                                  || ||\n                                 ooO Ooo ")
opcion = int(input("""
\n\n
        Si quieres convertir de USD a CLP ingresa 1
        Si quieres convertir de  UF a CLP ingresa 2
        Si quieres convertir de UTM a CLP ingresa 3

            Ingresa el número de tu opción: """))

valor_usd = 850
valor_uf = 28500
valor_utm = 50000

if opcion == 1:
    usd = float(input("\n\tIngresa la cantidad de USD que quieres convertir a CLP: "))
    print(f"\n\tUSD${usd} son ${valor_usd*usd} CLP")
if opcion == 2:
    uf = int(input("\n\tIngresa la cantidad de UF que quieres convertir a CLP: "))
    print(f"\n\t{uf} UF son ${valor_uf*uf} CLP")
if opcion == 3:
    utm = int(input("\n\tIngresa la cantidad de UTM que quieres convertir a CLP: "))
    print(f"\n\t{utm} UTM son ${valor_utm*utm} CLP")
