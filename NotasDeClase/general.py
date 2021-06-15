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

print("El minimo numero positivo", end=" ")
print("en esta maquina es", min_maquina())

#Problemas

#Ejemplo