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

1º
2º Si vemos que se cumple Pitágoras sacamos por pantalla --> Es un Triángulo Rectangulo
3º Si vemos que los dos lados del triángulo son iguales entonces sacamos por pantalla --> Es un Triángulo Isósceles
4º Si vemos que los tres lados del triángulo son iguales sacamos por pantalla --> Es un Triángulo Equilátero
5º Si vemos que no se cumple ninguna de las condiciones anteriores, es decir, no tiene ningun lado igual y tampoco
cumple Pitágoras entonces sacamos por pantalla --> Es un Triangulo Escaleno

"""
