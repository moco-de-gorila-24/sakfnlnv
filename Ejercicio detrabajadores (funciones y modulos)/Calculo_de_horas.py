# Modulo 1
import Impresion as imp

def horas ():
    personas_40_horas = 0
    trabajador = ()
    trabajadores = []
    horas_totales = 0
    promedio_horas_general = 0
    
    
    num_trabajadores = int(input("Ingrese el numero de trabajadores: "))
    for i in range (1, num_trabajadores + 1):
        nombre = str(input(f"ingrese el nombre del trabajador {i} :"))
        hora1 = float(input("Ingrese el numero de horas trabajadas en el proyecto 1: "))
        hora2 = float(input("Ingrese el numero de horas trabajadas en el proyecto 2: "))
        hora3 = float(input("Ingrese el numero de horas trabajadas en el proyecto 3: "))
        sumatoria_horas = hora1 + hora2 + hora3
        if sumatoria_horas > 40:
            personas_40_horas +=1
        horas_totales +=sumatoria_horas
        promedio_horas_general = horas_totales / num_trabajadores
        
        trabajador = (nombre, hora1, hora2, hora3, sumatoria_horas)
        trabajadores.append(trabajador)
    imp.impresion(trabajadores, personas_40_horas, promedio_horas_general)
    
        
    

