"""

Creado el día 25/10/2021

Hecho por Francisco José Gómez Ruiz

Haz un programa que juegue al piedra/papel/tijera contra el ordenador, que usará números aleatorios para realizar la
tirada. Después de cada jugada pregunta al usuario si quiere continuar, en caso negativo se muestra el número de
partidas jugadas, las  ganadas por cada jugador y las empatadas.

Algoritmo:

1º Importamos la random
2º Creamos una variable que va a crear un número aleatorio para la máquina y segun lo que genere, le ganará al usuario,
perderá contra el usuario o acabará en empate.
3º Tendremos que crear para más tarde 4 variables; 1º para almacenar todas las partidas jugadas, 2º para almacenar las
partidas ganas por el usuario, 3º partidas perdidas por el usuario, 4º partidas empatadas por el usuario
4º Creamos ciclo while que pedirá al usuario que nos enseñe un número del 1 al 3 sabiendo que el 1 es la piedra el 2 la
tijera y el 3 la tijera, si nos inserta otro número distinto a eso se lo volveremos a pedir.
5º Creamos una variable incializada a True con el fin de repetir el ciclo, hasta que el usuario diga lo contrario, y en
en ese ciclo comparamos las diferentes posibilidades que se pueden dar a lo largo del juego.
6º Luego le pedimos al usuario si quiere seguir jugando pidiendoselo con dos únicos valores (s/n), en caso de que no nos
de ninguno de esos lo volverá a pedir
7º Si dice que si la variable juega seguira en True y por tanto seguirá trabajando el bucle
8º SI dice que no quiere seguir jugando la variable pasará a False y mostrará por pantalla todas las partidas jugadas
con anterioridad, las partidas que ha ganado el usuario, las partidas que ha perdidio el usuario y las partidas que ha
empatado el usuario

"""

import random

print("Vas a jugar al piedra, papel o tijera contra mi, mucha suerte!")

# Creación del número random de la máquina
num_random = random.randrange(1, 3)

# Creación de dichas variables de almacenamiento
partidas_jugadas = 0
partidas_ganadas = 0
partidas_perdidas = 0
partidas_empatadas = 0

# Pedimos al usuario el número con el que va a jugar
num_usuario = int(input("¿Piedra(1), Papel(2) o Tijera(3)? "))

while num_usuario > 3 or num_usuario < 1:
    print("No podemos jugar si no me insertas un número correcto...")
    num_usuario = int(input("¿Piedra(1), Papel(2) o Tijera(3)? "))

# Sacamos lo que jugaría la máquina
if num_random == 1:
    print("Ordenador juega: Piedra")
elif num_random == 2:
    print("Ordenador juega: Papel")
else:
    print("Ordenadro juega: Tijera")

# Creamos la variable juega para hacer el ciclo
juega = True

# Mientras sea verdad que juega el ciclo se repetirá y comparará todo
while juega:

    if num_usuario == 1 and num_random == 1:
        print("Empate, Piedra a Piedra")
        partidas_jugadas += 1
        partidas_empatadas += 1
    elif num_usuario == 2 and num_random == 2:
        print("Empate, Papel a Papel")
        partidas_jugadas += 1
        partidas_empatadas += 1
    elif num_usuario == 3 and num_random == 3:
        print("Empate, Tijera a Tijera")
        partidas_jugadas += 1
        partidas_empatadas += 1
    elif num_usuario == 1 and num_random == 2:
        print("Perdiste, Piedra a Tijera, lo siento...")
        partidas_jugadas += 1
        partidas_perdidas += 1
    elif num_usuario == 1 and num_random == 3:
        print("Me ganaste!!, Piedra a Papel")
        partidas_jugadas += 1
        partidas_ganadas += 1
    elif num_usuario == 2 and num_random == 1:
        print("Me ganaste!!, Papel a Piedra")
        partidas_jugadas += 1
        partidas_ganadas += 1
    elif num_usuario == 2 and num_random == 3:
        print("Perdiste, Papel a Tijera, lo siento...")
        partidas_jugadas += 1
        partidas_perdidas += 1
    elif num_usuario == 3 and num_random == 2:
        print("Me ganaste!!, Tijera a Papel")
        partidas_jugadas += 1
        partidas_ganadas += 1
    elif num_usuario == 3 and num_random == 1:
        print("Perdiste, Tijera a Piedra, lo siento...")
        partidas_jugadas += 1
        partidas_perdidas += 1

    # Le preguntamos al usuario si quiere seguir jugando y no
    sigue_jugando = str(input("¿Quieres seguir jugando? (s/n): "))
    if sigue_jugando == "s":
        juega = True
        num_usuario = int(input("¿Piedra(1), Papel(2) o Tijera(3)? "))
    elif sigue_jugando == "n":
        print("Vale esto son los resultados: ")
        juega = False
    else:
        while sigue_jugando != "s" and sigue_jugando != "n":
            print("Esta feo que no me digas si quieres volver a jugar conmigo o no bien...")
            sigue_jugando = str(input("¿Quieres seguir jugando? (s/n): "))

# Sacamos por pantalla los resultados.
print("Esto serían las partidas jugadas: ", partidas_jugadas)
print("Esto serían las partidas perdidas: ", partidas_perdidas)
print("Esto serían las partidas ganadas: ", partidas_ganadas)
print("Esto serían las partidas empatadas: ", partidas_empatadas)

