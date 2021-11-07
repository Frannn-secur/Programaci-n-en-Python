"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Programa que pida dos números e indique si el primero es mayor que el segundo o no.

Algoritmo:

1º Pedimos dos números al usuario
2º Comparamos para saber cual es mayor que el otro
3º Sacamos el valor mas alto diciendo que este ha sido el valor más alto

"""

print("Dame dos valores y te diré cual es el mas alto de ambos: ")

# Pedimos las dos variables:
print("Valor 1: ")
n1 = int(input())
print("Valor 2: ")
n2 = int(input())

# Hacemos el cálculo.
if n1 > n2:
    print("El valor más alto es: ", n1)
else:
    print("El valor más alto es: ", n2)





