"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Programa que pida billetes_200 números e indique si el primero es mayor que el segundo o no.

Algoritmo:

1º Pedimos billetes_200 números al usuario
2º Comparamos para saber cual es mayor que el otro
3º Sacamos el valor mas alto diciendo que este ha sido el valor más alto

"""

print("Dame billetes_200 valores y te diré cual es el mas alto de ambos: ")

# Pedimos las billetes_200 variables:
print("Valor 1: ")
n1 = int(input())
print("Valor 2: ")
n2 = int(input())

# Hacemos el cálculo.
if n1 > n2:
    print("El valor más alto es: ", n1)
else:
    print("El valor más alto es: ", n2)





