"""

Creado el día 08/11/2021

Hecho por Francisco José Gómez Ruiz

Escribir un programa que lea un año indicar si es bisiesto.

Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea
divisible por 400.

Algoritmo:

1º Pedimos el año para calcular si el año es bisiesto o no
2º Hacemos un if para saber si el año puede ser divisible por 400
3º Seguimos haciendo un elif para saber que el año no sea divisible por 100 si no lo es tiene que haber otro elif que
nos confirme que el año es divisible por 4
4º Si nada de lo de antes se ha cumplido es por que no es un año bisiesto

"""

anno = int(input("Introduce dicho año para saber si es bisiesto o no: "))

if anno % 400 == 0:
    print("Es un anno bisiesto.")
elif anno % 100 == 0:
    print("No es un anno bisiesto.")
elif anno % 4 == 0:
    print("Es un anno bisiesto.")
else:
    print("No es un anno bisiesto")

