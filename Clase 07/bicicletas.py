#listas
bicicletas = ['mountain', 'ruta', 'playera', 'bmx', 10]

print(type(bicicletas))
print(bicicletas) #imprime tal cual definida

#acceder a un elemento de la lista
print(bicicletas[0]) #primer elemento

primer = bicicletas[0]
print(primer.title()) #aplicar formato al string
print(f"Mi primer bicicleta fué {bicicletas[0]}")

ultimo = bicicletas[4] #10
print(ultimo)
print(bicicletas[-1]) #accede al ultimo elemento

#longitud
print(len(bicicletas)) #verificar el elemento a acceder

#no está la posición
print(bicicletas[8]) #rompe el código

