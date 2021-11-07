"""
Creado el día 07/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto
dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
tomando en cuenta su sueldo base y comisiones.

"""

print("Insértame las tres comisiones que tienes: ")

# Pedimos valores al usuario
venta_1 = float(input())
print("El valor de la primera venta es el siguiente: " + str(venta_1))
venta_2 = float(input())
print("El valor de la segunda venta es el siguiente: " + str(venta_2))
venta_3 = float(input())
print("El valor de la tercera venta es el siguiente: " + str(venta_3))

# Realizamos cálculos con las variables
comision_ventas = venta_1 * 0.1 + venta_2 * 0.1 + venta_3 * 0.1
print("")

print("A continuación debes insértame el sueldo base para poder hacer el sueldo total: ")
sueldo_base = float(input())
print("El valor del sueldo base sería: " + str(sueldo_base))
print("")
# Resultado total
sueldo_total = comision_ventas + sueldo_base
print("Este sería el sueldo total: " + str(sueldo_total))






