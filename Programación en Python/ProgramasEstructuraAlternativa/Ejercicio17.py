"""

Creado el día 08/11/202

Hecho por Francisco José Gómez Ruiz

Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre
por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número
incorrecto.”.

Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos".

Algoritmo:

1º Pedimos la cara obtenida por el dado al tirarlo
2º Hay varios casos que se pueden dar:
    2.1º En la cara opuesta esta el seis
    2.2º En la cara opuesta esta el cinco
    2.3º En la cara opuesta esta el cuatro
    2.4º En la cara opuesta esta el tres
    2.5º En la cara opuesta esta el dos
    2.6º En la cara opuesta esta el uno
3º Ponemos por default que va a haber un error si no son esos numeros

"""

print("Dame la cara obtenida al tirar el dado: ")

cara_dado = int(input("Esta es la cara: "))

if cara_dado == 6:
    print("Es la cara seis y su cara opuesta sería el 1.")
elif cara_dado == 5:
    print("Es la cara cinco y su cara opuesta sería el 2.")
elif cara_dado == 4:
    print("Es la cara cuatro y su cara opuesta sería el 3.")
elif cara_dado == 3:
    print("Es la cara tres y su cara opuesta es el 4.")
elif cara_dado == 2:
    print("Es la cara dos y su cara opuesta es la 5.")
elif cara_dado == 1:
    print("Es la cara uno y su cara opueta es la 6.")
else:
    print(exit(1))


