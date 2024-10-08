import os

'''Entrada'''

#Datos del ticket
supermercado = "Las Marías"
direccion = "Av. Patagonia 123"
telefono = "0800-333-1111"
fecha = "3-10-2024 19:15"

#productos
producto1 = "Leche"
cantidad1 = 1
precio_unitario1 = 1550.50

producto2 = "Arroz"
cantidad2 = 2
precio_unitario2 = 2200.00

producto3 = "Huevos"
cantidad3 = 1
precio_unitario3 = 1600.00

'''Proceso'''
subtotal1 = precio_unitario1*cantidad1
subtotal2 = precio_unitario2*cantidad2
subtotal3 = precio_unitario3*cantidad3
total = subtotal1+subtotal2+subtotal3

#total = (precio_unitario1*cantidad1)+(precio_unitario2*cantidad2)+(precio_unitario3*cantidad3)

'''Salida'''
print("="*30) #imprima una linea punteada por un espacio de 30 caracteres
#print("Supermercado : "+supermercado.upper())
print(f"{supermercado.upper():^30}") #imprima la variable supermercado centrado en un espacio de 30 caracteres
#cadena.center(ancho, relleno_opcional)
#print(supermercado.center(30, '-').upper())#imprima la variable supermercado centrado en un espacio de 30 caracteres, agrego relleno relleno_opcional
print(f"Dirección: {direccion:^20}")
print(f"Tel: {telefono:^30}")
print(f"Fecha: {fecha:^30}")
print("="*30)
print(f"{'Producto':<15} {'Cant':<5} {'Precio':>8}")
print("-"*30)
print(f"{producto1:<15} {cantidad1:<5} {precio_unitario1:>8}")
print(f"{producto2:<15} {cantidad2:<5} {precio_unitario2:>8}")
print(f"{producto3:<15} {cantidad3:<5} {precio_unitario3:>8}")
print("-"*30)
print(f"{'Total:':<20}{total:>10.2f}")
print("="*30)

#para limpiar pantalla....ampliaremos
os.system('cls')
print('Limpió la pantalla')