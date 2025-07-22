estudiantes =[]
curva= True
for i in range(5):
    nombre= input("Ingrese el nombre del estudiante: ")
    suma=0
    notas =[]
    for j in range(3):
        nota = float(input("Ingrese las notas del estudiante: "))
        notas.append(nota)
        suma += nota
    promedio = suma /3
    if promedio >= 70:
        curva = False
    estudiantes.append([nombre, notas])
if curva:
    for e in estudiantes:
        for i in range(3):
            e[i][1]=e[i][1]+5
            if e[i][1] >100:
                e[i][1] = 100
print("Tabla de estudiantes")
print("| Nombre | Promedio |")
print("-"*22)
for e in estudiantes:
    promedio = sum(e[1])/3
    print(f"|{e[0]:<8}|{promedio:>10.2f}|")
    print("-" * 22)