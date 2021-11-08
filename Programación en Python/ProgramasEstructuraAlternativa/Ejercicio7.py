"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz


Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir billetes_100
cosas:

El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

Algoritmo:

1º Pedimos la base y el exponente al usuario
2º Si el exponente es posivito imprimiremos la potencia
3º Si el exponente es 0, el resultado siempre será 1
4º Si el exponente es negativo, será 1/potencia con el exponente que antes era negativo ahora positivo y lo imprimimos

"""

print("Insertame la base y el exponente de la potencia para hacerla: ")

base = int(input("Esta sería la base: "))
exponente = int(input("Esto sería el exponente: "))

if exponente > 0:
    potencia = base ** exponente
    print("Esta sería la potencia si tiene el exponente positivo: ", potencia)
if exponente == 0:
    potencia = 1
    print("Esta sería la potencia con el exponente = 0: ", potencia)
else:
    potencia = 1/base ** -exponente
    print("Esta sería la potencia si el exponente fuese negativo: ", potencia)

