"""
Creado el día 09/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Dadas billetes_200 variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que
intercambie los valores de ambas variables y muestre cuanto valen al final las billetes_200 variables.

No solamente necesitamos tener 2 variables si no necesitamos otra variable que guarde el valor de una (en este caso la a
y que esa misma variable aux (auxiliar) le de el valor guardado de "a" a la variable "b"
"""

print("Introduce la variable A: ")
A = int(input())
print("Introduce la variable B: ")
B = int(input())

aux = A
A = B
B = aux

print("Nuevo valor de a: " + str(A))
print("Nuevo valor de b: " + str(B))
