# Inicializamos el contador
contador_productos = 0

# Solicitamos el primer nombre de producto
nombre_producto = input("Ingresá el nombre del producto (o 'salir' para finalizar): ").lower()

# Mientras el nombre del producto no sea 'salir', seguimos pidiendo productos
while nombre_producto != "salir":
    # Solicitamos la cantidad en stock del producto
    cantidad_stock = int(input(f"Ingresá la cantidad en stock de {nombre_producto}: "))
    
    # Aumentamos el contador de productos
    contador_productos += 1

    # Volvemos a solicitar el nombre del siguiente producto
    nombre_producto = input("Ingresá el nombre del producto (o 'salir' para finalizar): ").lower()

# Mostramos el total de productos ingresados
print(f"Se ingresaron {contador_productos} productos en total.")
