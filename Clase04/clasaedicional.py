import os
#ddatos del ticket

supermercado = "las marias"
direccion = "Av. Patagonia 123"
telefono = "0800-333-1111"
fecha = "3/10/2024   19:15"
'''

#productos
producto1 = "Leche"
cantidad1 = "1"
precio_unitario1 = "1550"

producto2 = "arroz"
cantidad2 = "2"
precio_unitario2 = "2290"

producto3 = "huevos"
cantidad3 = "1"
precio_unitario3 = "1600"

#proceso

subtotal1 = precio_unitario1 * cantidad1
subtotal2 = precio_unitario2 * cantidad2
subtotal3 = precio_unitario3 * cantidad3

total = subtotal1 + subtotal2 + subtotal3


#salida
'''
print("~"*30)
print(f"{supermercado.upper():^30}")
print("~"*30)
print(supermercado.upper().center(30,'-'))
print()
print(f"Dirección: {direccion:^20}")
print(f"Tel.: {telefono:^30}")
print(f"Fecha: {fecha:^30}")
print("_"*30)
print(f"('producto':<15) ")


os.system('')
os.system('cls')

