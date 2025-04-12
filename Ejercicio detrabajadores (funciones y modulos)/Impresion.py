# Modulo 2

def impresion(trabajadores, personas_40_horas, promedio_horas_general):
    print("Las horas por proyecto de los trabajadores son:")
    print("*"*50)
    print("Nombre    hora1    hora2    hora3    sumatoria")
    for trabajador in trabajadores:
      print(f"{trabajador[0]:s}, {trabajador[1]:>8.1f}, {trabajador[2]:>8.1f}, {trabajador[3]:>7.1f}, {trabajador[4]:>6.1f}")
    print("*"*50)
    print("El promedio general de horas de los trabajadores es: ",promedio_horas_general)
    print("El numero de personas con mas de 40 horas en los tres proyectos es: ",personas_40_horas)
    