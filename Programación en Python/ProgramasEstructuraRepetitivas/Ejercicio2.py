"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe
informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

1º Pedimos una cantidad de números al usuario
2º Todos estos números se clasificaran en valores tanto positivos, negativos o 0, por lo que haremos un contador de cada
uno para tenerlos controlados, y los inicializaremos
3º Haremos un for in range(cantidad metida por el usuario) de cualquier número que inserte el usuario y le diremos si es
mayor, menor o igual que cero
4º Una vez terminado el loop lo que haremos será sacar por pantalla los tres contadores con sus respectivas
informaciones recopildas

"""

print("Vamos a calcular la cantidad de números positivos, negativos o neutros que presenta el número que me vas a "
      "insertar: ")

# Al tratarse de 3 cantidades de números diferentes lo primero que haremos será inicializar las 3 variables de ellos.

num_positivos = 0
num_negativos = 0
num_ceros = 0

# Pedimos el número al usuario (cuando le pedimos el número, vamos a basar nuestro ciclo en ese número)

num_usuario = int(input("Insertame un número de la veces que se va a hacer el loop: "))

for n in range(num_usuario):
    num = float(input("Introduceme un número para decirte como es: "))
    if num > 0:
        print("El número insertado es positivo")
        num_positivos += 1
    elif num < 0:
        print("El número insertado es negativo")
        num_negativos += 1
    else:
        print("El número insertado es un cero")
        num_ceros += 1

print("Cantidad de números positivos obtenidos: ", num_positivos)
print("Cantidad de números negativos obtenidos: ", num_negativos)
print("Cantidad de números ceros obtenidos: ", num_ceros)

