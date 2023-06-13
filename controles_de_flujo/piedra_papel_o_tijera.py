print("!bienvenido a piedra, papel o tijera¡")

jugador1 = input("jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("jugador 2, elige piedra, papel o tijera: ").lower()

if jugador1 == jugador2:
    print("empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("¡jugador 1 has ganado!")
else:
    print("¡jugador 2 has ganado!")