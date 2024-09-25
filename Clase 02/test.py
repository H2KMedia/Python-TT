compras_mensuales = (150, 200, 180, 220, 210, 190)
promedio = sum(compras_mensuales) / len(compras_mensuales)
print("\tLista de compras mensuales (primeros 6 meses): ")
for i, compra in
enumerate(compras_mensuales, 1):
print(f"\t-Mes {i}: {compra}
unidades")

print(f"\n\tPromedio de compras:
{promedio:.2f} unidades")        