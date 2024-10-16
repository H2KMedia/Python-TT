import os
os.system('cls')
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

def mostrar_submenu_registrar():
    print("=== Submenú: Registrar Libro ===")
    print("Ingrese los detalles del libro:")

def obtener_id_libro():
    """Obtiene el próximo ID secuencial desde el archivo."""
    if os.path.exists("base_de_datos.txt"):
        with open("base_de_datos.txt", "r") as file:
            lineas = file.readlines()
            return len(lineas) + 1  # ID secuencial
    return 1

def guardar_libro(libro):
    """Guarda el libro en el archivo base_de_datos.txt."""
    with open("base_de_datos.txt", "a") as file:
        file.write(f"{libro['id']},{libro['titulo']},{libro['autor']},{libro['anio']},{libro['editorial']},{libro['isbn']}\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            while True:
                mostrar_submenu_registrar()
                titulo = input("Título del libro: ")
                autor = input("Autor: ")
                anio = input("Año de edición: ")
                editorial = input("Editorial: ")
                isbn = input("Número de ISBN: ")
                
                id_libro = obtener_id_libro()
                print(f"Número de registro: {id_libro}")

                confirmar = input("¿Confirma el registro del libro? (s/n): ")
                if confirmar.lower() == 's':
                    libro = {
                        "id": id_libro,
                        "titulo": titulo,
                        "autor": autor,
                        "anio": anio,
                        "editorial": editorial,
                        "isbn": isbn
                    }
                    guardar_libro(libro)
                    print("Libro registrado exitosamente.")
                else:
                    print("Registro cancelado.")

                otro = input("¿Desea registrar otro libro? (s/n): ")
                if otro.lower() != 's':
                    break
        elif opcion == '2':
            print("Actualizar Libro seleccionado.")
            # Lógica para actualizar un libro.
        elif opcion == '3':
            print("Eliminar Libro seleccionado.")
            # Lógica para eliminar un libro.
        elif opcion == '4':
            print("Buscar Libro seleccionado.")
            # Lógica para buscar un libro.
        elif opcion == '5':
            print("Listar Libros seleccionado.")
            # Lógica para listar libros.
        elif opcion == '6':
            print("Reportes de Libros seleccionado.")
            # Lógica para reportes de libros.
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Presione cualquier tecla para continuar...")
            input()

if __name__ == "__main__":
    main()
