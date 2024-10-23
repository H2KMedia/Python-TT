# Solicitar el precio al usuario
precio = float(input("Ingresá el precio del producto: "))

# Validar que el precio sea mayor a 0
while precio <= 0:
    print("Error: el precio debe ser un valor mayor a 0.")
    precio = float(input("Ingresá el precio del producto nuevamente: "))

# Mostrar el precio válido
print(f"El precio aceptado es: ${precio:.2f}")