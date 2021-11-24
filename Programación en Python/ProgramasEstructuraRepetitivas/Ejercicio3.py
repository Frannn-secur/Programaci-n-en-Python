"""

Creado el día 20/11/202

Hecho por Francisco José Gómez Ruiz

Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina
cuando se introduce un espacio.

1º Pedimos al usuario un carácter inicial para poder hacer un loop
2º El bucle se repetirá hasta que el usuario no inserte un espacio, momento que el usuario lo inserte se acaba el
programa
3º Creamos una variable estática con todas las vocales
4º Si dicha cosa insertada no es una vocal sacará por pantall NO VOCAL, si lo insertado es una vocal sacará VOCAL

"""

print("Algoritmo creado para saber tantas veces como el usuario quiera, si el caracter insertado por el mismo es una "
      "vocal o no: ")

# Creamos la variable estática que tendra almacenada todas las vocales

VOCALES = "AEIOUaeiou"

caracter = str(input("Insertame el caracter y te digo lo que es: "))

# En python hay una funcion de String que es isalpha, esta funcion saca un True si lo insertado es un caracter.

while caracter.isalpha() != True or len(caracter) != 1:
    caracter = str(input("No puedes insertarme más de un caracter o un número recuerda... "))

while caracter != " ":
    if caracter in VOCALES:
        print("Es una VOCAL lo que has insertado")
        caracter = str(input("¿Quieres insertarme otro caracter?"))
    else:
        print("Lo que has insertado NO ES UNA VOCAL")
        caracter = str(input("¿Quieres insertarme otro supuesto caracter?"))
