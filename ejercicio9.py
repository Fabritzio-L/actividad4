dia= input("¿Que dia de la semana es?: ").lower()
edad= int(input("Ingrese su edad: "))
estudiante= input("¿Usted es estudiante?: ")
clasificacion = int(input("Ingrese la clasificación de la pelicula: "))
if edad< 13 and clasificacion > 15:
    print("No puede ver esta pelicula, no cumple con la edad minima.")
else:
    precio = 50
    precio_estudiantes= 35
    precio_final=0
    if dia == "miercoles" or dia == "miércoles":
        print("2x1 el día de hoy")
        if estudiante== "si" or estudiante =="sí":
            precio_final = precio_estudiantes
        else:
            precio_final = precio
        print(f"Paga {precio_final} por dos entradas")
    else:
        if estudiante== "si" or estudiante =="sí":
            precio_final = precio_estudiantes
        else:
            precio_final = precio
            print(f"Cumple los requisitos, total a pagar: {precio_final}")