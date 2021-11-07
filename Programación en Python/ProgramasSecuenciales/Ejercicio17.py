"""
Creado el día 09/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar
a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

Hay que convertir la hora y los minutos de la salida a segundos y sumárselos a los segundos que ha tardado en llegar a
la otra ciudad
"""

print("Hora de la que ha partido de la ciudad: ")
horas_salida = int(input())
print("Minutos de los que ha partido de la ciudad: ")
minutos_salida = int(input())
print("Segundos a los que ha salido de la ciudad: ")
segundos_salida = int(input())
print("El tiempo en segundos que ha tardado en llegar a la otra ciudad: ")
segundos_llegada = int(input())

print("Lo pasamos todo a segundos para poder sumarle los segundos de la llegada a la otra ciudad: ")
segundos_totales = horas_salida * 3600 + minutos_salida * 60 + segundos_salida + segundos_llegada

horas_finales = segundos_totales // 3600
minutos_finales = (segundos_totales % 3600) // 60
segundos_finales = (segundos_totales % 3600) % 60
print("La hora a la que ha llegado a la otra ciudad sería " + str(horas_finales) + " horas " + str(minutos_finales) +
      " minutos y " + str(segundos_finales) + " segundos")

