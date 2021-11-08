"""
Creado el día 07/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Pide al usuario billetes_200 pares de números x1,y2 y x2,y2, que representen billetes_200 puntos en el plano. Calcula y
muestra la distancia entre ellos.


Para calcular la distancia que hay entre billetes_200 puntos de un eje de coordenadas (debido a que un punto tiene un par
de numero hay que hacer el modulo de ambos lo cual seria hacer la raíz cuadrad de la resta de los puntos x al cuadrado
mas la resta de los puntos y al cuadrado
"""

print("Ingrésame el primer punto: ")

print("Dame x1: ")
x1 = float(input())
print("Dame x2: ")
y1 = float(input())

print("Ingrésame el segundo punto: ")

print("Dame x2: ")
x2 = float(input())
print("Dame y2: ")
y2 = float(input())

modulo = round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5, 0)


print("Esta sería la distancia entre ambos puntos: " + str(modulo))
