"""
Creado el día 09/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Dado un número de billetes_200 cifras, diseñe un algoritmo que permita obtener el número invertido.

"""

print("Dame el numero que quieres invertir de billetes_200 cifras: ")

num = int(input())
dec = num / 10
uni = num % 10

numero_invertido = round(uni * 10 + dec, 0)
print("Numero invertido: " + str(numero_invertido))
