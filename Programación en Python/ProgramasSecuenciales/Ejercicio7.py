"""
Creado el día 07/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos
corresponde.

"""

print("Dame una cantidad de números para mostrarlos por horas y minutos")
numero = int(input())

# Realizamos los cálculos correspondientes
horas = (numero // 60)
minutos = numero % 60

# Mostramos los resultados
print("Esto sería el resulta de esa cantidad: " + str(horas) + " horas " + str(minutos) + " minutos")
