origen = input("¿Desde donde se encuentra?:").lower()
destino = input("¿A donde se dirige?: ").lower()
if (origen == "norte" and destino == "sur") or (origen == "sur" and destino == "norte"):
    print("Dirijase recto al norte" if destino == "norte" else "Dirijase recto al sur")
elif (origen == "este" and destino == "oeste") or (origen == "oeste" and destino == "este"):
    print("Dirijase recto al este" if destino == "este" else "Dirijase recto al oeste")
elif origen == destino:
    print("Ya se encuentra en su destino")
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