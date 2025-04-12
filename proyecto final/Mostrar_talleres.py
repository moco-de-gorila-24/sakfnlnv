# Función para actualizar los datos de un taller
def actualizar_taller(catalogo_talleres):
    print("\n--- Actualizar Datos de un Taller ---")
    while True:
        # Solicitar el ID del taller a actualizar
        id_taller = input("Ingrese el ID del taller que desea actualizar (o 'salir' para volver al menú): ").strip()
        if id_taller.lower() == 'salir':
            print("Regresando al Menú Principal...\n")
            break


        # Verificar si el ID existe
        if id_taller in catalogo_talleres:
            # Mostrar información actual del taller
            taller = catalogo_talleres[id_taller]
            print("\n--- Datos Actuales del Taller ---")
            print(f"ID: {id_taller}")
            print(f"Nombre: {taller['Nombre']}")
            print(f"Fecha: {taller['Fecha']}")
            print(f"Hora: {taller['Hora']}")
            print(f"Lugar: {taller['Lugar']}")
            print(f"Duración: {taller['Duración']}")
            print(f"Capacidad Máxima: {taller['Capacidad']}")
            print(f"Costo: {taller['Costo']}\n")


            # Menú para seleccionar el campo que se actualizara
            print("¿Qué dato desea actualizar?")
            print("1. Nombre")
            print("2. Fecha")
            print("3. Hora")
            print("4. Lugar")
            print("5. Duración")
            print("6. Capacidad")
            print("7. Costo")
            opcion = input("Seleccione una opción (1-7): ").strip()


            # Actualizar el campo que se seleecciono
            if opcion == '1':
                taller['Nombre'] = input("Nuevo nombre: ").strip()
            elif opcion == '2':
                taller['Fecha'] = input("Nueva fecha (YYYY-MM-DD): ").strip()
            elif opcion == '3':
                taller['Hora'] = input("Nueva hora (HH:MM): ").strip()
            elif opcion == '4':
                taller['Lugar'] = input("Nuevo lugar: ").strip()
            elif opcion == '5':
                taller['Duración'] = input("Nueva duración (ejemplo: '2 horas'): ").strip()
            elif opcion == '6':
                taller['Capacidad'] = input("Nueva capacidad máxima: ").strip()
            elif opcion == '7':
                taller['Costo'] = input("Nuevo costo: ").strip()
            else:
                print("Opción no válida. No se realizó ninguna actualización.\n")
                continue


            print("\nDatos del taller actualizados exitosamente.\n")
        else:
            print("No se encontró un taller con ese ID. Intente nuevamente.\n")


        # Preguntar si desea actualizar otro taller
        continuar = input("¿Desea actualizar otro taller? (S/N): ").strip().upper()
        if continuar != 'S':
            print("Regresando al Menú Principal...\n")
            break
