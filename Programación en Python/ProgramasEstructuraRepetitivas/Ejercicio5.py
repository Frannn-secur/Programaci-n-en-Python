"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el
superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes
informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.

1º Pedimos el limite inferior y el superior, en caso de que el limite inferior sea > que el limite superior los volvemos
a pedir
2º Vamos pidiendo números hasta que se encuentre con un 0
3º Despues nos va a decir la suma de los números que han estado dentro de ese intervalo
4º Cuantos números estan fuera del intervalo
5º Si hemos insertado algun número igual al limite del intervalo nos los dira tambien

"""

print("A través de dos límites dados por el usuario, le pediré números y luego le diré la suma de los número dentro de "
      "ese intervalo, la cantidad de número que se quedaron fuera, y si me has insertado números iguales a los limites")

limite_inferior = int(input("Este sería el limite inferior: "))
limite_superior = int(input("este sería el limite superior: "))

suma = 0
contador_numeros_fuera = 0
numeros_limites_iguales = 0

while limite_inferior > limite_superior:
    limite_inferior = int(input("No puedes insertarme un número mayor que el limite superior aqui: "))
    limite_superior = int(input("No puedes insertame un número menor que el limite inferior aquí: "))

numeros = int(input("Ve dandome números: "))

while numeros != 0:
    if limite_inferior < numeros < limite_superior:
        suma += numeros
    else:
        contador_numeros_fuera += 1
        if numeros == limite_superior or numeros == limite_inferior:
            print("Hay un número que es igual al intervalo.")

    numeros = int(input("Insertame otro, pero si me insertas un 0 se acaba el programa: "))

print("La suma de aquellos números que estan dentro del intervalo son: ", suma)
print("Los números que se han quedado afuera son: ", contador_numeros_fuera)