"""
Creado el día 09/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que
está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los billetes_200
vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
alcanzará el vehículo más rápido al otro.

Lo que queremos saber entre esos billetes_200 coches es en cuantos segundos va a alcanzar el 2 vehículo al 1 (porque el 2
vehículo es mas rápido que el 1) para calcular eso sabemos que la velocidad es igual al espacio recorrido, es decir, la
distancia entre ambos, entre el tiempo en minutos, despejando esta ecuación tendríamos que el tiempo en minutos sería
igual a la distancia entre la velocidad en km/h de ambos coches.

"""

print("Ingrésame la velocidad 1 del primer coche: ")
velocidad_1 = float(input())
print("Ingrésame la velocidad 2 del primer coche: ")
velocidad_2 = float(input())
print("A cuanta distancia están ambos: ")
distancia = float(input())

tiempo = distancia / (velocidad_1 - velocidad_2)
tiempo = -(tiempo * 60)
print("Según la serie de datos que me has dado el tiempo que tardaría en coger el segundo coche al primero sería de:" +
      str(tiempo) + "minutos.")
