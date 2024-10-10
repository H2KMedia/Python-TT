#ejemplo3.py

print("1. Alta")
print("2. Modificar")
print("3. Baja")
print("4. Salir")

opcion = int(input("ingrese opción: "))

if opcion ==1:
    print("Funcionalidad en construcción 1")
else:
    if opcion ==2:
        pass #sentencia pasar por alto el código sin error
        print("Funcionalidad en construcción 2")
    else:
        if opcion ==3:
            print("Funcionalidad en construcción 3")
        else:
            if opcion == 4:
                print("Funcionalidad en construcción 4")
            else:
                print("opción erronea")
                
print("programa continua")