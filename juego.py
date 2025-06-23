from descriptor import Personaje
import random
import time

nombre = input("Bienvenido a Gran Fantasía ¿Cual es el nombre de tu personaje?: ")
jugador=Personaje(nombre)
print (jugador.estado)

Orco=Personaje("orco")
Probabilidad = jugador.probabilidad(Orco)

p = Personaje.dialogo(Probabilidad)

while p == 1:
    resultado = "G" if random.uniform(0, 1) < Probabilidad else "P"
    if resultado == "G":
        print("""
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!""")
        jugador.estado = 50
        Orco.estado = -30
    else:
        print("¡Oh no! ¡El orco te ha ganado!")
        time.sleep(1.5)
        print ("¡Has perdido 30 puntos de experiencia!")
        time.sleep(2)
        jugador.estado = -30
        Orco.estado = 50

    print(jugador.estado)
    print(Orco.estado)

    Probabilidad = jugador.probabilidad(Orco)
    p = Personaje.dialogo(Probabilidad)