"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
realiza un programa que cuente cuantas palabras tiene.

1º Pedimos la cadena
2º Recorremos la cadena con el fin de contar los espacios que tiene y cuando detecte uno, aumentamos nuestra variable
contador de espacios
3º Después mostraremos dicha variable para decir cuantas palabras hay en la cadena insertada.

"""

print("Programa que cuenta las palabras que hay segun los espacios que hay.")
cadena = input("Introduzca la frase: ")
espacios = 0

# El .strip nos devolverá una copia de la cadena sin espacios en blanco, pero podemos hacerlo tmb sin ella.

for i in cadena:
    # i va a pasar por todos los huecos de la cadena, una vez pase por un espacio en blanco, sumará el espacio.
    if i == " ":
        espacios += 1

print(f"Hay {espacios + 1} palabras.")
