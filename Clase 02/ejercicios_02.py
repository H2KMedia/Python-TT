'''
EJERCICIO 1 - LISTA DE COMPRAS
Usando la instrucción print() y lo visto en la clase,
escribir un programa que muestre en la terminal la
lista de productos que necesitamos comprar en el
supermercado.
'''
titulo = "listado de productos a comprar en el super"
print()
print(titulo)
print()
print(46*"-")
print("| Producto \t | Cantidad \t | Precio    | \t")
print(46*"-")
print("| Manteca \t |    1    \t | $1.490,00 | \t")
print("| Aceite \t |    1    \t | $1.890,00 | \t")
print("| Harina \t |    1    \t | $1.050,00 | \t")
print("| Azúcar \t |    1    \t | $  980,00 | \t")
print(46*"-")
print("| Total calculado de compra  \t | $5.410,00 |")
print(46*"-")
print()
print()
print(60*"*")
print()
'''
EJERCICIO 2 - INGRESO PROMEDIO
Escribir un programa que guarde en variables el
monto del ingreso de cada uno de los primeros 6
meses del año.

Luego, calcular y guardar en otra variable el
promedio de esos valores.

Por último, mostrar una leyenda que diga “El
ingreso promedio en el semestre es de xxxxx”
donde “xxxxx” es el valor calculado.
'''
ene24, feb24, mar24, abr24, may24, jun24 = 259000, 198500, 277300, 325300, 389400, 410150
tk01, tk02, tk03, tk04, tk05, tk06 = 12, 9, 14, 18, 21, 24
ingreso_gross = ene24 + feb24 + mar24 + abr24 + may24 + jun24
ingreso_prom = ingreso_gross /6
ingreso_prom = f"{ingreso_prom:.2f}"
ingreso_prom_tx = "|   INGRESO PROMEDIO DEL SEMESTRE    $ " + str(ingreso_prom) + " |"
tk_total = tk01 + tk02 + tk03 + tk04 + tk05 + tk06
tk_prom = tk_total /6
tk_prom = f"{tk_prom:.2f}"
tk_prom_tx = "|   TICKETS PROMEDIO MENSUALES          " + str(tk_prom) + "    |"
vta_prom = ingreso_gross / tk_total
vta_prom = f"{vta_prom:.2f}"
vta_prom_tx = "|   VALOR PROMEDIO DE ARTÍCULO       $ " + str(vta_prom) + "  |"
print(50*"=")
print("|        ESTADÍSTICAS DE VENTA SEMESTRALES       |")
print(50*"=")
print("|   MES \t| VENTAS \t |     MONTO     |")
print(50*"-")
print("| ENERO \t|     12    \t |  $   259.000  |")  
print("| FEBRERO \t|      9    \t |  $   198.500  |")  
print("| MARZO \t|     14    \t |  $   277.300  |")  
print("| ABRIL \t|     18    \t |  $   325.300  |")  
print("| MAYO      \t|     21    \t |  $   389.400  |")  
print("| JUNIO \t|     24    \t |  $   410.150  |")  
print(50*"-")
print("| SEMESTRE \t|     98   \t |  $ 1.859.650  |")
print(50*"-")
print(ingreso_prom_tx)
print(tk_prom_tx)
print(vta_prom_tx)
print(50*"=")
print()