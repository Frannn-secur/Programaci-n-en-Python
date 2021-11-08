"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz


Crea un programa que lea la edad de billetes_200 personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que
ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

Algoritmo:

1º Pedimos billetes_200 edades al usuario.
2º Calculamos cual edad es mas alta que la otra
3º En caso de igualdad de edad pondremos por salida --> Tienen ambas personas la misma edad
4º Si todo esta correcto sacaremos una edad que es más alta que la otra.

"""

print("Insertame la edad de las billetes_200 personas para saber cual és mas joven: ")

edad1 = int(input("Primera edad de la primera persona: "))
edad2 = int(input("Segundad edad de la segunda persona: "))

if edad1 < edad2:
    print("La edad mas joven sería la de la primera persona con: ", edad1, "annos")
if edad1 > edad2:
    print("La edad mas joven sería la de la segunda persona con: ", edad2, "annos")
if edad1 == edad2:
    print("La edad en ambas personas es la misma.")
