#Eliminar una inscripcion por folio 
folio_inscripcion = {}

import inscripcion_taller as it 

def eliminar_inscripcion(folio_inscripcion):
    print("Lista de inscripciones a talleres")
    print("-----------------------------------------------------------------------")
    print(f"{'Folio':<8}{'Taller':<10}{'Id Estudiante':<18}{'Nombre estudiante':<22}{'costo':<10}")
    for id, dato in folio_inscripcion:
        print(f"{id:<8}{dato['fecha']:<10}{dato['ID']}")