#asignacion 24 Cálculo de Inversión (version con for)

intereses = 1.03  #esta cantidad es por mes 
total_capital = 0
monto_interes = 0

continuar = str(input("¿Desea usar nuestro sevicio? "))
if continuar.lower() == "si":

    meses = int(input("¿Cuantos meses desea dejar su dinero en el banco? "))
    for mes in range(1,meses + 1):
        capital=float(input("Ingrese su cantidad en el mes {}: ".format(mes)))
        total_capital += capital
        monto_interes = (capital * intereses)
        print("-"*45)
        print("meses       capital       monto capital")
        print(mes, f"{capital:>14.1f}, {monto_interes:>13.1f}".format(mes))
        print("-"*45)

    print("-" * 45)
    print(f"Total después de {meses} meses: {total_capital * intereses:>14.2f}")
    print("-" * 45)
    
else:
    print("Gracias por su tiempo")