productos = {"pizza": 55.00, "hamburguesa":35.99, "pastel":17.50}
carrito =[]
for i in productos:
    print("Productos disponibles")
    print(f"-{i}")
while True:
    solicitar_producto = input("Ingrese el nombre del producto para consultar precio (o 'fin' para terminar): ").lower()
    if solicitar_producto == "fin":
        break
    if solicitar_producto in productos:
        precio = productos[solicitar_producto]
        print(f"El precio de {solicitar_producto} es: Q{precio}")
        agregar_producto = input("¿Desea agregar el producto al carrito? (si o no)").lower()
        if agregar_producto in ("si","sí"):
            carrito.append(precio)
            print(f"{solicitar_producto} agregado al carrito")
        else:
            print("Producto no agregado")
    else:
        print("Producto no encontrado.")
if not carrito:
    print("\nNo hay productos en el carrito")
else:
    subtotal = sum(carrito)
    propina = input("¿Desea dejar propina?: ")
    if propina in ("si","sí"):
        porcentaje_propina= int(input("Ingrese en porcentaje la propina que quiera dejar: "))
        prop = subtotal * (porcentaje_propina/100)
    else:
        prop = 0
    tarjeta_cliente_frecuente = input("¿Cuenta con tarjeta de cliente frecuente si/no?: ")
    if tarjeta_cliente_frecuente in ("si","sí"):
        descuento = subtotal * 0.1
    else:
        descuento= 0
    iva= subtotal * 0.12
    total_compra= subtotal + iva + prop - descuento
    print("----FACTURA----")
    print(f"Subtotal: Q{subtotal:.2f}")
    print(f"Propina {porcentaje_propina}%: Q{prop:.2f}")
    print(f"IVA: Q{iva}")
    print(f"Descuento: Q{descuento:.2f}")
    print(f"Total: Q{total_compra:.2f}")