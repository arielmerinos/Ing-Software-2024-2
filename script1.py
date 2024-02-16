
def imprimir_ascii_cancha(cambio_cancha):
    """Imprime una representación bonita en ASCII de la cancha, indicando el cambio de cancha."""
    if cambio_cancha:
        return """
        +--Cambio de Cancha--+ 
        |        | |        |
        |        | |        |
        |       /   \\       |
        |      /     \\      |
        +-------------------+
        """
    else:
        return """
        +--Misma Cancha--+ 
        |        | |        |
        |        | |        |
        |       /   \\       |
        |      /     \\      |
        +-------------------+
        """

def imprimir_ascii_sets(sets, nombres):
    representacion_sets = f"Sets: {sets[0]} - {sets[1]}\n"
    representacion_sets += "  " + nombres[0] + ": " + "🎾" * sets[0] + "\n"
    representacion_sets += "  " + nombres[1] + ": " + "🎾" * sets[1] + "\n"
    return representacion_sets

# Actualizaremos la función imprimir_marcador para incluir arte ASCII
def imprimir_marcador(nombres, puntos, juegos, sets, cambio_cancha):
    print(f"Marcador de puntos: {nombres[0]} {puntos[0]} - {puntos[1]} {nombres[1]}")
    print(f"Juegos (Set actual): {juegos[0]} - {juegos[1]}")
    print(imprimir_ascii_sets(sets, nombres))
    print(imprimir_ascii_cancha(cambio_cancha))

def punto_ganado(marcador, jugador):
    """Actualiza el marcador con el jugador que ganó el punto."""
    if marcador[jugador] == 40:
        if marcador[1 - jugador] < 40: # Gana el juego
            return "juego"
        elif marcador[1 - jugador] == 40:
            marcador[jugador] = "Adv" # Ventaja
        else:
            # Elimina la ventaja del oponente si la tiene
            marcador[1 - jugador] = 40
    elif marcador[jugador] == "Adv":
        # Gana el juego
        return "juego"
    else:
        # Actualiza el marcador de puntos
        marcador[jugador] = 40 if marcador[jugador] == 30 else marcador[jugador] + 15
    return None

def juego_ganado(juegos, sets, jugador):
    """Actualiza los juegos y sets con el jugador que ganó el juego."""
    juegos[jugador] += 1
    if juegos[jugador] >= 6 and (juegos[jugador] - juegos[1 - jugador] >= 2):
        # Gana el set
        sets[jugador] += 1
        juegos[0] = 0
        juegos[1] = 0
        return True
    return False



def main():
    nombres = []  # Lista para almacenar los nombres de los jugadores
    puntos = [0, 0]  # Marcador de puntos para el juego actual
    juegos = [0, 0]  # Juegos ganados en el set actual
    sets = [0, 0]  # Sets ganados

    # Entrada de datos nombres de los jugadores
    nombres.append(input("Nombre del Jugador 1: "))
    nombres.append(input("Nombre del Jugador 2: "))

    jugador_saque = 0  # Jugador que inicia sacando
    cambio_cancha = False

    while sets[0] < 2 and sets[1] < 2:  # Continua mientras ningún jugador haya ganado 2 sets
        try:
            ganador_punto = int(input(f"Quién ganó el punto? [0] {nombres[0]}, [1] {nombres[1]}: "))
            resultado = punto_ganado(puntos, ganador_punto)
        except IndexError:
            print("Opción inválida. Intente de nuevo.")
            continue
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue

        if resultado == "juego":
            if juego_ganado(juegos, sets, ganador_punto):
                print(f"Set ganado por {nombres[ganador_punto]}")
                if sets[0] == 2 or sets[1] == 2:
                    print(f"Partido ganado por {nombres[ganador_punto]}")
                    break
            puntos = [0, 0]  # Reinicia el marcador de puntos
            jugador_saque = 1 - jugador_saque  # Cambio de saque

        if (juegos[0] + juegos[1]) % 2 != 0:
            cambio_cancha = not cambio_cancha
            print("Cambio de cancha")

        imprimir_marcador(nombres, puntos, juegos, sets, cambio_cancha)


# Comentar la llamada a main para prevenir ejecución automática en este entorno
main()
