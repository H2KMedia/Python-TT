#motos2.py
#eliminar
motos = ['fencor', 'zanella', 'scooter', 'motomel', 'honda']
print(motos)

#del
del motos[0]
print(motos)

del motos[1]
print(motos)

#pop()
motos = ['scooter', 'ducati', 'motomel', 'honda']
moto_eliminada = motos.pop()
print(motos)
print(moto_eliminada)

primer_moto = motos.pop(0)
print(motos)

#remove 
motos.remove('motomel')
print(motos)

muy_cara = 'ducati'
motos.remove(muy_cara)
print(motos)