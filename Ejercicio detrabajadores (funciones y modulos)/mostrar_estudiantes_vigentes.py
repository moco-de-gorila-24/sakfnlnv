def mostrar_estudiantes_vigentes(folio_inscripciones):
    print("\n--- Listado de Estudiantes Vigentes ---")
    print(f"{'Folio':<10}{'Nombre':<20}{'Taller ID':<10}")
    print("-" * 40)
    for id_taller, lista_participantes in folio_inscripciones.items():
        for participante in lista_participantes:
            print(f"{participante['Folio']:<10}{participante['Nombre']:<20}{id_taller:<10}")
    print("-" * 40)
