import os

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
        file.write(f"{libro['id']},{libro['titulo']},{libro['autor']},{libro['anio']},{libro['editorial']},{libro['isbn']},{libro['unidades']}\n")

def listar_libros():
    """Lista todos los libros almacenados en base_de_datos.txt."""
    if os.path.exists("base_de_datos.txt"):
        with open("base_de_datos.txt", "r") as file:
            lineas = file.readlines()
        
        print("\n=== Lista de Libros ===")
        print("+----+--------------------+--------------------+------+--------------------+------------+----------+")
        print("| ID | Título             | Autor              | Año  | Editorial          | ISBN       | Unidades |")
        print("+----+--------------------+--------------------+------+--------------------+------------+----------+")
        
        for linea in lineas:
            datos = linea.strip().split(",")
            print(f"| {datos[0]:<2} | {datos[1]:<18} | {datos[2]:<18} | {datos[3]:<4} | {datos[4]:<18} | {datos[5]:<10} | {datos[6]:<8} |")
        
        print("+----+--------------------+--------------------+------+--------------------+------------+----------+")
    else:
        print("No hay libros registrados.")

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
                unidades = input("Cantidad de unidades: ")

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
                        "isbn": isbn,
                        "unidades": unidades
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
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
            listar_libros()
            input("Presione cualquier tecla para continuar...")
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
