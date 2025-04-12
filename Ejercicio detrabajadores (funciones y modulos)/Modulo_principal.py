#Modulo principal
import Calculo_de_horas as ch

while True:
    opcion = str(input("¿Desea añadir las horas de trabajadores? si/no "))
    if opcion.lower() == "si":
        ch.horas()
    elif opcion.lower() == "no":
        print("saliendo del sistema...")
        break
    elif opcion.lower() != "si" or "no":
        print("Ingrese alguna de las dos opciones")
        continue