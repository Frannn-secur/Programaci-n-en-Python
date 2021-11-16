"""

Creado el día 08/11/202

Hecho por Francisco José Gómez Ruiz

La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta
dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto, los siguientes tres, 80 céntimos por minuto
, los siguientes dos minutos, 70 céntimos por minuto, y a partir del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%, y en turno de tarde,
10%. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

Algoritmo:

1º Preguntamos el tiempo que ha estado en llamada
2º Le preguntamos al usuario si es domingo, si NO es domingo y tampoco es por la tarde el cargo del impuesto es de 0.15,
si no es domingo y es por la tarde el impuesto es de 0.1
3º Si la llamada se ha realizado el domingo el cargo por minuto será 0.3
4º Si el tiempo ha sido menos de 5 minutos, el precio de la llamada será el tiempo durado * 100
5º Si no, el tiempo ha sido igual o menor de 8 minutos la llamada, el precio será el tiempo durado - 5 (porque lo que va
a costar mas sería los siguiente 3 min) * 80 y le sumamos a ese resultado 500 (que sería 5 min = 5€
6º Si no, el tiempo ha sido igual o menor de 10 minutos la llamada, el precio será el tuempo durado - 8 (por que los
siguientes 2 min seran de 70 cent) y le sumariamos 740 del resto de los minutos
7º Si no, el tiempo sería 10 min y por lo cual el ultimo min costaria 50 cent por lo que sería 880 + (tiempo-10) * 50

"""

print("Programa que calcula el precio de una llamada.")

tiempo = int(input("Inserta los minutos que ha durado dicha llamada: "))

# Comprobamos el impuesto a añadir.
domingo = input("¿Es domingo?(S/N) ")
if domingo.upper() == "N":
    tarde = input("¿Es turno de tardes?(S/N) ")
    if tarde.upper() == "N":
        # Impuestos de mañanas.
        impuesto = 0.15
    else:
        # Impuestos de tardes.
        impuesto = 0.1
else:
    # Impuestos de domingos.
    impuesto = 0.03

# Calculamos el coste de la llamada.
if tiempo <= 5:
    precio = tiempo * 100
elif tiempo <= 8:
    precio = 500 + (tiempo-5) * 80
elif tiempo <= 10:
    precio = 740 + (tiempo-8) * 70
else:
    precio = 880 + (tiempo-10) * 50

print(f"El precio final de la llamada es {precio * (1 + impuesto) / 100:.2f} €")
