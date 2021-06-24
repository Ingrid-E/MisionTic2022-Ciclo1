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

#print("2 elevado a la", n, "=", dosElevado(n))

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

#Cadenas
print("Cadena con un tabulado \t y una nueva \n linea")
nombre = "Ingrid"
apellido = "E"

print(nombre + ' ' + apellido)

print('ab' < 'ba')
print('Rosas' > 'Rojas')
print("Rojas" is "Rojas")

nombre = "Ingrid E"
for i in nombre:
    print (i, end=' ')
print()
palabra = "MisionTic 2022"
print(palabra[0]) # M
print(palabra[:5]) # Misio
print(palabra[0:7]) # MisionT
print(palabra[6:10]) # Tic
print(palabra[:: 2]) # MsoTc22

palabra = "Hola amigos buenos dias, Hola"
print('primera:', palabra.find("Hola"))
print('ultima:', palabra.rfind("Hola"))

txt  = "-----hola----+"
x = txt.strip('-+')
print(x)

obj = "The avengers"
print(obj.count('e'), end="; ")
print(obj.count('e',4,len(obj)))

cad = 'abcabcabcabcabc'
print(cad.count('abc'))

string = "Cien años de soledad"
print(string) # Cien años de soledad
replace = string.replace('Cien', 'Setenta')
print(replace)
replace = string.replace('años', 'dias')
print(replace)
replace = string.replace('a','#')
print(replace)

x = 3
n = -2

def potencia(x,n) -> float:
    p = 1.0
    if n > 0:
        for i in range(1,n+1):
            p *= x
    elif n < 0:
        for i in range(1,-n+1): #(1,-(-n)+1)
            p *= x
        p = 1.0/p
    return p

print(potencia(x,n))

print("Tabla de multiplicar de 1 al 9")

for i in range(1, 10):
    print(i, ':', end='')
    for j in range(1,10):
        prod = i * j
        print('\t', prod, end='')
    print('', end='\n')

print("TUPLAS")
print()

tupla = (10,9,8,7,6,5)
print(tupla[::-1])
print(tupla.index(10), tupla.index(8), tupla.index(5)) 


repetidos = (1,1,1,1,3,2,3,2)
print(repetidos.count(1))
print(repetidos.count(2))
print(repetidos.count(3))
print(repetidos.count(4))

print(max(tupla), min(tupla)) # 10 5

nombre = "Ingrid"
tupla_Nombre = tuple(nombre)
print(tupla_Nombre)

tipos_tuplas= ("holaa" ,122, 0.456)

cadena1 = "23" #<class 'str'>
numero = 1234 #<class 'int'>
cadena = int(cadena1) + numero # Los dos tiene que ser tipo str para concatenar

print(cadena) # Numero: 1234
print(type(cadena)) #<class 'str'>

print("Listas")
print()

numList = [0,1,2,3]
letterList = ['A','B','C']

print(numList*3) # [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
print(letterList * 2) # ['A', 'B', 'C', 'A', 'B', 'C']

print(["Rojas", 123] < ["Rosas", 123]) # True
print(["Rosas", 123] == ["rosas", 123]) # False
print(["Rosas", 123] > ["Rosas", 23]) # True
print(["Rosas", "123"] > ["Rosas", "23"]) # False
#print(("Rosas", "123") > ("Rosas", 23)) #Error str > int no funciona


text = ["cien", "años", "de", "soledad"]
if "años" in text:
    print("Si esta en la lista")
else:
    print("No esta en la lista")

if "hola" not in text:
    print("No esta en la lista")
else:
    print("Si esta en la lista")


print("Ejercicios")
print()

# Leer una lista y convertir sus dígitos numéricos a  enteros.

def leerLista(texto):
    return input(texto).split(' ')

#ll = leerLista('su lista: ') print(ll)

'''
Calcular el producto punto de dos puntos
Producto v con w (v.w)

Formula de Producto Punto
v = (a1,b1,c1)
u = (a2,b2,c2)

producto_punto = (a1*a2)+(b1*b2)+(c1*c2)
'''

'''
Punto directo vectores multiplicados
v = (a1,b1,c1)
u = (a2,b2,c2)
[a1*a2,b1*b2,c1*c2]
'''


'''
Hallar la mediana de un arreglo
'''

def mediana(A):
    A.sort()
    middle = int(round(len(A)/2, 0))
    print(A[middle])

#mediana([6,-3,4,5,3,2])


'''
colocar los 0 al final del arreglo
'''

def zerosBack(list):
    for i in list:
        if i == 0:
            list.remove(i)
            list.append(i)
    print(list)

zerosBack([0,0,0,5,6,0,7,-3,8,0,-2,0])




