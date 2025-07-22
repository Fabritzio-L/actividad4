dia = int(input("Ingrese el día: "))
mes= int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
if bisiesto:
    dias_mes[1]=29
if 1 <dia < dias_mes[mes -1]:
    print("Dia invalido")
elif 1 < mes < 12:
    print("Mes invalido")
else:
    q = dia
    m = mes
    a= año
