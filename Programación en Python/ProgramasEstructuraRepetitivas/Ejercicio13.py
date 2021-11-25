"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

1º Pedimos la cadena.
2º Recorremos la cadena para saber si estamos enfrente de un caracter en minúscula o en mayúscula.
3º Después usaremos la función swapcase para convertir dicho caracter en su contrario.
4º Lo sacamos por pantalla

"""

print("Pedimos una cadena para transformarla segun este, pasando los caracteres minúsculos a mayúsculas y viceversa: ")

cadena = str(input("Dame la cadena: "))
cadena_final = ""

# Usamos los métodos islower y isupper para ver si la cadena fuese minuscula o mayuscula
for i in cadena:
    if i.islower() or i.isupper():
        # Con la funcion swapcase nos quitamos de problemas ya que lo que sea i lo convertirá a lo otro y viceversa.
        cadena_final += i.swapcase()

print(f"Esta sería la cadena nueva: {cadena_final}")
