"""
Creado el día 07/10/2021

@author: Francisco José Gómez Ruiz

Algoritmo: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto
deberá pagar finalmente por su compra.

"""

print("La tienda hace un descuento del 15% al total de la compra: ")

compra = float(input())
print("Está sería la compra sin el descuento: " + str(compra) + "€")

descuento_tienda = compra * 0.15
compra_final = -(descuento_tienda - compra)
print("Este sería el descuento que le haría a la compra" + str(descuento_tienda) + "€")

print("Y esto es lo que pagaría el cliente: " + str(compra_final) + "€")



