"""
Creado el día 09/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene
ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?

La raíz cuadrada la podemos hacer a través de la función sqrt de la librería math cuando la importamos pero la raíz
cúbica no debido a que no podemos elevar nada en esa función por lo que lo haríamos elevando el numero a 1/3.
"""

import math

print("Dame un número para hacerte la raíz cuadrad y su raíz cúbica: ")
num = int(input())

raiz_cuadrada = math.sqrt(num)
raiz_cubica = round(num ** 1/3, 1)

print("Esta sería la raíz cuadrada: " + str(raiz_cuadrada))
print("Esta sería la raíz cúbica: " + str(raiz_cubica))



