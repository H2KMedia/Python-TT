import os

# Ciclo principal del menú
ultimo_artista = None

while True:
    print("\n---- Menú de Gestión de Artistas ----")
    print("1. Crear nuevo artista")
    print("2. Buscar artista")
    print("3. Mostrar último artista registrado")
    print("4. Borrar pantalla")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    
    #if elif de las ociones
    # si opcion es 5 - break
    # crear las funcionalidades
    # no esta dentro del 1 a 5 indicar error
    if opcion == "1":
        # Crear nuevo artista
        nuevo_artista = input("Ingrese el nombre del nuevo artista: ").strip()
        
        if len(nuevo_artista) == 0:
            print("Error: El nombre del artista no puede estar vacío.")
        else:
            ultimo_artista = nuevo_artista
            print(f"Artista '{nuevo_artista}' registrado exitosamente.")

    elif opcion == "2":
        # Buscar artista
        if ultimo_artista is None:
            print("No hay ningún artista registrado aun.")
        else:
            nombre = input("Ingrese el nombre del artista a buscar")
            if nombre.lower() == ultimo_artista.lower():
                    print(f"Artista '{nombre}' encontrado.")
            else:
                print(f"El artista '{nombre}' no coincide con el registrado ('{ultimo_artista}').")
    
    elif opcion == "3":
        # Mostrar el último artista registrado
        if ultimo_artista is None:
            print("No hay ningún artista registrado aún.")
        else:
            print(f"Último artista registrado: {ultimo_artista}")
    
    elif opcion == "4":
    # Borrar la pantalla
        if os.name == 'nt':  # Si estamos en Windows
            os.system('cls')
        else:  # Si estamos en Linux o macOS
            os.system('clear')
    
    elif opcion == "5":
        # Salir del programa
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")