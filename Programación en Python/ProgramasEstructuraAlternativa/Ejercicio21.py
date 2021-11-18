"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Realiza un programa que pida tres números enteros y diga cuál es el mayor.

1º Pedimos al usuario 3 números
2º Comparamos el primer número con el segundo y el tercero
3º Si el segundo número es más grande que el primer número y el tercero
4º Si el tercer número es más grande que el primero y el segundo número
5º Ponemos como mensaje de error en caso de que los tres números sean iguales ponemos --> Error los 3 números son
iguales.

"""

print("Insertame 3 número para decirte cual es el mayor de los 3: ")

n1 = int(input("Insertame el número 1: "))
n2 = int(input("Insertame el número 2: "))
n3 = int(input("Insertame el número 3: "))

if n1 > n2 and n1 > n3:
    print("El número 1 es el número mayor de los 3")
elif n2 > n1 and n2 > n3:
    print("El número 2 es el número mayor de los 3")
elif n3 > n1 and n3 > n2:
    print("El número 3 es el número mayor de los 3")
else:
    print("Error los 3 números son iguales")
