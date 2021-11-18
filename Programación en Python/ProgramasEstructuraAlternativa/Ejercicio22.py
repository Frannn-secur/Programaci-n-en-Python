"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Realiza un programa que pida cinco números enteros y diga cuál es el mayor.

1º Pedimos al usuario 5 números
2º Comparamos el primer número con el segundo, el tercero, el cuarto y el quinto sea mayor
3º Si el segundo número es mayor que el primero, tercero, cuarto y quinto número
4º Si el tercer número es mayor que el primero, segundo cuarto y quinto número
5º Si el cuarto número es mayor que el primero, segundo, tercero  y quinto número
6º Si el quinto número es mayor que el resto de los número añadidos anteriormente
5º Ponemos como mensaje de error en caso de que los cinco números sean iguales ponemos --> Error los 5 números son
iguales.

"""

print("Insertame los 5 números para decirte cual es mayor de todos: ")

n1 = int(input("Insertame el número 1: "))
n2 = int(input("Insertame el número 2: "))
n3 = int(input("Insertame el número 3: "))
n4 = int(input("Insertame el número 4: "))
n5 = int(input("Insertame el número 5: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print("El número 1 es el número mayor de los 5")
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print("El número 2 es el número mayor de los 5")
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print("El número 3 es el número mayor de los 5")
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print("El número 4 es el número mayor de los 5")
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print("El número 5 es el número mayor de los 5")
else:
    print("Error los cinco números son iguales")
