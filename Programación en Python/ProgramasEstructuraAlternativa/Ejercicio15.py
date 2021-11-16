"""

Creado el día 08/11/2021

Hecho por Francisco José Gómez Ruiz

El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno
y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o
más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y
si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realiza un
programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

Algoritmo:
1º Lo primero que haríamos sería pedir el numero de Alumnos, y ahora hacemos lo siguiente
2º Si el número de alumnos que nos han dado fuese mayor o igual a 100 sacamos por pantalla --> El pago a la agencia es
de (multiplicamos el numero de alumnos por 65 porque es lo que paga cada alumno)
3º Si no, el numero de alumnos es de 99 a 50 nos sacará por pantalla --> El pago a la agencia es de (multiplicamos el
numero de alumnos por 70 euros porque sería lo que pagaría cada uno)
4º Si no, el número de los alumnos es de 49 a 30  sacamos por pantalla --> El pago a la agencia es de (multiplicamos el
numero de alumnos por 95 porque es lo que pagaría cada alumno)
5º Si no, el número sacamos por pantalla --> Como el numero de alumnos es menor de 30 costará el pago de la agencia
4000/numeroalumnos

"""

print("Vamos a sacar el valor que nos va a costar la agencia de autobuses: ")

numero_alumnos = int(input("Dame el número de alumnos que irían de viaje: "))

if numero_alumnos >= 100:
    print("El pago a la agencia es de ", numero_alumnos * 65, "euros y cada alumno de los que irian al viaje pagaría "
                                                              "65 por persona")
elif 100 > numero_alumnos >= 50:
    print("El pago a la agencia es de ", numero_alumnos * 70, "euros y cada alumno de los que irían al viaje pagaría "
                                                              "70 por persona")
elif 50 > numero_alumnos >= 30:
    print("El pago a la agencia es de ", numero_alumnos * 95, "euros y cada alumno de los que irían al viaje pagaría "
                                                              "95 por persona")
else:
    print("El coste de la agencia del autobús es de 4000 euros  y cada alumno pagaría: ", 4000/numero_alumnos, "€")
