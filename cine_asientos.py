def pedir_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Ingresa un número mayor que cero.")
        except ValueError:
            print("Entrada no válida. Escribe un número entero.")


def mostrar_sala(asientos):
    print("\n       " + "  ".join(str(c + 1) for c in range(len(asientos[0]))))
    for i, fila in enumerate(asientos):
        print(f"Fila {i + 1:>2}: " + "  ".join(fila))
    print()


def pedir_posicion(asientos):
    filas = len(asientos)
    columnas = len(asientos[0])

    fila = pedir_entero_positivo(f"Ingresa la fila (1-{filas}): ")
    columna = pedir_entero_positivo(f"Ingresa la columna (1-{columnas}): ")

    if fila > filas or columna > columnas:
        print("Error: ese asiento no existe. Verifica la fila y la columna.")
        return None

    return fila - 1, columna - 1


def reservar_asiento(asientos):
    posicion = pedir_posicion(asientos)
    if posicion is None:
        return

    fila, columna = posicion
    if asientos[fila][columna] == "L":
        asientos[fila][columna] = "X"
        print("¡Reserva realizada! El asiento ahora está ocupado.")
    else:
        print("Ese asiento ya está ocupado. Elige otro.")


def liberar_asiento(asientos):
    posicion = pedir_posicion(asientos)
    if posicion is None:
        return

    fila, columna = posicion
    if asientos[fila][columna] == "X":
        asientos[fila][columna] = "L"
        print("El asiento se liberó correctamente.")
    else:
        print("Ese asiento ya está libre.")


def mostrar_estadisticas(asientos):
    ocupados = sum(fila.count("X") for fila in asientos)
    libres = sum(fila.count("L") for fila in asientos)

    print("\n--- Estadísticas de la sala ---")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")
    print(f"Total de asientos: {libres + ocupados}")


def main():
    print("=== SISTEMA DE RESERVACIÓN DEL CINE ===")
    filas = pedir_entero_positivo("Número de filas del cine: ")
    columnas = pedir_entero_positivo("Número de columnas (asientos por fila): ")

    asientos = [["L" for _ in range(columnas)] for _ in range(filas)]

    while True:
        print("\n========== MENÚ ==========")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_sala(asientos)
        elif opcion == "2":
            reservar_asiento(asientos)
        elif opcion == "3":
            liberar_asiento(asientos)
        elif opcion == "4":
            mostrar_estadisticas(asientos)
        elif opcion == "5":
            print("Gracias por usar el sistema del cine. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Selecciona un número del 1 al 5.")


if __name__ == "__main__":
    main()
