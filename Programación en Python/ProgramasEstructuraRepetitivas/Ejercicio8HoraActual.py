"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Hora actual

1º Importamos la calse time para poder usar el método .sleep y otros métodos utiles como .localtime y .strftime
2º Creamos la hora_local que le daremos el valor time.localtime()
3º Le daremos el formato del cronómetro y lo sacamos por pantalla
4º Le ponemos que espere 1s con el método sleep

"""

import time

while True:
    # Le damos el valor time.localTime() que coge los segundos transcurridos actualmente y lo transforma en una hora
    # Local
    hora_local = time.localtime()
    # time.strftime lo que hace es trasnforma esa cantidad de tiempo en la cadena que nosotros querramos
    final = time.strftime("%H:%M:%S", hora_local)
    print("\b"*8 + final, end="")
    time.sleep(1)

