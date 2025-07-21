ingreso_anual = int(input("Ingrese su ingreso anual: "))
dependientes = int(input("Ingrese el numero de dependientes: "))
if ingreso_anual < 40000 and dependientes >2:
    print("No paga impuestos.")
else:
    if  0>= ingreso_anual <=30000:
        impuestos= ingreso_anual * 0.05
    elif ingreso_anual <= 60000:
        impuestos = ingreso_anual * 0.1
    elif ingreso_anual <= 100000:
        impuestos= ingreso_anual * 0.15
    elif impuestos > 100000:
        impuestos = ingreso_anual * 0.2
    else:
        print("Dato no valido")