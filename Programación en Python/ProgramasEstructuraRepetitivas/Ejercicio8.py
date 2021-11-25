"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.

1. Definimos horas, minutos y segundos a 0;
2. Mientras VERDADERO:
3.  Imprimir HORAS:MINUTOS:SEGUNDOS;
4.  Segundos = segundos + 1;
5.  Esperar un segundo;
6.  Si segundos == 60:
7.      segundos = 0;
8.      minutos = minutos + 1;
9.      Si minutos == 60:
10.         minutos = 0;
11.         horas = horas + 1;
12. Mover el cursor al principio de linea
"""

import time

print("Este programa es un cronometro\n"
      "-------------------------------------------")

horas = 0
minutos = 0
segundos = 0

while True:
    print(f"{horas:02}:{minutos:02}:{segundos:02}", end="")
    segundos += 1
    time.sleep(1)

    if segundos == 60:
        segundos = 0
        minutos += 1

        if minutos == 60:
            minutos = 0
            horas += 1

    print(8 * "\b", end="")
