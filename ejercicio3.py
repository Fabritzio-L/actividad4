usuarios = ["usuario1","usuario2","usuario3"]
contraseñas = ["123","abc","123abc"]
intentos = 0
acceso = False
while intentos < 3:
    usuario =input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    usuario_correcto= False
    for i in range(len(usuarios)):
        if usuarios[i] == usuario:
            usuario_correcto = True
            if contraseñas[i] == contraseña:
                print("Acceso concedido")
                acceso = True
            else:
                intentos += 1
                print(f"Contraseña incorrecta, le quedan {intentos} intentos.")
            break
