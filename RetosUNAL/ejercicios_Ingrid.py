import math
'''
Conocidos los tres lados de un triàngulo,
determine su respectivo tipo.

3. Equilatero: 3 lados iguales.
2. Isósceles: 2 lados iguales.
1. Escaleno: Ningún lado igual

'''
lados_Triangulo = input("Introduce los lados del triàngulo: ").split()
a = lados_Triangulo[0]
b = lados_Triangulo[1]
c = lados_Triangulo[2]

def tipoTriangulo():
    if a != b or a != c or b != c:
        print("Escaleneo")
    elif a == b and b==c:
        print("Equilatero")
    else:
        print("Isósceles")

tipoTriangulo()

'''
Haga una expresión que devuelva el N de días que tiene
el mes m (30 días trae nov, abril,junio y septiembre.
28 solo 1, los demás 31), donde bisiesto = 1, si el
año es bisiesto o 0 si no es bisiesto.

'''
mes = input("El numero del mes ")
bisiesto = input("El año es bisiesto? 1- Si, 0- No ")

def numero_Dias():
    treinta_Dias = 30*(mes==11 or mes == 4 or mes == 6 or mes == 9)
    veintiocho_Dias = (28+bisiesto)*(mes == 2)
    treintaYUno_Dias = 31*(mes ==1 or mes ==3 or mes==5 or mes==7 or mes ==8 or m==10 or mes ==12)
    return treinta_Dias + veintiocho_Dias+ treinta_Dias

print(numero_Dias())

'''
Decir si un nro entero m es exactamente divisible entre
otro numero entero n. 1 significa que si es divisible, 0
que no lo es.
'''
numeros = input("Ingresa los números: ").split()
m = numeros[0]
n = numeros[1]

def divisible():
    if(m%n == 1):
        print("Divisible")
    else:
        print("No Divisible")

divisible()

'''
Determine si un año es bisiesto.
1: Si es bisiesto
0: No es bisiesto

Un año bisiesto si es divisible entre 4, pero
no es divisible entre 100, o si es divisible entre
400
'''