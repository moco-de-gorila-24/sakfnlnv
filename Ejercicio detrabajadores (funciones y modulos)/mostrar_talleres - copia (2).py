#Mostrar talleres 

def mostrar_talleres(catalogo_talleres):
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
    while True:
        dato = str(input("¿Que datos desea que se muestren? (I=ID, D=Duracion, L=Lugar,C=costo)"))
        if dato.lower() != "i" or "d" or "l" or "c":
            print("ingrese un dato valido ")
            continue
        orden = str(input("¿En que orden desea que se muestre (A=Acendente, D=Decendente)"))
        if orden.upper() != "A" or "D":
            print("Ingrese un dato valido")
            continue
        
        if orden.upper() == "A":
            print("Mostrando en orden acendente")
            print("\n--- Datos de los Talleres ---")
            if dato.lower() == "i":
                print("ID de los talleres:")
                for id in sorted(catalogo_talleres):
                    print(id)
            elif dato.lower() == "d":
                print("Duracion de los talleres:") 
                for id, dato in sorted(catalogo_talleres.items(),key= lambda item: item[1]["Duración"]):
                    print(dato["Duración"])  
            elif dato.lower() == "l":
                print("Lugares donde se llevaran a cabo:")
                for id, dato in sorted(catalogo_talleres.items(), key= lambda item: item[1]["Lugar"]):
                    print(dato["Lugar"])
            elif dato.lower() == "c":
                print("Costo de los talleres:")
                for id, dato in sorted(catalogo_talleres.items(), key= lambda item: item[1]["Costo"]):
                    print(dato["Costo"])
            
        elif orden.upper() == "D":
            print("Mostrando en orden decendente")
            if dato.lower() == "i":
                print("ID de los talleres")
                for id in sorted(catalogo_talleres, reverse= True):
                    print(id)
            elif dato.lower() == "d":
                print("Duracion de talleres:")
                for id, dato in sorted(catalogo_talleres.items(),key= lambda item: item[1]["Duración"], reverse= True):
                    print(dato["Duración"])
            elif dato.lower() == "l":
                print("Mostrando lugares donde se llevaran a cabo:")
                for id, dato in sorted(catalogo_talleres.items(),key= lambda item: item[1]["Lugar"], reverse= True):
                    print(dato["Lugar"])
            elif dato.lower() == "c":
                print("Costo de los talleres:")
                for id, dato in sorted(catalogo_talleres.items(),key= lambda item: item[1]["Costo"], reverse= True):
                    print(dato["Costo"])
                    
            
            