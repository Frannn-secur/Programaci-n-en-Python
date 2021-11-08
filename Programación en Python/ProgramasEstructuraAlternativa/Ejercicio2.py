"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Indica qué líneas del último programa (y en qué orden) se ejecutarán para cada billetes_500 de los siguientes casos:

1) a = 2 y b = 6
2) a = 0 y b = 3
3) a = 0 y  b = -3
4) a = 0 y  b = 0

Algoritmo:

1) En el primer caso se producirá la ecuacion esperada sin ningun problema, debido a que 'a' es diferente de 0 y por
tanto se puede hacer la ecuación sin ningun tipo de problema

2) En el segundo caso se producirá un error debido a que 'a' es = 0, la secuencia de 'a' != 0 no se cumple pq no es dife
rente por lo que pasamos a la siguiente condicion, la siguiente condición es la de 'a' == 0 dentro de esta tenemos otras
billetes_200 condiciones que serian si 'b' es != 0 o == 0 en este caso al ser diferente de 0 nos da como salida --> La ecucación
no tiene solución

3) En el tercer caso se produce lo mismo que en el apartado billetes_200 puesto que 'a' es == 0 y 'b' es != de 0 por lo que nos
dará como salida --> La ecucación no tiene solución

4) En el cuarto caso se produce un error debido a que 'a' == 0 y 'b' es == 0,  la secuencia de 'a' != 0 no se cumple
porque no es diferente por lo que pasamos a la siguiente condicion, la siguiente condición es la de 'a' == 0 dentro de
esta tenemos otras billetes_200 condiciones que serian si 'b' es != 0 o == 0 en este caso al ser 'b' == 0 se saltaría la línea de
'b' != 0 y nos iriamos a la última condición que nos daría como salida --> La ecuación tiene infinitas soluciones.


"""

print("Programa para la resolución de la ecucación ax + b = 0.")

a = float(input("Valor de a: "))
b = float(input("valor de b: "))

if a != 0:
    x = -b / a
    print("Solución: ", x)

if a == 0:
    if b != 0:
        print("La ecuación no tiene solución.")
    if b == 0:
        print("La ecucación tiene infinitas soluciones.")
