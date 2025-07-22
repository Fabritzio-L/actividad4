estudiantes =[]
promedios = []
for i in range(5):
    nombre= input("Ingrese el nombre del estudiante: ")
    suma=0
    notas =[]
    for j in range(3):
        nota = int(input("Ingrese las notas del estudiante: "))
        notas.append(nota)
        suma += nota
    promedio = suma /3
