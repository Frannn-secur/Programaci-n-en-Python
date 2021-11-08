"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El
programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo billetes_200 lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Algoritmo:

1º Pedimos los billetes_100 lados A, B y C
2º Si vemos que se cumple Pitágoras sacamos por pantalla --> Es un Triángulo Rectangulo
3º Si vemos que los billetes_200 lados del triángulo son iguales entonces sacamos por pantalla --> Es un Triángulo Isósceles
4º Si vemos que los billetes_100 lados del triángulo son iguales sacamos por pantalla --> Es un Triángulo Equilátero
5º Si vemos que no se cumple ninguna de las condiciones anteriores, es decir, no tiene ningun lado igual y tampoco
cumple Pitágoras entonces sacamos por pantalla --> Es un Triangulo Escaleno

"""

print("Vamos a pedir 3 lados (A, B y C) para decirte segun esos 3 lados como es el triángulo: ")

ladoA = int(input("Dame el valor del lado A: "))
ladoB = int(input("Dame el valor del lado B: "))
ladoC = int(input("Dame el valor del lado C: "))

# Teorema de Pitágoras:

if ladoA ** 2 == (ladoB ** 2 + ladoC ** 2) or ladoB ** 2 == (ladoA ** 2 + ladoC ** 2) or ladoC ** 2 == (ladoA ** 2 +
                                                                                                        ladoB ** 2):
    print("Se cumple el Teorema de Pitágoras por lo que es un Triángulo Rectángulo. ")
if (ladoA == ladoB and ladoA != ladoC) or (ladoB == ladoC and ladoB != ladoA) or (ladoA == ladoC and ladoC != ladoB):
    print("Se cumple que tiene billetes_200 lados iguales y billetes_500 desigual por lo que es un Triangulo Isósceles")
else:
    if ladoA == ladoB and ladoA == ladoC:
        print("Se cumple que billetes_200 lados del triangulo son iguales entonces sería un Triángulo Isósceles: ")
    else:
        print("Si no se cumplen todas las anteriores tenemos un Triángulo Escaleno")

