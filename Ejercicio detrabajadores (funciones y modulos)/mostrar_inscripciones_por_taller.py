def mostrar_inscripciones_por_taller(folio_inscripciones):
    print("\n--- Listado de Inscripciones por Taller ---")
    for id_taller, lista_participantes in folio_inscripciones.items():
        print(f"\nTaller ID: {id_taller}")
        print(f"{'Folio':<10}{'Nombre':<20}")
        print("-" * 30)
        for participante in lista_participantes:
            print(f"{participante['Folio']:<10}{participante['Nombre']:<20}")
        print("-" * 30)
