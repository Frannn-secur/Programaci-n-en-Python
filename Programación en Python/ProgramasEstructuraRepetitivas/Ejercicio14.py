"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

Para comprobar si una cadena es subcadena de otra iremos desplazando un índice y comparando la subcadena que se inicia
en ese índice con tantos caracteres como la cadena a comprobar con esa misma cadena. Si no es igual pasamos al índice
siguiente y así seguimos hasta que la encontremos o ya no podamos comparar más.
Si no encotramos la subcadena le sacamos que no nos mienta y que nos diga la verdad, si coincide sacamos la subcadena,
junto con la cadena.

"""

# Inicializamos variables
esta_subcadena = False
i = 0

# Pedimos datos
cadena = input("Dame una cadena: ")
subcadena = input(f"Dame una subcadena de '{cadena}': ")

# Proceso de búsqueda de la subcadena
comprobar_hasta = len(cadena) - len(subcadena)
while not esta_subcadena and i <= comprobar_hasta:
    if subcadena == cadena[i:i + len(subcadena)]:
        esta_subcadena = True
    i += 1

# Mostramos resultado
if esta_subcadena:
    print("Muy bien")
else:
    print(f"No me mientas '{subcadena}' no forma parte de '{cadena}'")

