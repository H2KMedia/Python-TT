import os
'''
TIF
    registrar, actualizar, eliminar y mostrar productos
    CRUD (Create, Read, Uptade, Delete)
    funciones de búsqueda, gestionar el stock mínimo(reportes)
'''
#Inventario de libros

#Menú de opciones:
print(100*"-")
print("|                              MENÚ DE OPCIONES DISTRIBUIDORA LIBROS                               |")
print(100*"-")
print("|                                                                                                  |")
print("|                                    1 - REGISTRAR LIBRO                                           |")
print("|                                    2 - ACTUALIZAR LIBRO                                          |")
print("|                                    3 - ELIMINAR LIBRO                                            |")
print("|                                    4 - BUSCAR LIBRO                                              |")
print("|                                    5 - LISTAR LIBROS                                             |")
print("|                                    6 - REPORTE DE LIBROS CON BAJO STOCK                          |")
print("|                                    0 - SALIR DE SISTEMA                                          |")
print("|                                                                                                  |")
print(100*"-")

opcion = int(input("Ingrese opción seleccionada (1 - 7)"))
if opcion > 7 : 
    os.system('cls')
    print("ingreso inválido,\n intente nuevamente")
else: 
    print(f"Ud. seleccionó {opcion}")

'''
#Registrar libros
titulo = input("Título: ") #alicia en El país de las Maravillas
print(titulo)
titulo = titulo.title()#Alicia En El País De Las Maravillas
print(titulo)
titulo = titulo.upper()#todo en mayusculas
print(titulo)
titulo = titulo.lower()#todo en minusculas
print(titulo)
print(titulo[0]) #A
print(titulo[0:5]) #subcadena

isbn = input("ISBN: ")
es_numero = isbn.isnumeric() #booleana
print(es_numero)
print(len(str(isbn))) #longitud del string
autor = input("Autor: ")
genero = input("Género: ")

#actualizar libros
#isbn - stock
#Eliminar
#isbn - borra registro
#Buscar
#criterios (filtros) de busqueda: isbn - titulo

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))

print("Ud. ingresó: \t Nombre: ", nombre, "\t Apellido: ", apellido,"\t Edad: ", edad)

print("Datos ingresados: "+nombre+" "+apellido+" "+str(edad))

#format-strings docu: https://www.w3schools.com/python/ref_string_format.asp
print(f"Datos ingresados: {nombre} {apellido} {edad}. ")


#reportes
print("\t Nombre: \t Apellido: \t Edad: ")
print("\t ",nombre," \t ",apellido," \t ",edad)
'''