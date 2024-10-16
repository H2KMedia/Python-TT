def mostrar_menu():
    print("=== Menú de Libros ===")
    print("1 - Registrar Libro")
    print("2 - Actualizar Libro")
    print("3 - Eliminar Libro")
    print("4 - Buscar Libro")
    print("5 - Listar Libros")
    print("6 - Reportes de Libros")
    print("0 - Salir")
    print("=======================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Registrar Libro seleccionado.")
            # Aquí puedes agregar la lógica para registrar un libro.
        elif opcion == '2':
            print("Actualizar Libro seleccionado.")
            # Aquí puedes agregar la lógica para actualizar un libro.
        elif opcion == '3':
            print("Eliminar Libro seleccionado.")
            # Aquí puedes agregar la lógica para eliminar un libro.
        elif opcion == '4':
            print("Buscar Libro seleccionado.")
            # Aquí puedes agregar la lógica para buscar un libro.
        elif opcion == '5':
            print("Listar Libros seleccionado.")
            # Aquí puedes agregar la lógica para listar libros.
        elif opcion == '6':
            print("Reportes de Libros seleccionado.")
            # Aquí puedes agregar la lógica para reportes de libros.
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Presione cualquier tecla para continuar...")
            input()

if __name__ == "__main__":
    main()
