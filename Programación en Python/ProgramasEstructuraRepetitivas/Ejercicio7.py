"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así
sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después
de los 20 meses.

1º Creamos una variable estática con los 20 meses, y una variable normal con el primer pago que nos servirá para ir
incrementando dicho mensualidad, tambien inicializaremos una variable --> Totalidad = 0.
2º Hacemos un loop y dentro de él mismo aumentaremos la totalidad con el precio del mes.
3º Dentro de ese loop iremos aumentando * 2 la variable del primer pago.

"""

print("Vamos a calcular cuanto costará un articulo después de los 20 meses si su primer pago fue de 10€.")

MESES = 20
primer_pago = 10

pago_mes = primer_pago
totalidad = 0

# Ciclo para recorrer los 20 meses que dura el periodo de pago y que nos mostrará lo que paga cada mes
for i in range(MESES):
    totalidad += pago_mes
    pago_mes *= 2
    print(i + 1, "º mes paga -->", pago_mes)

print("La totalidad de todos los 20 meses pagando será: ", totalidad)
