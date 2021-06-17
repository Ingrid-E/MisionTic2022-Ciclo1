from math import pi
# pi es una variable global
# pi = 3.141592653589793

'''
Las variables globales son muy útiles
'''

def volEsfera(r1):
    return (4/3)*pi*(r1**3)

# Ciclos While

def min_maquina():
    Xo = 1.0
    Xi = Xo / 2.0
    while Xi > 0.0:
        Xo = Xi
        Xi = Xo / 2.0
    return Xo

#print("El minimo numero positivo", end=" ")
#print("en esta maquina es", min_maquina())

# Ejemplos de while


i = 1
anterior = 1
nuevo = 1/2

while nuevo < anterior:
    penultimo = anterior
    anterior = nuevo
    i+=1
    nuevo = 1/2**i

#print(i-2,penultimo)

#Ejemplo de for
'''
for i in range(10, 0,-1): #El tercer valor es el incremento
    print(i)
'''
#Calcular 2**n utilizando multiplicaciones sucesivas = 2 . 2 .2 . 2 ....n veces

def dosElevado(n):
    prod = 1
    for i in range (1, n+1):
        prod*= 2
    return prod
n = 5

print("2 elevado a la", n, "=", dosElevado(n))

'''
Pasos dosElvedo(n)

Si queremos el resultado de 2^5 llamamos la función con 5.

dosElevado(5):
    prod = 1
    for i in range (1,5+1): #Repetir 5 veces
        prod = 1 * 2 -> 2 # 1
        prod = 2 * 2 -> 4 # 2
        prod = 4 * 2 -> 8 # 3
        prod = 8 * 2 -> 16 # 4
        prod = 16 * 2 -> 32 #5 <- Stop
    return prod

# Como prod = 35, entonces nos retorna 35



'''

