"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes
correspondiente.

1º Pedimos al usuario que nos inserte un número entre el 1-12
2º Hay varios casos que se pueden dar:
    2.1º Nos inserte uno sacamos por pantalla que es Enero y tiene 31 días.
    2.2º Nos inserte dos sacamos por pantalla que es Febrero y tiene 28 días.
    2.3º Nos inserte tres sacamos por pantalla que es Marzo y tiene 31 días.
    2.4º Nos inserte cuatro sacamos por pantalla que es Abril y tiene 30 días.
    2.5º Nos inserte cinco sacamos por pantalla que es Mayo y tiene 31 días.
    2.6º Nos inserte seis sacamos por pantalla que es Junio y tiene 30 días.
    2.7º Nos inserte siete sacamos por pantalla que es Julio y tiene 31 días.
    2.8º Nos inserte ocho sacamos por pantalla que es Agosto y tiene 31 días.
    2.9º Nos inserte nueve sacamos por pantalla que es Septiembre y tiene 30 días.
    2.10º Nos inserte diez y sacamos por pantalla que es Octubre y tiene 31 días.
    2.11º Nos inserte once y sacamos por pantalla que es Noviembre y tiene 30 días.
    2.12º Nos inserte doce y sacamos por pantalla que es Diciembre y tiene 31 días.
3º Ponemos por default que va a haber un error si no son esos numeros

"""

print("Segun el número que me insertes del 1-12 te diré un mes del año de Enero-Diciembre respectivamente, con sus "
      "correspondientes días.")

mes = int(input("Dame un número del 1-12 y te digo su respectivo mes y dias que tiene: "))

if mes == 1:
    print("Es Enero con 31 días")
elif mes == 2:
    print("Es Febrero con 28 días")
elif mes == 3:
    print("Es Marzo con 31 días")
elif mes == 4:
    print("Es Abril con 30 días")
elif mes == 5:
    print("Es Mayo con 31 días")
elif mes == 6:
    print("Es Junio con 30 días")
elif mes == 7:
    print("Es Junio con 31 días")
elif mes == 8:
    print("Es Agosto con 31 días")
elif mes == 9:
    print("Es Septiembre con 30 días")
elif mes == 10:
    print("Es Octubre con 31 días")
elif mes == 11:
    print("Es Noviembre con 30 días")
elif mes == 12:
    print("Es Diciembre con 31 días")
else:
    print("Error")
