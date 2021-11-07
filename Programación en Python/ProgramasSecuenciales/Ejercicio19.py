"""
Creado el día 18/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada respuesta
correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
"""

print("Vamos a calcular nota final del estudiante: ")
print("Introdúceme la cantidad de respuestas correctas que has tenido: ")
correctas = int(input())
print("Introdúceme la cantidad de respuestas incorrectas que has tenido: ")
incorrectas = int(input())
print("Introdúceme la cantidad de respuestas en blanco que has tenido: ")
blanco = int(input())

# No podemos poner la preguntas en blanco porque no sirven para nada puesto que ni restan ni suben nota

nota_final = correctas * 5 + incorrectas * (-1)
print("La nota final del estudiante es: " + str(nota_final))

