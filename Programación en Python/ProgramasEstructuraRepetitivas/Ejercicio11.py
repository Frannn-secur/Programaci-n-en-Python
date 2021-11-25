"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
realiza un programa que cuente cuantas palabras tiene.

1º Pedimos la cadena y el caracter al usuario (nos aseguramos que sea un solo caracter)
2º Recorremos la cadena a la vez que comparamos con nuestro caracter
3º Mostramos la cantidad de veces que sea mostrado el caracter en la cadena

"""

print("Programa que cuenta las palabras que hay segun los espacios que hay.")
cadena = input("Introduzca la frase: ")
espacios = 0

# El .strip nos devolverá una copia de la cadena sin espacios en blanco, pero podemos hacerlo tmb sin ella.

for i in cadena:
    if i == " ":
        espacios += 1

print(f"Hay {espacios + 1} palabras.")
