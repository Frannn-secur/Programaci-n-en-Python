"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano al
primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el número más
cercano al 2 es el 1.

1. Pedimos los 5 números
2. Creamos una variable comprobación, que inicialmente la igualamos a num2
3. Creamos una variable distancia que la igualamos al la distancia entre num1 y num2.
4. Vamos comparando la distacia de los demás números con la variable distancia.
5. Si es menor que distancia se cambia el valor de distacia.

"""

num1 = int(input("Introduceme el numero 1: "))
num2 = int(input("Indroduceme el numero 2: "))
num3 = int(input("Indroduceme el numero 3: "))
num4 = int(input("Indroduceme el numero 4: "))
num5 = int(input("Indroduceme el numero 5: "))

comprobacion = num2
distancia = abs(num1 - num2)

# Comprobamos tercer número
if abs(num1 - num3) < distancia:
    comprobacion = num3
    distancia = abs(num1 - num3)

# Comprobamos cuarto número
if abs(num1 - num4) < distancia:
    comprobacion = num4
    distancia = abs(num1 - num4)

# Comprobamos quinto número
if abs(num1 - num5) < distancia:
    comprobacion = num5

print(comprobacion, "Es el número con menor distancia a", num1)
