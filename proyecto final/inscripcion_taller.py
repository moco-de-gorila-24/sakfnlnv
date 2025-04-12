#registrar inscripciones al taller

catalogo_estudiantes = (
    ("00000565676", "Juan Castelo Ruiz", "juan.castelo@gmail.com", "64412324252", "Si"),
    ("00000565687", "Julio López Estrada", "julio.lop@gmail.com", "6441750026", "No"),
    ("00000565693",	"Jhoana Madrigal Castro", "j.mcastro@gmail.com", "6441762499", "No"),
    ("00000565699",	"Michelle Perez Ion", "mperezi18@gmail.com", "6441782400", "No"),
    ("00000565703",	"Andres Pacheco Solis", "pacheco7659@gmail.com", "6441982411", "No"),
    ("00000565733", "Antonio García Tineo",	"antoniogtineo@gmail.com", "6441652422", "No"),
    ("00000565754",	"Perla Esquer Vega", "perlita19obr@gmail.com", "6441882433", "Si"),
    ("00000565798",	"Maritza Vega Ruiz", "mvegaruiz@gmail.com",	"6441006515", "Si"),
    ("00000565856",	"Héctor Figueroa Ozuna", "hfigue22@gmail.com", "6441552477", "No"),
    ("00000565887",	"Francisco Sauceda Vega", "fco.sauceda@hotmail.com", "6441332474", "No"),
    ("00000565895",	"Patricia Estrella Sonora",	"paty19son@gmail.com", "6441008899", "No"),
    ("00000565907",	"Juana Escalante Ian", "juanita43@gmail.com", "6441006532",	"No"),
    ("00000565932",	"Kevin Sotelo Duarte", "kevinsotelo@gmail.com",	"6441875498", "Si"),
    ("00000565996",	"Carlos Zamudio Soto", "zamudioobr@gmail.com", "6441234565", "No"),
    ("00000565998",	"Yolanda Valdez Osuna", "yolyvaldez18@gmail.com", "6441985410",	"No"),
    ("00000566006",	"Amalia Miranda Soqui",	"amaliamir2005@gmail.com",	"6441094387", "Si"),
    ("00000566178",	"Pedro Hernandez Silva", "pedrosilva2@gmail.com", "6441121233",	"No"),
    ("00000566197",	"Catalina Mungaro Velez", "caty.m.v@gmail.com",	"6441767676", "No")
)   
def inscripcion_talleres (catalogo_estudiantes):
    folio_inscripcion = {}
    
    
    
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
    print("\n--- Catálogo de Talleres ---")
    print(f"{'ID':<5}{'Nombre':<20}{'Fecha':<12}{'Hora':<10}{'Lugar':<15}{'Duración':<12}{'Capacidad':<10}{'Costo':<10}")
    print("-" * 90)
    for id, datos in sorted(catalogo_talleres.items()):
        print(f"{id:<5}{datos['Nombre']:<20}{datos['Fecha']:<12}{datos['Hora']:<10}{datos['Lugar']:<15}{datos['Duración']:<12}{datos['Capacidad']:<10}{datos['Costo']:<10}")
    print("-" * 90)
   
   
    while True:
        id_taller = str(input("¿A que taller desea inscribirse? "))
        if id_taller in catalogo_talleres:
            for id, datos in sorted(catalogo_talleres.items()):
                if id == id_taller:
                    print("Talleres disponibles")
                    print("-" * 90)
                    print(f"{'ID':<5}{'Nombre':<20}{'Fecha':<12}{'Hora':<10}{'Lugar':<15}{'Duración':<12}{'Capacidad':<10}{'Costo':<10}")
                    print(f"{id:<5}{datos['Nombre']:<20}{datos['Fecha']:<12}{datos['Hora']:<10}{datos['Lugar']:<15}{datos['Duración']:<12}{datos['Capacidad']:<10}{datos['Costo']:<10}")
                    print("-" * 90)
    
                    fecha_inscripcion = int(input("Ingrese la fecha de inscripcion del estudiante en el formato: año-mes-dia " ))
                     
                    id_estudiante = str(input("Ingrese el ID con los ceros del estudiante inscrito"))
                    for i in catalogo_estudiantes:
                        if i == id_estudiante:
                            print(i)
                    
                    
                    
        else:
            print("Este id no existe, ingrese uno mostrado en el catalogo")
                
