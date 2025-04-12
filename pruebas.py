# Definición de la función para calcular el promedio
def Calificaciones(cal1, cal2, cal3):
    return (cal1 + cal2 + cal3) / 3

# Definición de la función para buscar un alumno
def buscar_alumno(id_alumno, grupo):
    for alumno in grupo:
        if alumno[1] == id_alumno:
            return alumno  # Devuelve el alumno completo
    return "Alumno no encontrado"

# Lista para almacenar los alumnos y contador de reprobados
grupo = []
reprobados = 0

while True:
    print("-" * 44)
    print("Presiona 1 para agregar un alumno")
    print("Presiona 2 para buscar un alumno")
    print("Presiona 3 para solicitar los datos del alumno")
    print("Presiona 0 para detener")
    dato = int(input())

    if dato == 1:
        print("Estás en la opción 1")
        nombre = input("Ingrese el nombre del alumno: ")
        id_alumno = int(input("Ingrese el ID del alumno: "))

        # Verificar si el ID ya está registrado
        for alumno in grupo:
            if alumno[1] == id_alumno:
                print("No puede registrar dos alumnos con el mismo ID")
                break
        else:  # Solo si no se ha encontrado un ID duplicado
            cal1 = float(input("Ingrese la calificación 1: "))
            cal2 = float(input("Ingrese la calificación 2: "))
            cal3 = float(input("Ingrese la calificación 3: "))

            promedio = Calificaciones(cal1, cal2, cal3)
            alumno = (nombre, id_alumno, cal1, cal2, cal3, promedio)
            grupo.append(alumno)

            # Contabilizar reprobados
            if promedio < 7:
                reprobados += 1

    elif dato == 2:
        if len(grupo) == 0:
            print("Aún no se han registrado alumnos.")
        else:
            print("Estás en la opción 2")
            busqueda_id = int(input("Ingrese el ID del alumno: "))
            alumno_encontrado = buscar_alumno(busqueda_id, grupo)
            if alumno_encontrado == "Alumno no encontrado":
                print(alumno_encontrado)
            else:
                print("Datos del alumno encontrado:")
                print(f"Nombre: {alumno_encontrado[0]}")
                print(f"ID: {alumno_encontrado[1]}")
                print(f"Calificaciones: {alumno_encontrado[2]}, {alumno_encontrado[3]}, {alumno_encontrado[4]}")
                print(f"Promedio: {alumno_encontrado[5]}")

    elif dato == 3:
        if len(grupo) == 0:
            print("Aún no se han registrado alumnos.")
        else:
            print("Estás en la opción 3")
            print("Datos de todos los alumnos:")
            print("*" * 44)
            print("Nombre       ID    Cal1   Cal2   Cal3   Promedio")
            for alumno in grupo:
                print(f"{alumno[0]:<12} {alumno[1]:<5} {alumno[2]:<6} {alumno[3]:<6} {alumno[4]:<6} {alumno[5]:<6.2f}")
            print(f"El número de reprobados es: {reprobados}")
            print("*" * 44)

    elif dato == 0:
        print("Fin del programa")
        break

    else:
        print("Seleccione un número de los mostrados en el menú")
