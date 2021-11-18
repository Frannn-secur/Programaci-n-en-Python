"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
Algoritmo:

1º Pedimos al usuario que nos inserte un número entre el 1-7
2º Hay varios casos que se pueden dar:
    2.1º Nos inserte uno sacamos por pantalla que es Lunes
    2.2º Nos inserte dos sacamos por pantalla que es Martes
    2.3º Nos inserte tres sacamos por pantalla que es Miercoles
    2.4º Nos inserte cuatro sacamos por pantalla que es Jueves
    2.5º Nos inserte cinco sacamos por pantalla que es Viernes
    2.6º Nos inserte seis sacamos por pantalla que es Sábado
    2.7º Nos inserte siete sacamos por pantalla que es Domingo
3º Ponemos por default que va a haber un error si no son esos numeros

"""

print("Segun el número que me insertes del 1-7 te diré un día de la semana del Lunes-Domingo respectivamente.")

dia_semana = int(input("Dame un número del 1-7 y te digo su respectivo día: "))

if dia_semana == 1:
    print("Es Lunes")
elif dia_semana == 2:
    print("Es Martes")
elif dia_semana == 3:
    print("Es Miercoles")
elif dia_semana == 4:
    print("Es Jueves")
elif dia_semana == 5:
    print("Es Viernes")
elif dia_semana == 6:
    print("Es Sabado")
elif dia_semana == 7:
    print("Es Domingo")
else:
    print("Error")

