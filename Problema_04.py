"""""

Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.

"""""

alumnos = []

num_alumnos = int(input("Ingrese el número de alumnos: "))

for _ in range(num_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    
    notas = []
    
    for i in range(1, 4):
        nota = int(input(f"Ingrese la calificación {i} para {nombre}: "))
        notas.append(nota)
    
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    
    alumnos.append(alumno)

print("\nListado de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")