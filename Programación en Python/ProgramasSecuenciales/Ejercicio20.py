"""
Creado el día 18/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas
monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

Pedimos cada moneda, sumamos todos los euros y los centimos y luego pasamos los euros a centimos.
"""

print("Cuantas monedas de 2€ tienes: ")
moneda_2euros = int(input())
print("Cuantas monedas de 1€ tienes: ")
moneda_1euro = int(input())

# Esta sería la suma de los euros que tendrías
suma_euros = moneda_2euros * 2 + moneda_1euro

print("Cuantas monedas de 50 centimos tienes: ")
moneda_50centimos = int(input())
print("Cuantas monedas de 20 centimos tienes: ")
moneda_20centimos = int(input())
print("Cuantas monedas de 10 centimos tienes: ")
moneda_10centimos = int(input())

# Esto sería la suma de las monedas de centimos que tendrías
suma_centimos = moneda_50centimos * 50 + moneda_20centimos * 20 + moneda_10centimos * 10

# Convertimos los centimos a euros y se lo sumamos a los euros anteriores.

total_centimos = suma_centimos % 100
total_euros = suma_euros + (total_centimos / 100)
print("Esto sería todo en euros: " + str(total_euros))