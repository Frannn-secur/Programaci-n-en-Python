"""
Creado el día 09/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

"""

print("Dame el numero que quieres invertir de dos cifras: ")

num = int(input())
dec = num / 10
uni = num % 10

numero_invertido = round(uni * 10 + dec, 0)
print("Numero invertido: " + str(numero_invertido))
