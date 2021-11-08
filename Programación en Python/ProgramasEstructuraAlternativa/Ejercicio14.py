"""

Creado el día 08/11/2021

La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos
A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere
determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo
A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B,
se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para
determinar la ganancia obtenida.

Algoritmo:

1º Pediremos al usuario que nos muestre por pantalla los kilos de las uvas, el tipo si es A o B y el precio total de
todo.
2º Si la uva es de tipo A el tamaño será == 1 por lo que si se cumple sumamos 20 céntimos al precio inicial, si esto no
se cumple entonces sumamos 30 céntimos al precio inicial
3º Si el tamaño no es A si no que es B vemos si es de tipo 1 si se cumple le restamos el precio original - 30 si no se
cumple que sea == 1 entonces al precio le - 50
4º Después calcularemos el precio total segun el precio de las uvas y los kilos que se lleve.
5º Y luego mostramos la ganancia obtenida.


"""
# Variables que usaremos a lo largo del algoritmo.

kilos = int(input("Esta es la cantidad de kilos de las uvas que tenemos: "))
precio_por_kilos = float(input("Este sería el precio por kilo de las uvas: "))
tipo_uva = input("El tipo de uva que debería de ser A o B: ")
tamaño_uva = int(input("El tamaño de la uva tiene que ser de 1 o de 2: "))

if tipo_uva == 'A':
    if tamaño_uva == 1:
        precio_por_kilos = precio_por_kilos + 20
    else:
        precio_por_kilos = precio_por_kilos + 30
else:
    if tamaño_uva == 1:
        precio_por_kilos = precio_por_kilos - 30
    else:
        precio_por_kilos = precio_por_kilos - 50

print("Calculamos el total del precio segun la cantidad de kilos y el precio de él mismo: ")

total = precio_por_kilos * kilos

print("Has sacado una ganancia por, ", kilos, "kilos de uva de: ", total, "€")


