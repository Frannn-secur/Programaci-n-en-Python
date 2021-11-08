"""
Creado el día 07/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se
compone de los siguientes porcentajes:

* 55% del promedio de sus billetes_100 calificaciones parciales.

* 30% de la calificación del examen final.

* 15% de la calificación de un trabajo final

"""

print("¿Quieres saber tu nota final de Algoritmos?")

print("Insértame la nota del primer parcial: ")
primer_parcial = float(input())
print("Insértame la nota del segundo parcial: ")
segundo_parcial = float(input())
print("Insértame la nota del tercer parcial: ")
tercer_parcial = float(input())
print("Insértame la nota del examen final: ")
examen_final = float(input())
print("Insértame la nota del trabajo final: ")
trabajo_final = float(input())

promedio_parciales = ((primer_parcial + segundo_parcial + tercer_parcial) / 3) * 0.55
examen_nota_final = examen_final * 0.30
trabajo_nota_final = trabajo_final * 0.15


Total = promedio_parciales + examen_nota_final + trabajo_nota_final
print("La nota total de toda la asignatura sería: " + str(Total))



