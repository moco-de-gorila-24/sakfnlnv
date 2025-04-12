#Ejercicio de diccionarios

grupo = {}
reprobados = 0
suma_promedios = 0

Alumnos = int(input("¿Cuantos alumnos hay en el grupo? "))
while Alumnos > 0:
    Alumnos -=1
    nombre = str(input("Ingrese el nombre del alumno: "))
    cal1 = float(input("Ingrese la calificacion 1: "))
    cal2 = float(input("Ingrese la calificacion 2: "))
    cal3 = float(input("Ingrese la calificacion 3: "))
    promedio = (cal1 + cal2 + cal3)/3
    if promedio < 7:
        reprobados += 1
    
    grupo[nombre] = (cal1, cal2, cal3, promedio)
    suma_promedios += promedio
    promedio_grupo = suma_promedios / len(grupo) if len(grupo) > 0 else 0
print("-"*44)
print("alumno    cal1    cal2    cal3    promedio ")
for nombre, datos in grupo.items():
    cal1, cal2, cal3, promedio = datos
    print(f"{nombre:<5} {cal1:>7.1f} {cal2:>7.1f} {cal3:>7.1f} {promedio:>8.1f}" )
print("-"*44)
print("El numero de reprobados es: ",reprobados," El promedio general es: ",f"{promedio_grupo:.1f}")