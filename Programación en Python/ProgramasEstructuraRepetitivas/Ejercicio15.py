"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual
adelante que atrás.

1º Pedimos la cadena, la pasamos a minúsculas y le quitamos los espacios y vocales con tildes
2º Creo una variable vacia en la que almacenaremos la cadena invertida
3º Sacamos por pantalla si las cadenas son palíndromos o no

"""
print("Es un programa que a la hora de insertarme una cadena te diré si es palíndroma o no")

VOCALES_CON_TILDE = "áéíóú"
VOCALES_SIN_TILDE = "aeiou"
# Crearemos cadenas, la cadena1 es cadena original en minúsculas, sin espacios ni tildes y la cadena2 es la invertida.
cadena1 = ""
cadena2 = ""
cadena = input("Introduce una cadena para comprobar si es palíndroma: ")

# Pasamos a minúsculas la cadena orginal, quitamos tildes y espacios.
cadena1 = cadena.lower().replace(" ", "")

# Creamos un bucle en el que la cadena reemplazará si hay vocales con tilde por vocales sin tildes.
for i in range(len(VOCALES_CON_TILDE)):
    cadena1 = cadena1.replace(VOCALES_CON_TILDE[i], VOCALES_SIN_TILDE[i])

cadena2 = cadena1[::-1]
if cadena1 == cadena2:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
