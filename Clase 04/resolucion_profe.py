'''Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.
Luego, debe calcular el importe de IVA (21%) de cada producto.
Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la compra. '''
nombre_producto1 = input("Ingrese el nombre del producto 1: ")
cantidad_producto1 = int(input("Ingrese la cantidad del producto 1: "))
valor_unitario_producto1 = float(input("Ingrese el valor unitario del producto 1:"))

nombre_producto2 = input("Ingrese el nombre del producto 2: ") 
cantidad_producto2 = int(input("Ingrese la cantidad del producto 2: "))
valor_unitario_producto2 = float(input("Ingrese el valor unitario del producto 2:"))

nombre_producto3 = input("Ingrese el nombre del producto 3: ") 
cantidad_producto3 = int(input("Ingrese la cantidad del producto 3: "))
valor_unitario_producto3 = float(input("Ingrese el valor unitario del producto 3:"))

IVA = 0.21

importe_producto1 = cantidad_producto1 * valor_unitario_producto1
importe_producto2 = cantidad_producto2 * valor_unitario_producto2
importe_producto3 = cantidad_producto3 * valor_unitario_producto3

iva_producto1 = importe_producto1 * IVA
iva_producto2 = importe_producto2 * IVA
iva_producto3 = importe_producto3 * IVA

total_compra_producto1 = importe_producto1 + iva_producto1
total_compra_producto2 = importe_producto2 + iva_producto2
total_compra_producto3 = importe_producto3 + iva_producto3

total_iva = iva_producto1 + iva_producto2 + iva_producto3
total_compra = total_compra_producto1+total_compra_producto2+total_compra_producto3


# Mostrar el ticket en un formato mejorado
print("-"*50)
print("Ticket de la compra".center(50))
print("-"*50)
print(f"{'Producto':<15} {'Cant.':<5} {'P.U.($)':<10} {'Total($)':<10} {'IVA($)':<10}")
print("-"*50)
print(f"{nombre_producto1:<15} {cantidad_producto1:<5} {valor_unitario_producto1:<10.2f} {total_compra_producto1:<10.2f} {iva_producto1:<10.2f}")
print(f"{nombre_producto2:<15} {cantidad_producto2:<5} {valor_unitario_producto2:<10.2f} {total_compra_producto2:<10.2f} {iva_producto2:<10.2f}")
print(f"{nombre_producto3:<15} {cantidad_producto3:<5} {valor_unitario_producto3:<10.2f} {total_compra_producto3:<10.2f} {iva_producto3:<10.2f}")
print("-"*50)
print(f"{'Total Compra:':<30} ${total_compra:<10.2f}")
print(f"{'Total IVA:':<30} ${total_iva:<10.2f}")
print("-"*50)
print("Gracias por su compra. ¡Vuelva pronto!")
print("-"*50)