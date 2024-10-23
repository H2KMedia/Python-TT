#ordena permanentemente (sort)
autos = ['ford', 'renault', 'chevrolet', 'peugeot', 'fiat']
print("base")
print(autos)
print("lista con sort")
autos.sort()
print(autos)

#invierte el orden
print("lista con sort/reverse/true")
autos.sort(reverse = True)
print(autos)

print("lista con .reverse")
autos.reverse()
print(autos)

#ordena temporalmente
autos = ['koeninsegg', 'lamborghini','audi', 'ferrari', 'mercedes', 'porsche']
print("lista con sorted")
print(sorted(autos))
print(autos)


#crear una copia
autos =  ['audi', 'mercedez','bmw']
nuevos_autos = autos[:] #creo copia
print(nuevos_autos)
