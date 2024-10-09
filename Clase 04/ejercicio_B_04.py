litros_consumidos = (litros_por_100km * longitud_viaje) / 100
dinero_gastado = litros_consumidos * costo_por_litro
print(f"\n---DETALLE DEL VIAJE---")
print(f"LITROS CONSUMIDOS : {litros_consumidos:2f} LITROS")
print(f"DINERO GASTADO: $ {dinero_gastado:2f}")