"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Crea un programa que pida al usuario billetes_200 números y muestre su división si el segundo no es cero, o un mensaje de aviso
en caso contrario.

Algoritmo:

1º Pedimos billetes_200 números al usuario.
2º Calculamos la división si el segundo número insertado es diferente de 0.
3º Si el segundo número es 0, sacar como salida --> No podemos hacer una división entre 0.
4º Si todo esta bien sacaremos el número de la división.

"""

print("Vamos a calcular la división de billetes_200 números que me vas a insertar: ")

print("Insertame el dividendo: ")
numero1 = int(input())
print("Insertame el divisor: ")
numero2 = int(input())

if numero2 != 0:
    resultado = numero1 / numero2
    print("El resultado de la división de ambos números son: ", resultado)
else:
    print("No podemos hacer una división con el divisor siendo = 0")


