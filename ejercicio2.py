ingreso_anual = int(input("Ingrese su ingreso anual: "))
dependientes = int(input("Ingrese el numero de dependientes: "))
if ingreso_anual <0 or dependientes <0:
    print("El valor no puede ser negativo")
elif ingreso_anual < 40000 and dependientes >2:
    print("No paga impuestos.")
else:
    if  ingreso_anual <=30000:
        impuestos= ingreso_anual * 0.05
    elif ingreso_anual <= 60000:
        impuestos = ingreso_anual * 0.1
    elif ingreso_anual <= 100000:
        impuestos= ingreso_anual * 0.15
    else:
        impuestos = ingreso_anual * 0.2
    deducccion = dependientes * 1000
    impuesto_final = impuestos - deducccion
    if impuesto_final <0:
        impuesto_final=0
    print(f"Su impuesto inicial era de: Q{impuestos}")
    print(f"Su deducción por dependientes es de: Q{deducccion}")
    print(f"Su iimpuesto final a pagar es de : Q{impuesto_final}")