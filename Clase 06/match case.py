option = int(input("ingrese una opción: "))

match option:
    case 1:
        print("Alta")
    case 2:
        print("Baja")
    case 3:
        print("Modificar")
    case _:
        print("Opción no válida") 