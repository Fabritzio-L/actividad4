print("Fecha 1")
dia_1= int(input("Ingrese el dia: "))
mes_1= int(input("Ingrese el mes: "))
año_1= int(input("Ingrese el año: "))
print("Fecha 2")
dia_2 = int(input("Ingrese el dia: "))
mes_2 = int(input("Ingrese el mes: "))
año_2 = int(input("Ingrese el año: "))
if año_1 > año_2:
    mayor = "Fecha 1 es mayor"
elif año_1 < año_2:
    mayor = "Fecha 2 es mayor"
else:
    if mes_1 > mes_2:
        mayor = "Fecha 1 es mayor"
    elif mes_1 < mes_2:
        mayor= "Fecha 2 es mayor"
    else:
        if dia_1 > dia_2:
            mayor = "Fecha 1 es mayor"
        elif dia_1 < dia_2:
            mayor = "Fecha 2 es mayor"
        else:
            mayor= "Las fechas son iguales"
if mes_1 == mes_2 and año_1 == año_2:
    mismo_año_mes = "Estan en el mismo año y mes"
else:
    mismo_año_mes= "Estan en años o meses distintos"