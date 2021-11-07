"""
Creado el día 06/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius

"""

print("Dame los grados en Fahrenheit para pasarlo a grados Celsius: ")

grados_F = float(input())
print("Estos serian los grados en Fahrenheit: " + str(grados_F))
operacion = ((grados_F - 32) * 5) / 9

print("Al pasarlo a Celsius sería lo siguiente: " + str(operacion))
