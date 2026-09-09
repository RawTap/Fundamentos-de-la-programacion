import random

formas=["piedra","papel","tijera"]

jugador=input("Selecciona piedra, papel o tijera: ")
computadora=random.choice(formas)

ganador={("piedra","tijera"),("papel","piedra"),("tijera","papel")}
if jugador == computadora:
    resultado="Empate"
elif (jugador, computadora) in ganador:
    resultado="Ganaste"
else:
    resultado="Perdiste"

print(f"{resultado}, la computadora eligió {computadora}.")
