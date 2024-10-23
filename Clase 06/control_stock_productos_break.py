# Inicializamos el contador
contador_productos = 0

# Iniciamos el ciclo para ingresar productos
while True:
    # Solicitamos el nombre del producto
    nombre_producto = input("Ingresá el nombre del producto (o 'salir' para finalizar): ").lower()

    # Condición para terminar el ciclo
    if nombre_producto == "salir":
        break

    # Solicitamos la cantidad en stock
    cantidad_stock = int(input(f"Ingresá la cantidad en stock de {nombre_producto}: "))

    # Aumentamos el contador de productos
    contador_productos += 1

# Mostramos el total de productos ingresados
print(f"Se ingresaron {contador_productos} productos en total.")
