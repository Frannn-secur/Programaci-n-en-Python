"""
Creado el día 06/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Calcular el perímetro y área de un rectángulo dada su base y su altura.

"""

print("Vamos a hacer el perímetro y el area del siguiente rectángulo dada su base y su altura: ")

print("Dame la base del rectángulo: ")
base = float(input())
print("Dame la altura del rectángulo")
altura = float(input())

perimetro = 2 * base + 2 * altura
area = base * altura

print("El perímetro seria:" + str(perimetro))
print("El área seria: " + str(area))



