"""

Creado el día 19/10/2021

Hecho por Francisco José Gómez Ruiz

Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno
de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas

Algoritmo:

1º Le pedimos x1,y1,r1 y tambien x2,y2,r2
2º Tenemos que calcular la distancia entre los centros
3º Si la distancia que hay entre los centros es mayor que la suma de los radios de las dos circunferencias --> Circunfe-
rencias exteriores
4º Si la distancia que hay entre los centros es igual a la suma de los radios de las dos circunferencias --> Circunfe-
rencias tangentes exteriores
5º Si la distancia que hay entre los centros es menor que la suma de los radios de las dos circunferencias --> Circunfe-
rencias secantes
6º Si la distancia que hay entre los centros es igual al valor absoluto de la resta de los radios --> Circunferencias
tangente interiores
7º Si la distancia que hay entre los centros es mayor que 0 y menor que el valor absoluto de la resta de los radios -->
Circunferencia interiores
8º Si la distancia que hay entre los centros es = 0 --> Circunferencia concéntricas

"""

print("Vamos a calcular cual es el estado de las dos siguientes circunferencias que me va a insertar: ")

# Primera circunferencia
x1 = int(input("Dame la coordenada x1: "))
y1 = int(input("Dame la coordenada y1: "))
r1 = int(input("Dame la coordenada r1: "))

# Segunda circunferencia
x2 = int(input("Dame la coordenada x2: "))
y2 = int(input("Dame la coordenada y2: "))
r2 = int(input("Dame la coordenada r2: "))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1/2
print("Esta seria la distancia", distancia)

if distancia > (r1 + r2):
    print("Esto serian Circunferencias Exteriores")
if distancia == (r1 + r2):
    print("Esto serian Circunferencias Tangentes Exteriores")
if distancia < (r1 + r2):
    print("Esto serian Circunferencias Secantes")
if distancia == abs(r1 - r2):
    print("Esto serian Circunferencias Tangentes Interiores")
if 0 < distancia < abs(r1 - r2):
    print("Esto serian Circunferencias Interiores")
if distancia == 0:
    print("Esto serian Circunferencias concéntricas")

