nombre = input("Ingrese su nombre completo: ")
dpi = input("Ingrese su numero de DPI: ")
departamento = input("Ingrese su departamento: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad= 2025 - año_nacimiento
if len(nombre) <5:
    print("Su nombre debe tener minimo 5 letras.")
elif len(dpi) != 13:
    print("Numero de DPI incorrecto.")
else:
    departamento = departamento.lower()
    if edad >= 18 or (departamento in ["peten","petén", "alta verapaz"] >= 17):
        print(f"Bienvenido {nombre}, su centro de votación es {departamento}.")