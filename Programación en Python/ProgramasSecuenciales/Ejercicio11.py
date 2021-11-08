"""
Creado el día 07/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Pide al usuario billetes_200 números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de
modo que el resultado sea siempre positivo).

"""

print("Me vas a insertar billetes_200 números con la finalidad de calcularte la distancia de ambos: ")

print("Dame el primer número: ")
numero_1 = float(input())
print("Dame el segundo número: ")
numero_2 = float(input())

distancia = abs(numero_1 - numero_2)
print("La distancia entre ambos número es: " + str(distancia))
