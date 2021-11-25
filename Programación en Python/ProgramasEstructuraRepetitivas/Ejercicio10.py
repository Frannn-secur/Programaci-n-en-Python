"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

1º Pedimos la cadena y el caracter al usuario (nos aseguramos que sea un solo caracter)
2º Recorremos la cadena a la vez que comparamos con nuestro caracter
3º Mostramos la cantidad de veces que sea mostrado el caracter en la cadena

"""

caracter = str(input("Introduceme un caracter: "))
cadena = str(input("Introduceme la cadena: "))
contador = 0

while len(caracter) != 1:
    caracter = str(input("Introducem un solo caracter: "))

# Si ponemos el range(cadena) nos saldría un error de que no puede trabajar con enteros y strings a la vez
for i in cadena:
    if i == caracter:
        contador += 1

print("Se repite el caracter en la cadena: ", contador)
