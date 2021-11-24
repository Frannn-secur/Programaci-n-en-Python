"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el
resultado de la potencia. No se puede utilizar el operador de potencia ni la función.

1º Pedimos el número real (float) y el número positivo (int) al usuario
2º Hacemos un bucle siempre y cuando el exponente sea mayor que 0
3º Dentro del bucle multiplcamos la base tantas veces como de grande sea el exponente insertado por el usuario.

"""

print("A través de la base y el exponente que me digas, te daré la potencia sin ningun uso de operadores y funciones.")

base = float(input("Esto sería la base de la potencia: "))
exponente = abs(int(input("Esto sería la exponencia de la base en la potencia: ")))

# Creamos la potencia e igualamos a 1 para poder almacenar el valor de ella

potencia = 1

# Hacemos un ciclo de tal forma que vamos quitando valores del exponente a la vez que vamos multiplicando el base por
# ella misma tantas veces como de grande sea el exponente.

while exponente > 0:
    potencia *= base
    exponente -= 1

print("La potencia sería: ", potencia)

