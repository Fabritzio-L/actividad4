origen = input("¿Desde donde se encuentra?:").lower()
destino = input("¿A donde se dirige?: ").lower()
if origen == "norte":
    if destino == "este":
        print("Dirijase al noreste")
    elif destino == "oeste":
        print("Dirijase al noroeste")
elif origen == "sur":
    if destino == "este":
        print("Dirijase al sureste")
    elif destino == "oeste":
        print("Dirijase al suroeste")