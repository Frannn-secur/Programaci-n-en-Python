"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

1º Pedimso al usuario dos números. (uno que sera el inicial y otro el final)
2º Si el numero es impar le sumaremos uno y llegaremos hasta el final
3º Si el número es par lo sacaremos solo
4º Si el primer numero insertado es mas grande que el segundo los cambiamos y hacemos el mismo algoritmo

"""

print("A través de dos numeros que voy a pedirte te dire todos los posibles números pares que hay entre el valor "
      "inicial y el valor final")

num_inicial = int(input("Este será el valor inicial/mínimo: "))
num_final = int(input("Este será el valor final/maximo: "))

if num_inicial < num_final:
    if num_inicial % 2 == 0:
        for i in range(num_inicial, num_final + 1, 2):
            print(i)
    else:
        for i in range(num_inicial, num_final + 1, 2):
            print(i)
else:
    if num_inicial > num_final:
        num_inicial, num_final = num_final, num_inicial
        for i in range(num_inicial, num_final + 1, 2):
            print(i)
    else:
        for i in range(num_inicial, num_final + 1, 2):
            print(i)
