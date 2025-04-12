#Asignación 27: Uso de listas en Python (while)
grupo = []
alumnos = []
reprobados = 0
Alumnos = 1
suma_promedios = 0
i = 0
while Alumnos > 0:
    Alumnos -=1
    nombre = str(input("Ingrese el nombre del alumno: "))
    cal1 = float(input("Ingrese la calificacion 1: "))
    cal2 = float(input("Ingrese la calificacion 2: "))
    cal3 = float(input("Ingrese la calificacion 3: "))
    promedio = (cal1 + cal2 + cal3)/3
    if promedio < 7:
        reprobados += 1

    alumnos = [nombre, cal1, cal2, cal3 , promedio]
    grupo.append(alumnos)

print("-"*44)
print("alumno    cal1    cal2    cal3    promedio ")

while i < len(grupo):
    alumno = grupo[i]
    print(f"{alumno[0]:<10} {alumno[1]:>2.2f} {alumno[2]:>6.2f} {alumno[3]:>6.2f} {alumno[4]:>9.2f}")

    i += 1
while i < len(grupo):
    suma_promedios += grupo[i][4] 
    i += 1
print("-"*44)
promedio_general = suma_promedios / len(grupo) if grupo else 0
print(f"\nPromedio general de todos los alumnos: {promedio_general:.2f}")
print(f"Cantidad de alumnos reprobados: {reprobados}")