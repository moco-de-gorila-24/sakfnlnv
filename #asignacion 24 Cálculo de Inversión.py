#asignacion 24 Cálculo de Inversión


intereses = 1.03  #esta cantidad es por mes 
continuacion = ""

continuacion = str(input("¿Desea invertir su capital?")).lower()
while continuacion == "si":

    capital=float(input("Ingrese su cantidad inicial: "))
    meses = float(input("Ingrese el numero de meses "))
    continuacion = str(input("¿Desea continuar?"))
    monto_interes = (capital*intereses)
print("-"*45)
print("meses       capital       monto capital")
print(meses, f"{capital:>14.1f}, {monto_interes:>13.1f}")
print("-"*45)

