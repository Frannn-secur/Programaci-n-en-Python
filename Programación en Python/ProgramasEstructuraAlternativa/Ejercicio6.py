"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz


Programa que lea una cadena por teclado y compruebe si es una letra mayúscula

Algoritmo:

1º Pedimos una cadena de una letra.
2º Calculamos si la cadena correspondiente es una letra mayuscula o no.
3º Sacamos por teclado si es una letra minúscula o mayúscula.

"""

print("Insertame una cadena de una letra y te diré si es una letra en minúscula o en mayúscula: ")

cadena = input()

if cadena == cadena.upper():
    print("Es una cadena en mayúscula")
else:
    print("Es una cadena en minúscula.")
