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
    3.1º Si la zona es 1 el precio será peso * 24
    2.2º Si la zona es 2 el precio será peso * 20
    2.3º Si la zona es 3 el precio será peso * 21
    2.4º Si la zona es 4 el precio será peso * 10
    2.5º Si la zona es 5 el precio será peso * 18
4º Ponemos por default que va a haber un error si no son esos numeros
"""

print("Segun el peso y la zona de destino la tarifa será de una forma o de otra.")
print("zona 1 --> América del Norte")
print("zona 2 --> América Central")
print("zona 3 --> América del Sur")
print("zona 4 --> Europa")
print("zona 5 --> Asia")

peso = float(input("Insertame cuanto es el peso del objeto que quiere enviar: "))
zona = int(input("A que zona quiere enviar el paquete: "))

if peso > 5:
    print("El paquete no ha sido admitido por el peso")
elif peso < 1:
    print("El paquete no puede tener un peso negativo.")
else:
    if zona == 1:
        print("Segun la zona y el peso su coste de envío será: ", peso * 24)
    elif zona == 2:
        print("Segun la zona y el peso su coste de envío será: ", peso * 20)
    elif zona == 3:
        print("Segun la zona y el peso su coste de envío será: ", peso * 21)
    elif zona == 4:
        print("Segun la zona y el peso su coste de envío será: ", peso * 10)
    elif zona == 5:
        print("Segun la zona y el peso su coste de envío será: ", peso * 18)
    else:
        print("Error en la zona añadida")
