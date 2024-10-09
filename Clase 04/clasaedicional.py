import os
# link de clase  https://docs.python.org/3/tutorial/inputoutput.html
# link de clase https://www.w3schools.com/python/ref_string_format.asp
# link de clase https://www.onlinegdb.com/vO9ev7cfQ7

'''
Ticket de compra
1- Escribir un programa que solicite el nombre, la cantidad y el valor unitario
de tres productos

2- debe calcular el importe de IVA (21%) de cada producto

3- por ultimo debe mostrar en la terminal el ticket de la operación
con todos los datos de la compra
'''
#ddatos del ticket

supermercado = "las marias"
direccion = "Av. Patagonia 123"
telefono = "0800-333-1111"
fecha = "3/10/2024   19:15"


#productos
producto1 = "Leche"
cantidad1 = int(1)
precio_unitario1 = "1550"

producto2 = "arroz"
cantidad2 = int(2)
precio_unitario2 = "2290"

producto3 = "huevos"
cantidad3 = int(1)
precio_unitario3 = "1600"

#proceso
IVA = 1.21

iva_prod1 = precio_unitario1 * IVA
iva_prod2 = precio_unitario2 * IVA
iva_prod3 = precio_unitario3 * IVA

precio_final_prod1 = precio_unitario1 + iva_prod1
precio_final_prod2 = precio_unitario2 + iva_prod2
precio_final_prod3 = precio_unitario3 + iva_prod3

subtotal1 = precio_final_prod1 * cantidad1
subtotal2 = precio_final_prod2 * cantidad2
subtotal3 = precio_final_prod3 * cantidad3

total_compra = (subtotal1 + subtotal2 + subtotal3)


#salida

print("~"*30)
print(f"{supermercado.upper():^30}")
print("~"*30)
#print(supermercado.upper().center(30,'-'))
print()
print(f"Dirección: {direccion:^20}")
print(f"Tel.: {telefono:^30}")
print(f"Fecha: {fecha:^30}")
print("_"*30)
print()
print(f"{'producto':<15} {'cant':<5} {'P.U.':<10} {'IVA':<10}")
print()
print("_"*30)

'''
os.system('')
os.system('cls')
'''
