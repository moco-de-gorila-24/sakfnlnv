#Gestion de talleres

catalogo_talleres = {
        "1": {
            "Nombre": "Java desde 0",
            "Fecha": "2024-12-11",
            "Hora": "11:00",
            "Lugar": "AV-1825",
            "Duración": "2 horas",
            "Capacidad": "20",
            "Costo": "$600.00"
        },
        "2": {
            "Nombre": "Diseño de SW",
            "Fecha": "2024-12-10",
            "Hora": "10:00",
            "Lugar": "AV-1822",
            "Duración": "3 horas",
            "Capacidad": "25",
            "Costo": "$700.00"
        },
        "3": {
            "Nombre": "Algoritmos",
            "Fecha": "2024-12-12",
            "Hora": "11:00",
            "Lugar": "AV-1823",
            "Duración": "3 horas",
            "Capacidad": "25",
            "Costo": "$600.00"
        }  
    }

# Agregar un nuevo taller al catálogo
def agregar_taller(catalogo_talleres):
    print("\n--- Registro de un Nuevo Taller ---")
    while True:
        # Solicitar ID del taller
        id_taller = input("Ingrese el ID único del taller (o 'salir' para volver al menú): ").strip()
        if id_taller.lower() == 'salir':
            print("Regresando al Menú Principal...\n")
            break




        # Verificar si el ID existe
        if id_taller in catalogo_talleres:
            print("Error: El ID ingresado ya existe. Intente con otro.\n")
            continue




        # Datos del nuevo taller
        nombre = input("Nombre del taller: ").strip()
        fecha = input("Fecha (formato YYYY-MM-DD): ").strip()
        hora = input("Hora (formato HH:MM): ").strip()
        lugar = input("Lugar del taller: ").strip()
        duracion = input("Duración del taller (ejemplo: '2 horas'): ").strip()
        capacidad = input("Capacidad máxima de asistentes: ").strip()
        costo = input("Costo del taller: ").strip()


        # Confirmar si desea registrar el taller
        confirmacion = input("¿Desea registrar este taller? (S/N): ").strip().upper()
        if confirmacion == 'S':
            # Registrar el taller en el catálogo
            catalogo_talleres[id_taller] = {
                "Nombre": nombre,
                "Fecha": fecha,
                "Hora": hora,
                "Lugar": lugar,
                "Duración": duracion,
                "Capacidad": capacidad,
                "Costo": costo
            }
            print("\nTaller registrado exitosamente.\n")
        else:
            print("\nRegistro cancelado.\n")
            continue


        # Mostrar catálogo actualizado
        print("\n--- Catálogo Actualizado de Talleres ---")
        print(f"{'ID':<5}{'Nombre':<20}{'Fecha':<12}{'Hora':<10}{'Lugar':<15}{'Duración':<12}{'Capacidad':<10}{'Costo':<10}")
        print("-" * 90)
        for id, datos in sorted(catalogo_talleres.items()):
            print(f"{id:<5}{datos['Nombre']:<20}{datos['Fecha']:<12}{datos['Hora']:<10}{datos['Lugar']:<15}{datos['Duración']:<12}{datos['Capacidad']:<10}{datos['Costo']:<10}")
        print("-" * 90)


        # Preguntar si desea agregar otro taller
        continuar = input("¿Desea agregar otro taller? (S/N): ").strip().upper()
        if continuar != 'S':
            print("Regresando al Menú Principal...\n")
            break


