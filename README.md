# MisionTic2022

## Clase #1
[Notas](/NotasDeClase/Clase1.md)
![Clase1](/Imagenes/MisionTic_Clase1.jpg)

## Input

![Input](/Imagenes/Input.png)


## Introducción

### Problemas

La resolución de problemas es una habilidad muy importante de un programador.

**Problema**: Cuando se desea encontrar uno o varios objetos desconocidos.

Para solucionar un problema debemos saber que objetos conocemos y las relaciones entre ellos. Un programador no puede resolver un problema que no entiende.

**Divide y vencerás**
- Descomponer un problema en subproblemas. Resolver los subproblemas y se combinan para tener la solución general.

#### Tipos de problemas:
*   Condicionado: Información necesaria para la solución.
*   Mal Condicionados: Sin información necesarias o respuesta sujeta a opinión.
    *   Sentimientos, emociones, cultura, etc....
    *   Relación no bien dada.
*   Computables: Secuencia de pasos, para definir la relación entre Entrada y Salida.
    *   Sin solución: Indecibles o no Computables.
*   Tratables: Solución Finita.
*   Intratables: Crecimiento exponencial.
*   Solucionables: Salida valida para entrada dada.
*   No Solucionable: Se tiene claro la relación pero no es posible encontrar la salida.

Analizar para entender y descomponer para resolver.

"Todos en este país deberían aprender a programar una computadora, porque enseña como pensar" - Steve Jobs

### Algoritmos

Problemas con secuencia finita de tareas bien definidas, para que desde una entrada se pueda generar una salida. Secuencia de pasos para llegar a la solución final.

Un algoritmo de programación se escribe y puede ejecutarse en cualquier lenguaje que requiera.

**Programado**: Descripción de la secuencia finita para que el computador solucione el problema.

#### Caracteristicas de un algoritmo:
*   Precisión: Definido
*   Determinismo
*   Finitud

#### Esta conformado por:
*   Datos: Información
*   Instrucciones: Las acciones
*   Estructuras de control: El orden de ejecución

#### Recursos
*   Tiempo: Tiempo definido para ejecutar la operación.
    *   Tiempo = tiempo * operaciones básicas
*   Espacio: Memoria que debe mantener
    *   S = numero de bytes * variables del algoritmo

Los programas necesitan ser ejecutados de manera rápida, para esto necesitan algoritmos ágiles que no tengan mucho tiempo de espera.

Los algoritmos son una parte esencial de la programación.

# Ciclos
-15 de Junio 2021

**Ciclos While**

Estructura general
```python
while(condición):  # Una condición que en algún momento es falsa, oh se detiene en algún momento.
    código...
    break # Nos sirve para detener ciclos.
```
**Ejemplos:**

1-
```python
    i = 0
    while (i<=6):
        print(i)
        i += 1   # Cuando la i > 6 la condición se vuelve falsa.
```
2-
```python
    i=2
    j=25
    while i < j:
        print(i,j,sep=", ") # Que hace sep=", " ?
        i *= 2
        j+= 10
    print("the end")
    print(i,j,sep=", ")
```

Como encontrar el mínimo número positivo representable por la máquina:

```python

def min_maquina():
    Xo = 1.0
    Xi = Xo / 2.0
    while Xi > 0.0:
        Xo = Xi
        Xi = Xo / 2.0
    return Xo

print("El mínimo numero positivo", end=" ")
print("En Esta maquina es", min_maquina())
```
```
El minimo numero positivo en esta maquina es 5e-324
```

El ciclo do while no existe como tal en Python. Pero se puede recrear.
Es mejor intentar no usar break, en ciclos while.

Mas Ejemplos:

```python
dato = 1
suma = 0
i = 0

while(dato !=0):
    dato = int(input("Ingrese un numero entero: "))
    suma += dato
    i += 1
i -=1 # fuera del cuerpo del while
promedio = suma/i

print(i, suma, promedio)
print(type(promedio))

````


```python
i = 1
anterior = 1
nuevo = 1/2

while nuevo < anterior:
    penultimo = anterior
    anterior = nuevo
    i+=1
    nuevo = 1/2**i

print(i-2,penultimo)

```

**Estudiar los incrementos de range en for**


```python


for i in range(0, 3): #El incremento por default es 0
    print(i, end=" ") #-> 0 1 2

for i in range(3, 0):
    print(i, end=" ") # Nada

for i in range(-3, 0):
    print(i, end=" ") #-> -3 -2 -1

for i in range(-6, 0, 2): #El tercer valor es el incremento
    print(i, end=" ") #-> -6 -4 -2

for i in range(0, 6, 2):
    print(i, end=" ") #-> 0 2 4

for i in range(10, 0, 2):
    print(i, end=" ") #-> Nada

for i in range(10, 0, -2):
    print(i, end=" ") #-> 10 8 6 4 2


for i in range(-10, 0, -2):
    print(i, end=" ") #Nada

for i in range(-10, 0, 2):
    print(i, end=" ") # -> -10 -8 -6 -4 -2

```

Podemos usar estos ciclos for para sacar los numeros impares o pares:

```python
for i in range (1, 99+1, 2):  # Numeros impares hasta el 99
    print("impar", i)

for i in range(2,100+1,2): #Numeros pares hasta el 100
    print("pares", i)
```

Calculas 2^n utilizando multiplicaciones sucesivas.

```python
def dosElevado(n):
    prod = 1
    for i in range (1, n+1):
        prod*= 2
    return prod
n = 5

print("2 elevado a la", n, "=", dosElevado(n))
```
```
2 elevado a la 5 = 35
```
Como funciona dosElevado?

Si queremos el resultado de 2^5 llamamos la función con 5.
-> dosElevado(5)

**Pasos de la función:**

dosElevado(5):
*   prod = 1
*   for i in range (1,5+1): **Repetir 5 veces**
    *   prod = 1 * 2 = 2   *- Paso 1*
    *   prod = 2 * 2 = 4   *- Paso 2*
    *   prod = 4 * 2 = 8   *- Paso 3*
    *   prod = 8 * 2 = 16  *- Paso 4*
    *   prod = 16 * 2 = 32 *- Paso 5* **STOP**
*   return **prod**

Como prod = 35, entonces nos retorna **35**

## Cadenas

* \t = tabulado
* \n = nueva linea
* \u01F4 = carácter unicode especifico

**Ejemplo**
```python
print("Cadena con un tabulado \t y una nueva \n linea")
```
```
Cadena con un tabulado  y una nueva
linea
```

Para concatenar palabras utilizamos el operador +
```python
nombre = "Ingrid"
apellido = "E"

print(nombre + ' ' + apellido)
```
```
Ingrid E
```
**Comparar cadenas**
* == : Comparar si son iguales
* < : Ver que palabra es mayor o menor según el código de la letra.


```python
'''
El codigo ASCCI de 'a' = 97
                   'b' = 98
'''
print('a' < 'b') #True

print('Rosas' == 'a') #False no son iguales

'''
R-82-o-111-s-115-a-97-s-115 = 529
R-82-o-111-j-106-a-97-s-115 = 511
'''
print('Rosas' > 'Rojas') #True

print("Rojas" is "Rojas") #True
```

Las cadenas de palabras str se pueden utilizar como arrays

Si tenemos la variable
<br> nombre = "Hola Mundo" <br>
Cada letra tiene una **posición**
*   nombre[0] = 'H'
*   nombre[1] = 'O'
*   nombre[2] = 'L'
*   nombre[3] = 'A'

```python
nombre = "Ingrid E"
for i in range(0,8):
    print(nombre[i], end=' ')

#-> I n g r i d   E

for i in nombre:
    print (i, end=' ')

#-> I n g r i d   E
```

El metodo *len()* nos permite obtener el largo de las palabras str
*   len("hola") = 4

También, podemos usar las listas para sacar subcadenas de las palabras

```python
palabra = "MisionTic 2022"
print(palabra[0]) # M
print(palabra[:5]) # Misio
print(palabra[0:7]) # MisionT
print(palabra[6:10]) # Tic
'''
Si utilizamos el :: nos devuelve la palabra por intervalos.
Si es negativo el intervalo va desde atrás.
Si es positivo va normal.
'''
print(palabra[::-1]) # 2202 ciTnoisiM
print(palabra[::-2]) # 20 inii
print(palabra[:: 2]) # MsoTc22
```

**Método count**
<br> Retorna el numero de veces que se encuentra una subcadena en una cadena.
*   obj.count(subcadena, ini,fin)

```python
obj = "The avengers"
print(obj.count('e')) # 3
print(obj.count('e',4,len(obj))) #2

cad = 'abcabcabcabcabc'
print(cad.count('abc')) # 5

```


**Método find/rfind()**

Nos permite encontrar partes de las palabras. find sirve para encontrar la primera, y rfind para encontrar la ultima.


```python
palabra = "Hola amigos buenos dias, Hola"
print('primera:', palabra.find("Hola")) # primera: 0
print('ultima:', palabra.rfind("Hola")) # ultima: 25
```

**Método mayúsculas y minúsculas**

* .lower() = cadena en minúsculas
* .upper() = cadena en mayúsculas
* .capitalize() = primera letra Mayúscula
* .title() = primera letra de cada palabra mayúscula
* .swapcase() = intercambia Mayúsculas y minúsculas

**Método strip/lstrip/strip()***
<br> Sirve para recortar o eliminar caracteres deseados.
*   .lstrip('-+') :  Elimina los especificado desde la izquierda.
*   .strip('-+') :  Elimina lo especificado al principio y final del string.
*   .rstrip('-+') :  Elimina los especificado desde la derecha.

 Si no se pone nada el default es espacios.

```python
txt = "     banana     "
x = txt.lstrip()

print("of all fruits", x, "is my favorite") # of all fruits banana     is my favorite

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")

print(x) # banana

txt = "     banana     "
x = txt.rstrip()

print("of all fruits", x, "is my favorite") # of all fruits      banana is my favorite

```

**Método split**
<br> Divide la cadena en una subcadena delimitadora

```python
sdate = "01-06-2021"
spi = sdate.split("-")
print(sp1) # -> ['01','06', '2021']
print('dia: ', sp1[0], 'mes:', sp1[1], 'año', sp1[2])
```

**Métodos para justificar**
*   .ljust(15,"-"): Añade '-' a el lado derecho de la cadena hasta que la cadena mas los '-' tengan un largo de 15.
*   .rjust(15,"-"): Lo mismo que ljust pero agrega los - en la izquierda.
*   .center(15,"-"): Agrega '-' en los dos lados hasta que el largo sea 15 y quede centrado.
*   .zfill(15): Agrega 0 en la izquierda hasta que tenga el largo 15

**Método replace**
<br> --- Remplaza una subcadena x por otra.

```python
string = "Cien años de soledad"
print(string) # Cien años de soledad
replace = string.replace('Cien', 'Setenta')
print(replace) # Setenta años de soledad
replace = string.replace('años', 'dias')
print(replace) # Cien dias de soledad
replace = string.replace('a','#')
print(replace) # Cien #ños de soled#d
```
**Método para revisar tipo**
<br> Utilizamos estos métodos para Determinar si la cadena contiene un valor.

*   .endswith('.') : Determinar si termina con '.'
*   .startswith('B') : Determinar si empieza con 'B'
*   .isaplha() : Determinar si contiene letras unicamente.
*   .isdigit() : Determinar si contiene solo numeros.
*   .isspace() : Determinar si una cadena es un titulo
*   .islower() : Si todos su caracteres están en minúscula.
*   .isupper() : Si todos su caracteres están en mayúscula.

**Código ASCII**

*   ord('x') : Retorna el numero ASCII que representa la 'x'

```python

codigo = ord(input("ingrese un solo char: ")) #-> 7
print(codigo)
print(48 <= codigo <= 57) #True

```
**Ejemplos:**

Determinar si un numero entero corresponde a una vocal minúscula.

```python
d = int(input("numero entero: "))

if d == 96 or d == 101 or d == 111 or d==117:
    print(True)
else
    print(False)

print(chr(d))
```

Implementar una función potencia sin utilizar el operador **, ni la función logarítmica.

Entrada: Numero (x), Potencia(n)
Salida: Resultado Potencia (p)

p = x * x * x * x ..... n veces.

Casos a tener en cuenta:
si n == 0 entonces x = 1
si n < 0 entonces 1/(x^n)

```python

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

print(potencia(x,n)) #0.1111111

```

Generar las tablas de multiplicación del 1 al 9

```python

for i in range(1, 10):
    print(i, ':', end='')
    for j in range(1,10):
        prod = i * j
        print('\t', prod, end='')
    print('', end='\n')
```

```
Tabla de multiplicar de 1 al 9

1 :      1       2       3       4       5       6       7       8       9
2 :      2       4       6       8       10      12      14      16      18
3 :      3       6       9       12      15      18      21      24      27
4 :      4       8       12      16      20      24      28      32      36
5 :      5       10      15      20      25      30      35      40      45
6 :      6       12      18      24      30      36      42      48      54
7 :      7       14      21      28      35      42      49      56      63
8 :      8       16      24      32      40      48      56      64      72
9 :      9       18      27      36      45      54      63      72      81
```

## Tuplas

Declaraciónes de tuplas.

*   tuple_1 = 1,2,3
*   tuple_2 = (0,1,2,3)
*   tuple_3 = (tuple_1,tuple_2)

Podemos tener 2 tuplas en 1 sola tupla, pero si queremos que las dos se combinen
en una sola tupla entonces usamos el operador +.
<br>
El operador *n utilizado con tuplas, no permite repetir la tulpa n cantidad de veces.

``` python
tuple_1 = 1,2,3
tuple_2 = ('A','B','C')
tuple_3 = (tuple_1,tuple_2)

print(tuple_1) # (1, 2, 3)
print(tuple_2) # ('A', 'B', 'C')
print(tuple_3) # ((1, 2, 3), ('A', 'B', 'C'))
print(tuple_1+tuple_2) # (1, 2, 3, 'A', 'B', 'C')
print(tuple_2 * 2) # ('A', 'B', 'C', 'A', 'B', 'C')
```

Para comparar tuplas, utilizamos los operadores de comparación.

``` python
tuple_1 = 'Rojas',123
tuple_2 = 'Rosas',123
tuple_3 = 'Rosas', 23
tuple_4 = 'Rojas', 23

print(tuple_1 < tuple_2) # True
print(tuple_1 == tuple_2) # False
print(tuple_3 > tuple_4) # True
print(tuple_3 < tuple_4) # False
```

El operador **is** sirve para determinar si dos tuplas referencia al mismo objeto.

``` python
tuple_1 = 'Rojas',123
tuple_2 = "Rojas",123
tuple_3 = 'Rojas',
tuple_4 = 123,
tuple_5 = tuple_3 + tuple_4

print(tuple_1 == tuple_2) #True
print(tuple_1 is tuple_2) #True
print(tuple_1 == tuple_5) #True
print(id(tuple_1)) #1801309591232
print(id(tuple_2)) #1801309591232
```

Para aceder a elementos en una tupla utilizamos [indice]
<br> Cuando es un signo negativo se considera un recorrido desde la inversa

```python
colores = ("Rojo", "Azul", "Verde", "Morado")

print(colores[2]) #Verde
print(colores[-2]) #Verde
```

Ciclos for con tuplas
``` python
colores = ("Rojo", "Azul", "Verde", "Morado")

for color in colores:
    print(color,end=', ') # Rojo, Azul, Verde, Morado,
```
**Asignarle valores a la tuplas**

Podemos asignarle variables a la tuplas.

``` python
colores = ("Rojo", "Azul", "Verde", "Morado")

r,a,v,m = colores

print(r) #Rojo
print(v) #Verde
print(a) #Azul
print(m) #Morado

tupla = (10,9,8,7,6,5)
a,b,c,d = [tupla[i] for i in (1,2,3,4)]
print(a,b,c,d) # 9 8 7 6
a,b,c,d = [tupla[i] for i in (1,1,2,2)]
print(a,b,c,d) # 9 9 8 8
a,b,c = [tupla[i] for i in range(0,6,2)]
print(a,b,c) # 10 8 6
```
Mas metodos para tuplas

``` python
tupla = (10,9,8,7,6,5)
print(tupla[::-1]) # (5, 6, 7, 8, 9, 10)

print(tupla.index(10), tupla.index(8), tupla.index(5)) # 0 2 5

print(max(tupla), min(tupla)) # 10 5

repetidos = (1,1,1,1,3,2,3,2)

print(repetidos.count(1)) # 4
print(repetidos.count(2)) # 2
print(repetidos.count(3)) # 2
print(repetidos.count(4)) # 0
```

Podemos volver una palabra en una tupla facilmente usando el metodo tuple()

``` python
nombre = "Ingrid"
tupla_Nombre = tuple(nombre)
print(tupla_Nombre) #('I', 'n', 'g', 'r', 'i', 'd')
```
## Listas
22/06/2021
<br>
Donde podemos almacenar datos como: int, float, str, tuple, dicc, etc.. <br>
En una lista separamos los datos con una '**,**' <br>
La **diferencia** que tiene con la tuplas es que, las listas son mutables es decir que se pueden modificar.<br>

[ ] Una lista vaciá, las listas pueden contener diferentes tipos de datos. <br>

Se pueden crear listas que tengan listas como elementos:

```python
numList = [0,1,2,3]
letterList = ['A','B','C']
combinationList = [numList, letterList]
print(combinationList) #[[0, 1, 2, 3], ['A', 'B', 'C']]
print(combinationList[0]) #[0, 1, 2, 3]
print(combinationList[1]) #['A', 'B', 'C']
print(combinationList[0][1]) #1
print(numList + letterList) # [0, 1, 2, 3, 'A', 'B', 'C']
```

Existe el método extend para agregar una lista al final de otra lista.
```python
numList = [0,1,2,3]
letterList = ['A','B','C']

numList.extend(letterList) # [0, 1, 2, 3, 'A', 'B', 'C'] sirve similar que +
print(numList)
```

Similar a la tuplas podemos crear una lista con múltiples copias de una lista.

```python
numList = [0,1,2,3]
letterList = ['A','B','C']

print(numList*3) # [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
print(letterList * 2) # ['A', 'B', 'C', 'A', 'B', 'C']
```

Los operadores de comparación se utilizan usando el orden lexicógrafo cuando es posible.
Se puede realizar mientras uno a uno de los elementos de la lista sean del mismo tipo.

```python
print(["Rojas", 123] < ["Rosas", 123]) # True
print(["Rosas", 123] == ["rosas", 123]) # False
print(["Rosas", 123] > ["Rosas", 23]) # True
print(["Rosas", "123"] > ["Rosas", "23"]) # False
print(("Rosas", "123") > ("Rosas", 23)) #Error str > int no funciona
```

**Subíndice [ ]**

Se puede aceder a los elementos dentro de la lista empezando desde [0]. Si es [-1] entonces se considera como la posición desde el final.


```python
avengers = ["Ironman", "Thor", "Ant-man", "Hulk"] 
print(avengers[0]) # IronMan
print(avengers[3]) # Hulk
print(avengers[-1]) # Hulk
print(avengers[-3]) # Thor
```

**IN**<br>
Utilizamos el operador in para determinar si un elemento se encuentra en una lista.

Si queremos saber si no se encuentra en la lista utilizamos  not in

```python
text = ["cien", "años", "de", "soledad"]
if "años" in text:
    print("Si esta en la lista")
else:
    print("No esta en la lista")

if "hola" not in text:
    print("No esta en la lista")
else:
    print("Si esta en la lista")

#Si esta en la lista
#No esta en la lista
```

**For**

Podemos iterar una lista utilizando el método for
```python
s = ["hola", "amigos", "mios"]
for palabra in s: # para cada palabra de la lista
    print(palabra, end = ", ")

# hola, amigos, mios
```

Se puede crear una lista utilizando un for adentro.
``` python
d = 10
desplaza = [d + x for x in range(5)]
print(desplaza) # [10,11,12,13,14]
potencias = [3 ** x for x in range(2, 6)]
print(potencias) # [9,27,81,243]
```

Igualmente como las tuplas se le puede agregar variables
``` python
lista = [1, -2, 3]
a, b, c = lista
# a = 1
# b = -2
# c = 3

lista = [11, 9, -2, 3, 8, 5]
var1, var2, var3 = [lista[i] for i in (1, 3, 5)]
print("var1 =", var1, ", var2 =", var2, ", var3 =", var3)
#var1 = 9 , var2 = 3 , var3 = 5
var1, var2, var3 = [lista[i] for i in range(0, 6, 2)]
print("var1 =", var1, ", var2 =", var2, ", var3 =", var3)
# var1 = 11 , var2 = -2 , var3 = 8
```

Las listas tambien contienen estos metodos:
*   Len(lista) = Longitud de la lista
*  .append(valor) _= Agrega un elemento al final de la lista
* .insert(posicion, valor) = Agrega un elemento en una posicion especifica
*   .remove(valor) = elimina donde encuentre primero el valor de izquierda a derecha
*   .count(valor) = Retorna las n veces que se repite un numero
*   .index(valor) = Retorna la posicion del valor si se repite coje el primero.
* max(lista) = Retorna el Maximo valor
* min(lista) = Retorna el Min Valor
* .sort() = De menor a mayor
* .sort(reverse =  True) = De mayor a menor
* list(valor) = Para volver un elemento a una lista
* .pop(posicion/default ultima posicion) = Elimina un elemento en la posicion

## Ejercicios
24/06/2021
'''