productos = {"pizza": 55.00, "hamburguesa":35.99, "pastel":17.50}
carrito =[]
for i in productos:
    print(f"-{i}")
while True:
    solicitar_producto = input("\nIngrese el nombre del producto para consultar precio (o 'fin' para terminar): ").strip().lower()
    if solicitar_producto in productos:
        precio = productos[solicitar_producto]
        print(f"El precio de {solicitar_producto} es: Q{precio}")
        agregar_producto = input("¿Desea agregar el producto al carrito? (si o no)").lower()
        if agregar_producto in ("si","sí"):
            carrito.append(precio)
            print(f"{agregar_producto} agregado al carrito")
        elif agregar_producto in ("no"):
            print("Producto no agregado")
        else:
            print("Ingrese una respuesta valida")
    else:
        print("Producto no encontrado.")