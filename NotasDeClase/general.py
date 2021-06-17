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

for i in range(10, 0,-1): #El tercer valor es el incremento
    print(i)

