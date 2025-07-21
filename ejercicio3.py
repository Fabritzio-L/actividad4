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
                print(f"Contraseña incorrecta, le quedan {3- intentos} intentos.")
            break
    if not usuario_correcto:
        intentos +=1
        print(f"Usuario incorrecto, le quedan {3- intentos} intentos.")
    if acceso:
        break
if not acceso:
    print("Se quedo sin intentos, acceso denegado.")
else:
    print("-----Menu-----")
    print("1. Ver perfil.")
    print("2. Cambiar contraseña.")
    print("3. Cerrar sesion.")