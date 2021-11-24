"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A
continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,a demás
de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número
(además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había
generado.)

1º Generamos un número aleatorio del 1 al 100
2º Creamos una variable que almacenará 10 intentos y irá disminuyendo conforme vayamos intentando.
3º Si seguimos teniendo intentos pasa lo siguiente:
        3.1º Leemos un número
        3.2º Lo comparamos con el creado aleatoriamente (decimos en caso de ser mayor o menor al numero generado).
        3.3º Pedimos otro número y pueden pasar dos cosas que se acabe el bucle por que hayamos sacado el número, o que
        haya perdido y por tanto volvemos a preguntar y asi hasta que se acabe los 10 intentos, si se llega aqui,
        sacamos el número generado
"""

import random

print("Voy a generar un número aleatorio del 1-100,¿serás capaz de averiguar cual es el número generado?")

intentos = 10
num_ramdom = random.randrange(1, 100)
num_usuario = int(input("Ingrésame tu número del cual partes: "))

while num_ramdom != num_usuario and intentos > 1:
    if num_ramdom > num_usuario:
        print("El número ingresado es bajo comparado con el numero generado.")
    else:
        print("El número ingresado es alto comparado con el número generado.")
        intentos = intentos - 1

        print("Te quedan ", intentos, "estos intentos.")
        num_usuario = int(input("Vuleve a darme otro valor: "))

if num_ramdom == num_usuario:
    print("ENHORABUENA HAS ACERTADO!!!")
else:
    print("Has perdidio el número era: ", num_ramdom)
