#listas
motos = ['fencor', 'zanella', 'honda', 'motomel', 'ktm', 'kawasaki']
print(motos)

#modificar
print(motos[0])
motos[0] = 'harley'
print(motos)

#agregar
motos.append('bmw') #por valor
print(motos)

nueva_moto = input("ingrese nuevo modelo: ") #proceder a validar
motos.append(nueva_moto)
print(motos)

print('motos2')
motos2 = []
motos2.append('ducati')
motos2.append('suzuki')
motos2.append('jawa')
motos2.append('kapnamu')
print(motos2)

#insertar dentro de la lista
motos2.insert(0,'honda')
print(motos2)

#eliminar
