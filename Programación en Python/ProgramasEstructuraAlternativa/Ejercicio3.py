"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Escribe un programa que lea un número e indique si es par o impar.

Algoritmo:

1º Pedimos un número al usuario.
2º Calculamos para saber si es impar o par.
3º Sacamos por pantalla lo que sea el número.

"""

print("Dame un número entero con el fin de decirte si es par o impar: ")

numero = int(input())
resto = numero % 2

if resto == 0:
    print("Es un número par")
else:
    print("Es un número impar")
