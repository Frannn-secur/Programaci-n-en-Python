"""
Creado el día 06/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Calcular la media de billetes_100 números pedidos por teclado.

"""

print("Dame billetes_100 valores para poder hacer la media: ")

print("Valor 1: ")

valor_1 = float(input())
print("este es el valor_1: " + str(valor_1))

valor_2 = float(input())
print("Este es el valor 2: " + str(valor_2))

valor_3 = float(input())
print("Este es el valor 3: " + str(valor_3))

media = (valor_3 + valor_2 + valor_1) / 3
print("Esta seria la media de los 3 valores insertados por teclado: " + str(media))

