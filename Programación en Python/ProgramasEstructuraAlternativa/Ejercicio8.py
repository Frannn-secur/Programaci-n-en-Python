"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz


Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor
o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo
sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

Algoritmo:

1º Pedimos la nota , la edad y un caracter para el sexo
2º Mostrará ACEPTADA si la nota es >= 5 edad => 18 y si el sexo es F
3º Mostrará POSIBLE si se cumple todo lo anterior pero siendo el sexo M
4º Si no se cumplen dichas condiciones se motrara NO ACEPTADA

"""
print("Insertame la respectiva nota, edad y el sexo (en un caracter): ")

# Pedimos datos al usuario
nota = float(input("La nota sería: "))
edad = float(input("La edad sería: "))
sexo = input("El caracter del sexo sería: ")

# Cálculo de dichas condiciones queridas.
if nota >= 5 and edad >= 18 and sexo == 'F':
    print("ACEPTADA")
    if nota >= 5 and edad >= 18 and sexo == 'M':
        print("POSIBLE")
else:
    print("NO ACEPTADA")
