# conocemos de antemano la cantidad de iteraciones
# con la funcion range creamos dentro de un intervalo

# for indice in range(1,11): #parametros: inicio, final, paso - extremo no incluye
#     print(indice)
    
# for i in range(21):
#     print(i)
    
    
#cadena de caracteres es un elemento iterable
lenguaje = 'Python'

#recorriendo por valor
# for letra in lenguaje:
#     print(letra)
    
print(len(lenguaje))

#acceder por indice
print(lenguaje[2])
print(lenguaje[0:2])
print(lenguaje[3:])
print(lenguaje[-1])
#print(lenguaje[7])#Index Error

for i in range(len(lenguaje)):
    print(i,end="-")
    print(lenguaje[i])

#lista de numeros    
numeros = [2,5,8,10] #elemento iterable
for numero in numeros:
    print(numero)
