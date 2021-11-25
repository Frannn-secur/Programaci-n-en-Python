"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

1º Creamos una variable que nos almacenará los números primos que queremos mostrar dado por el usuario, creamos una
variable numero_primo = 0 con el fin de ir subiendola
2º Creamos un for en el que el rango va a ser esa cantidad
3º if numero_primo % 1 or numero_primo % numero_primo lo sacaremos por pantalla y le sumaremos uno al numero_primo
4º else sumaremos 1 al numero primo

"""
import math

while True:
    cantidad_primos = int(input("¿Cuantos primos quieres sacar por pantalla?"))
    if cantidad_primos > 0:
        break
        # Con esto lo que quiero es obligar al usuario a sacar un número más alto de 0 y que no me pueda dar valores
        # negativos

print("1º 2")
numero_primos_mostrados = 1
siguiente_numero = 3

while numero_primos_mostrados < cantidad_primos:
    # Pienso que es primo hasta que piense como dividirlo
    es_primo = True
    dividir = 3
    # El siguiente número que iría sería el 3 por lo que sabemos que ya es impar
    while dividir <= math.sqrt(siguiente_numero) and es_primo:
        if siguiente_numero % dividir == 0:
            # Si esto se da significa que no es primo, por lo que cambiamos la variable y salimos del bucle
            es_primo = False
            # Solo queremos en si, numeros impares puesto que los pares sabemos que siempre se van a poder dividir
        dividir += 2
    if es_primo:
        numero_primos_mostrados += 1
        print(f"{numero_primos_mostrados}: {siguiente_numero}")
    siguiente_numero += 2


