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
elif origen == "este":
    if destino == "norte":
        print("Dirijase al noreste")
    elif destino == "sur":
        print("Dirijase al sureste")
elif origen == "oeste":
    if destino == "norte":
        print("Dirijase al noroeste")
    elif destino == "sur":
        print("Dirijase al suroeste")
else:
    print("Error, solo se permite norte,sur,este u oeste.")