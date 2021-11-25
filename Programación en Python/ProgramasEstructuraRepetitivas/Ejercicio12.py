"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en
la cadena por el segundo carácter.

1º Pedimos la cadena y dos caracteres
2º Hacemos un while para asegurarnos de que los dos caracteres que nos insertan son caracteres y no son cadenas.
3º Hacemos un for en el que cuando i sea igual al primer caracter nos devolverá una suma del segundo caracter a una
variable aux que tendremos para sustituir la cadena, en caso de que i no sea el caracter tenemos que meter directamente
el valor de i
4º Sacamos por pantalla el valor de la cadena nueva

"""

print("Esto es un programa que pediremos una cadena y dos caracteres, y el primer caracter dentro de la cadena, será "
      "sustituido por el segundo caracter insertado por el usuario")

caracter1 = str(input("Introduceme un caracter1: "))
caracter2 = str(input("Introduceme un caracter2: "))
cadena = str(input("Introduceme la cadena: "))

while len(caracter1) != 1 and len(caracter2) != 1:
    caracter1 = str(input("Introduceme un solo caracter1: "))
    caracter2 = str(input("Introduceme un solo caracter2: "))

# Tenemos que crear una nueva variable vacía con el fin de almacenar los caracteres cambiado en ella.
cadena_final = ""

for i in cadena:
    if i == caracter1:
        cadena_final += caracter2
    else:
        cadena_final += i

print(f"Esta sería la cadena: {cadena_final}")
