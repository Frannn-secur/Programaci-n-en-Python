"""
Creado el día 06/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

"""

print("Calcula la hipotenusa de un triangulo rectángulo dados los siguientes catetos: ")

print("Cateto a: ")
a = float(input())
print("Cateto b: ")
b = float(input())

hipotenusa = (a ** 2 + b ** 2) ** 0.5

print("Esta sería la hipotenusa: " + str(hipotenusa))
