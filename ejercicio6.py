peso_paquete= float(input("Ingrese el peso del paquete: "))
distancia = float(input("Ingrese la distancia en km del envio: "))
urgencia = input("¿El envio es de urgencia (si/no)?: ").lower()
tamaño = input("Ingrese el tamaño del paquete pequeño/mediano/grande: ").lower()
costo_base = peso_paquete * 2.5 + distancia * 1.5
recargo_urgencia=0
recargo_tamaño=0
descuento=0
if urgencia == "si" or urgencia =="sí":
    recargo_urgencia= 50
if tamaño == "grande":
    recargo_tamaño=30
if urgencia == "no" and peso_paquete <5:
    descuento=20
