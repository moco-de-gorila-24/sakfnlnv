"""
Asignación 29: Uso de funciones en python (caso listado de calificaciones)
menu de datos 
"""
def Calificaciones(cal1, cal2, cal3):
      return (cal1 + cal2 + cal3)/3

def buscar_alumno (id_alumno):
      for alumno in grupo:
        if alumno[1] == busqueda_id:
          return alumno[0]      
      return "Alumno no encontrado"

grupo = []
alumno = ()
alumnos = []
reprobados = 0
nombre = ""

while True:
  print("-"*44)
  print("Preciona 1 para agregar un alumno")
  print("Preciona 2 para buscar un alumno")
  print("Preciona 3 para solicitar los datos del alumno")
  print("preciona 0 para detener")
  dato = int(input())

  if dato == 1:
    print("Esta en el dato 1")
    nombre = input("Ingrese el nombre del alumno:")
    id_alumno = int(input("Ingrese el id del alumno:"))
    for alumno in grupo:
      if alumno[1] == id_alumno:
        print("No puede registrar dos alumnos con el mismo ID")
        break
    else:
      cal1 = float(input("Ingrese la calificacion 1: "))
      cal2 = float(input("Ingrese la calificacion 2: "))
      cal3 = float(input("Ingrese la calificacion 3: "))

      promedio = Calificaciones (cal1 ,cal2 ,cal3)

      alumno = (nombre, id_alumno, cal1, cal2, cal3, promedio)
      grupo.append(alumno)
      if promedio < 7:
        reprobados += 1

  elif dato == 2:
    if nombre == "" :
      print("Aun no registro un alumno")
      continue 

    print("Esta en el dato 2")
    busqueda_id = int(input("Ingrese el id del alumno que desea buscar: "))
    alumno_encontrado = buscar_alumno (id_alumno)
    print(alumno_encontrado)

  elif dato == 3:
    if nombre == "" :
      print("Aun no registro un alumno")
      continue

    print("Esta en el dato 3")
    print("Los datos del alumno son:")
    print("*"*44)
    print("Nombre  ID    cal1    cal2    cal3    promedio")
    for alumnos in grupo:
      print(alumnos[0], f"{alumnos[1]:>5.1f}, {alumnos[2]:>5.1f}, {alumnos[3]:>6.1f}, {alumnos[4]:>6.1f}, {alumnos[5]:>6.1f}")
    print("EL numero de reprobados es: ",reprobados)
    print("*"*44)
    
  elif dato == 0:
        print("ya es toda we")
        break
  elif dato != 1 or 2 or 3 or 0:
    print ("Selecione un numero de los mostrados en el menu")

