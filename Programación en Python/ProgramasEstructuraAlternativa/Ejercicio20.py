"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central,
América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que
va dirigido. Lo anterior se muestra en la tabla:

ZONA	UBICACIÓN	COSTO/GRAMO
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de
logística y de seguridad.

Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

1º Pedimos al usuario que nos inserte tanto el peso para saber si el producto tiene que ser admitido o no, y la zona
que depende de la zona del 1-5 seran la diferentes ubicaciones puestas en la tabla de arriba.
2º Lo primero es si el peso es > 5 no podrá ser aceptado, si el peso es menor de 1 sacaremos por pantalla que el valor
tiene que ser positivo, osea tiene que ser mayor que 1 pero menor de 5.
3º Dependiendo de la zona horaria el precio a pagar será mayor o menor, hay zonas del 1-4:


    3.1ºNos inserte uno sacamos por pantalla que es Enero y tiene 31 días.
    2.2º Nos inserte dos sacamos por pantalla que es Febrero y tiene 28 días.
    2.3º Nos inserte tres sacamos por pantalla que es Marzo y tiene 31 días.
    2.4º Nos inserte cuatro sacamos por pantalla que es Abril y tiene 30 días.
    2.5º Nos inserte cinco sacamos por pantalla que es Mayo y tiene 31 días.
4º Ponemos por default que va a haber un error si no son esos numeros
"""