"""

Creado el día 18/11/202

Hecho por Francisco José Gómez Ruiz

Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, proporcione la
calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las siguientes:
«Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual
que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).

1º Pedimos al usuario que nos de su nota
2º Si ese número es < 5 le sacaremos por pantalla que esta suspenso
3º Si ese número es >= 5 le sacaremos por pantalla que esta aprobado
4º Si ese número es  >= 5 and < 7 sacaremos por pantalla notable
5º Si ese número es >= 7 and < 9 sacaremos por pantalla Sobresaliente
6º Si ese número es >=9 and < 10 sacaremos por pantalla Matrícula de Honor
5º Ponemos como mensaje de erro que la nota insertada no esta dentro de la calificacion cualitiva habitual

"""

print("Pedimos al usuario la nota y le sacamos por pantalla su correspondiente calificación: ")

nota = int(input("Insertame tu nota para ser tu calificación: "))

if nota < 5:
    print("Esta nota esta SUSPENSA.")
elif 5 <= nota < 7:
    print("Esta nota esta APROBADA.")
elif 7 <= nota < 9:
    print("Esta nota es un NOTABLE")
elif 9 <= nota < 10:
    print("Esta nota es SOBRESALIENTE.")
elif nota == 10:
    print("ESTA NOTA ES DE MATRÍCULA DE HONOR!!")
else:
    print("Esta nota que me has insertado es incorrecta")
