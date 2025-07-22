dia = int(input("Ingrese el día: "))
mes= int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
if bisiesto:
    dias_mes[1]=29
if 1 <dia > dias_mes[mes -1]:
    print("Dia invalido")
elif 1 < mes > 12:
    print("Mes invalido")
else:
    q = dia
    m = mes
    a= año
    if m < 3:
        m +=12
        a -=1
    K = a %100
    J = a //100
    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7
    dias = ["Sabado","Domingo","Lunes","Martes","Miercoles","Jueves","Viernes"]
    print(f"El {dia}/{mes}/{año} es el día {dias[h]}")