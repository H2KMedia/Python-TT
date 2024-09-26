# Se desea calcular la distancia recorrida (m) por un móvil que
# tiene velocidad constante (m/s) durante un tiempo t (s),
# considerar que es un MRU (Movimiento Rectilíneo
# Uniforme).

# entrada : velocidad, tiempo
# proceso: (MRU) v = d/t => d = v*t
# salida: distancia
# entrada
print("Ingrese la velocidad y el tiempo y se informa la distancia recorrida")
# convertir entrada a el tipo de datos adecuado
velocidad = float(input("Ingrese velocidad (m/s): "))
tiempo = int(input("Ingrese el tiempo (s): "))
#proceso
distancia = velocidad * tiempo
#salida
print("La distancia recorrida es "+str(distancia)+" m.")
print(f"La distancia recorrida es {distancia:.2f} m.")

#------------------------------------------------------------

print("ingrese su fecha de nacimiento:")
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))
print(dia, mes, año)
#format
print(f"usted nació el {dia} del mes {mes} en el año {año}")
print("usted nació el {} del mes {} en el año {}.".format(dia, mes, año)) #código de versiones anteriores de python

print("\"cuanto más conozco a la gente más quiero a mi perro\"")

