#Asignación 27 Uso de listas en Python (for)
grupo = []
calificaciones = []
reprobados = 0

n_alumnos = int(input("¿Cuantos alumnos hay en su grupo?"))
for i in range (1,n_alumnos + 1):
    
    for m in range (1,4):
        calificaciones.append(float(input(f"Ingrese la calificacion {m} del alumno {i}: ")))
        promedio = sum(calificaciones) / len(calificaciones)
        if promedio < 7:
            reprobados += 1
    grupo.append(calificaciones + [promedio])


print(grupo)
print("-" * 44)
print("alumno    cal1    cal2    cal3    promedio ")
for i, calificaciones in enumerate(grupo, start=1):
    print(f"{i:<7}  {calificaciones[0]:<5}  {calificaciones[1]:<5}  {calificaciones[2]:<5}  {calificaciones[3]:<9.2f}")
print("-" * 44)
print("Total de alumnos reprobados:" ,reprobados)