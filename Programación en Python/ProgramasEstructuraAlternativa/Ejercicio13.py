"""

Creado el día 03/11/2021

Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay
billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.

Por ejemplo, si deseamos conocer el desglose de 434€, el programa mostrará por pantalla el siguiente resultado:

2 billetes de 200 euros.
1 billete de 20 euros.
1 billete de 10 euros.
2 monedas de 2 euros.

Algoritmo:
1º Pedimos la totalidad de los euros que tenemos que desglosar
2º Vamos haciendo cada operacion de todos los respectivos billetes, cogiendo como resto la cantidad que sobra del billete
y calculando desde ese resto el resto de los posibles billetes
3º Sacará por pantalla los billetes y monedas que son necesarios para desglosar la cantidad insertada
"""
dinero = int(input('Danos la cantidad exacta de euros a desglosar: '))
# 1º Pasamos la totalidad de euros para billetes de 500
billetes_500 = dinero / 500
# Calculamos el resto que nos sobra de los billetes de 500 y con ello calculamos los billetes de 200
resto_billetes_500 = dinero % 500
billetes_200 = resto_billetes_500 / 200
# Calculamos el resto que nos sobra de los billetes de 200 y con ello calculamos los billetes de 100
resto_billetes_200 = resto_billetes_500 % 200
billetes_100 = resto_billetes_200 / 100
# Calculamos el resto que nos sobra de los billetes de 100 y con ello calculamos los billetes de 50
resto_billetes_100 = resto_billetes_200 % 100
billetes_50 = resto_billetes_100 / 50
# Calculamos el resto que nos sobra de los billetes de 50 y con ello calculamos los billetes de 20
resto_billetes_50 = resto_billetes_100 % 50
billetes_20 = resto_billetes_50 / 20
# Calculamos el resto que nos sobra de los billetes de 20 y con ello calculamos los billetes de 10
resto_billetes_20 = resto_billetes_50 % 20
billetes_10 = resto_billetes_20 / 10
# Calculamos el resto que nos sobra de los billetes de 10 y con ello calculamos los billetes de 5
resto_billetes_10 = resto_billetes_20 % 10
billetes_5 = resto_billetes_10 / 5
# Calculamos el resto que nos sobra de los billetes de 5 y con ello calculamos las monedas de 2
resto_billetes_5 = resto_billetes_10 % 5
moneda_2 = resto_billetes_5 / 2
# Calculamos el resto que nos sobra de las monedas de 2 y con ello calculamos las monedas de 1
resto_moneda_2 = resto_billetes_5 % 2
moneda_1 = resto_moneda_2 / 1
resto_moneda_1 = resto_moneda_2 % 1

# Algoritmo que mantiene el programa en funcionamiento

if billetes_500 != 0:
    if billetes_500 == 1:
        print(billetes_500, 'Bellite de 500 euros.')
    if billetes_500 > 1:
        print(billetes_500, 'Billetes de 500 euros.')
if billetes_200 != 0:
    if billetes_200 == 1:
        print(billetes_200, 'Billete de 200 euros.')
    if billetes_200 > 2:
        print(billetes_200, 'Billetes de 200 euros.')
if billetes_100 != 0:
    if billetes_100 == 1:
        print(billetes_100, 'Billete de 100 euros.')
    if billetes_100 > 1:
        print(billetes_100, 'Billetes de 100 euros.')
if billetes_50 != 0:
    if billetes_50 == 1:
        print(billetes_50, 'Billete de 50 euros.')
    if billetes_50 > 1:
        print(billetes_50, 'Billetes de 50 euros.')
if billetes_20 != 0:
    if billetes_20 == 1:
        print(billetes_20, 'Billete de 20 euros.')
    if billetes_20 > 1:
        print(billetes_20, 'Billetes de 20 euros.')
if billetes_10 != 0:
    if billetes_10 == 1:
        print(billetes_10, 'Billete de 10 euros.')
    if billetes_10 > 1:
        print(billetes_10, 'Billetes de 10 euros.')
if billetes_5 != 0:
    if billetes_5 == 1:
        print(billetes_5, 'Billete de 5 euros.')
    if billetes_5 > 1:
        print(billetes_5, 'Billetes de 5 euros.')
if moneda_2 != 0:
    if moneda_2 == 1:
        print(moneda_2, 'Billete de 2 euros.')
    if moneda_2 > 1:
        print(moneda_2, 'billete de 2 euros.')
if moneda_1 != 0:
    if moneda_1 == 1:
        print(moneda_1, 'Moneda de 1 euros.')
    if moneda_1 > 1:
        print(moneda_1, 'Monedas de 1 euros.')
