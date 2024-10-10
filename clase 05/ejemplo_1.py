montototalcompra = float(input("ingrese el monto total de la compra:"))
cantidad_articulos = int(input("ingrese la cantidad de artículos que está comprando: "))
monto_final = montototalcompra
descuento = 0

if  montototalcompra > 0 and cantidad_articulos > 0:
    if cantidad_articulos < 3:
        print(f"No se aplica descuento. Monto total: ${montototalcompra:.2f}")
    else:
        if cantidad_articulos >= 3 and cantidad_articulos < 5:
            descuento = montototalcompra * 0.10
            monto_total_con_descuento = montototalcompra - descuento
            print(f"Se aplica descuento del 10%. Monto total después del descuento: ${monto_total_con_descuento:.2f}")
        else:
            #mayor a 5
            if montototalcompra > 10000 :
                descuento = montototalcompra * 0.15
                monto_total_con_descuento = montototalcompra - descuento
                print(f"Se aplica un descuento del 15%. Monto total después del descuento: ${monto_total_con_descuento:.2f}")
            else:
                print(f"No se aplica descuento. Monto total: ${montototalcompra:.2f}") 

    print()    
    print(f"Gracias por su compra de {montototalcompra}, Descuento: {descuento}")   
    print(f"Detalle: {monto_final} - Cantidad: {cantidad_articulos}")
    print("vuelva pronto")

else:
    print("Datos erroneos!")

