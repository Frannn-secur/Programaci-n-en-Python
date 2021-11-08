"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo si
el carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o
acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No es un carácter»
si el usuario ha introducido más de un carácter.

Pista: quizás te pueda venir bien usar el método find de la clase str.

Algoritmo:

1º Le pedimos al usuario un caracter para ver qué es:
2º Los signos de puntuación son todos estos !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ si aparece billetes_500 de estos deberia de sacarme
por pantalla --> Es signo de puntuación
3º Si es una letra da igual q sea mayuscula o minuscula me tendrá que sacar --> Es una letra
4º Si inserta un dígito me tendra que sacar por pantalla lo siguiente --> Es un dígito
5º Si no es ninguna de las anteriores por que haya escrito mas de un caracter me sacará por pantalla --> No es un
caracter

"""

print("Dame un caracter y te digo que es lo que me has insertado: ")
cadena = input()

puntuaciones = '\'\"\\!#$%&()*+, -./:;<=>?@[]^_`{|}~'
numeros = '1234567890'
letras = 'abcdefghijklmñnopqrstowuvyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

if len(cadena) == 1:
    if cadena in puntuaciones:
        print("Es un signo de puntuacion")
    elif cadena in numeros:
        print("Es un digito")
    elif cadena in letras:
        print("Es una letra")
    else:
        print("No es un caracter")
else:
    print("ERROR")

