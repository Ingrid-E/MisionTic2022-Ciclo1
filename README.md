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

## Archivos
29/06/2021 <br>
Existen 4 operaciónes que se pueden realizar con archivos desde un programa: <br>
*   Crear
*   Abrir
*   Cerrar
*   Eliminar
Modos de abrir archivos en **Python** son:
*   w : Escribir en el archivo, creandolo si no existe y si si sobreescribiendolo.
    *   w+ : Borra cualquier dato que existe en el archivo y lo deja como nuevo
*   r+ : Leer el archivo y escribir en el archivo desde el principio
*   a+ : Leer el archivo y escribir al final del archivo (append)
*   -x : Crear archivos
*   b  : Leer archivos binarios, se agrega al final de los otros modificadores:
    *   wb,ab,r+b,a+b

Para abrir archivos utilizamos el metodo <br>
open(ruta del archivo, 'r')

```python
def leerArch(path):
    modo = 'r'
    with open(path, modo) as f:
        data = f.read()
        data = f.read(6) #Especificamos que queremos leer en la
                         # segunda linea 6 bytes
    return data
path = 'files/data.txt' #Relativo al ejemplo mostrado
data = leerArch(path)
print(data)

with open(path, 'w') as f:
    data = "Escribiendo en el archivo 123"
    f.write(data) #Esto se escribe en el archivo 3 veces
    f.write(data)
    f.write(data)
```

Podemos especificar el tipo de codificación para la lectura del archivo.<br>
with open(ruta del archivo, modo, encoding="utf-8") as f: <br>

El metodo **readline()** sirve para leer el contenido de cada linea por individual. Las lunes se pueden cargar como un archivo si se utiliza el comando readlines().

```python
with open("files/data1.txt", 'r', enconding="utf-8") as f:
    print("Nombre del archivo: ", f.name)
    lista = f.readlines()
print(lista) # Nos devuelve una lista con las lineas.
```

La forma mas eficiente de abrir y procesar un archivo es leerlo linea por linea:

```python
with open("files/data1.txt", 'r', enconding="utf-8") as f:
    for line in f:
        print(line, end="")
```

Si queremos escribir datos en un archivo que no son cadenas de texto, podemos hacer.

```python
values = [1,2,3,4, False]

with open(path, 'w+') as f:
    for value in values:
        str_value = str(value)
        f.write(str_value)
        f.write('\n')
```

El metodo seek nos permite ubicar el puntero en la posición que deseemos dentro del archivo<br>

Si tenemos un archivo con:<br>

Las quince letras <br>
12345 <br>
5678 <br>


```python
with open(path, 'r', enconding='utf-8') as f:
    f.seek(11,0) # <- Empezamos a leer la info desde aqui
    for line in f:
        print(line)
```

Este metodo nos retorna: <br>

letras <br>
12345 <br>
5678 <br>

El metodo **tell** nos permite obtener la longitud de un archivo o la posición donde se encuentra.

```python
with open(path, 'a+') as f:
    print(f.tell()) # Retorna 29 con el archivo anterior

```

Para **editar** un archivo dado es utilizando list.insert(i, x), que permite insertar nuevos datos a la lista. Una vez creada se puede unir con **join** y escribirlo sobre el archivo. <br>

Si tenemos el archivo: <br>
Esta es la linea 1: abcabcabcabc <br>
Esta es la linea 2: abcabcabcabc <br>
Esta es la linea 3: abcabcabcabc <br>

Primero abrimos el archivo en modo lectura y luego leemos sus lineas, lo guardamos, lo modificamos y lo abrimos de nuevo para guardar la nueva linea.

```python
# Abre el archivo en modo de s ́olo lectura
with open("files/data5.txt", "r", encoding="utf-8") as f:
    list_content = f.readlines()
list_content.insert(1, "Esta es la l ́ınea 1.5: jajaja\n")

# Re-abre el archivo en modo de s ́olo escritura
# para sobreescribir la versi ́on anterior de  ́este
with open("files/data5.txt", "w", encoding="utf-8") as f:
    contenido = "".join(list_content)
    f.write(contenido)
```

La archivo queda como: <br>
Esta es la linea 1: abcabcabcabc <br>
Esta es la linea 1.5: jajajaja <br>
Esta es la linea 2: abcabcabcabc <br>
Esta es la linea 3: abcabcabcabc <br>

Existen muchas mas funciones que nos ayudan con la lectura de archivos en python: <br>

Si utilizamos **import os** podemos aplicar funciones de esa libreria <br>

*   os.scandir()
*   pathlib.Path()

```python
import os
entries = os.scandir("files/")
for entry in entries:
    print(entry.name + ", es directorio: " + str(entry.is_dir()) + "size" + str(entry.stat().st_size) + " bytes.")

#salidas:
data.txt, es directorio: False, size: 17 bytes.
data1.txt, es directorio: False, size: 95 bytes.
data2.txt, es directorio: False, size: 131 bytes.
data3.txt, es directorio: False, size: 32 bytes.
data4.txt, es directorio: False, size: 31 bytes.
data5.txt, es directorio: False, size: 128 bytes.
sample_data, es directorio: True, size: 4096 bytes.
```

Guardar estructuras de **datos** <br>

Cuando queremos guardar objetos en python como diccionarios ó listas, utilizamos el módulo pickle y su metodo dump nos permite serializar objetos.
<br>
El siguiente código permite crear dos listas y un diccionario.
<br>

```python
import pickle

name = ['mohit', 'bhaskar', 'manish']
skill = ['Python', 'C++', 'Java']
dict1 = dic([(k,v) for k,v in zip(name, skill)])

with open("files/programming_powers.pkl", "wb") as p_file:
    pickle.dump(name, p_file)
    pickle.dump(skill, p_file)
    pickle.dump(dict1, p_file)
```

Con esto se crea un archivo que se lee en binario y no es leible para nosotros.<br>

Para cargar estas estructuras lo hacemos de forma simple

```python
import pickle

with open("files/programming_powers.pkl", "rb") as p_file:
    list1 = pickle.load(p_file)
    list2 = pickle.load(p_file)
    dict1 = pickle.load(p_file)

print(list1) #['mohit', 'bhaskar', 'manish']
print(list2) #['Python', 'C++', 'Java']
print(dict1) # {'mohit': 'Python', 'bhaskar': 'Pyhon', 'manish':'Java'}
```

Una imagen de tipo .jgp es un archivo de tipo binario: Con cierto procesamiento es posible crear una copia de la imagen de la siguiente manera:


```python
with open("files/discurso.jpg", "rb") as imagen:
    data = imagen.read()
with open("files/copy.jpg", "wb") as f:
    f.write(data)
```

**Problemas Sesion 18**
||LINK EJERCICIO||

## JSON
30 de junio 2021 <br>

Javascript Object Notation, intercambio de información entre aplicaciones. Se puede utilizar en diferentes lenguajes de programación. <br>

Es un diccionario donde cada item esta delimitado por comillas dobles " y el valor puede ser cualquier tipo de dato. <br>

**Ejemplo:**
```JSON
{
    "Nombre": "Ingrid",
    "Apellido": "E",
    "PasaTiempos": ["Pintar", "Programmar", "Cantar"],
    "Edad": 19,
    "Empleado": false,
    "Jefe": null,
    "Hijos": [
        {"Nombre": "Alice", "Edad":16},
        {"Nombre": "Bob", "Edad":8}
    ]
}
```

No todos los diccionarios de Python es un objeto JSON ya que en python las claves pueden ser numeros, cadenas, tuplas...etc. En JSON solo se permite cadenas de caracter delimitadas por comillas dobles. <br>

|Tipo en Python| Tipo en JSON|
|---|---|
|dict|object|
|tuple,list|array|
|str|string|
|int,float|number|
|False|false|
|True|true|
|None|null|

En python podemos importar el modulo de JSON con <br>
**import JSON** <br>

Los archivos de JSON se pueden serializar. En la libreria de JSON encontramos el metodo 
dump() que permite escribir datos en un archivo.<br>

Si tenemos:
```JSON
data = {
    "cientifico":{
        "nombre": "Alan Mathison Turing",
        "edad": "41"
    }
}
```
Se puede **serializar** en un archivo asi:
```python
with open("json/data_file.json", "w") as write_file:
    json.dump(data_write_file)
```

Se crea un archivo que contiene:<br>
{"cientifico": {"nombre": "Alan Mathison Turing", "edad": "41"}} <br>

Tambien se puede asignar a un string y nos devuelve lo mismo que contiene el archivo. <br>
*   json.dump(data, indent=n) : Podemos especificar la cantidad de espacios con n en indent
*   json.load(archivo) : Cargar JSONs desde archivos o desde strings si estan dentro de 3 comillas simples.
*   pprint : Imprimir de forma bonita

**Ejemplo**
```python
import json
from pprint import pprint
strjson = '''{
    "boolean1: null,
    "diccionario": {"papa":2000, "arroz": 5000},
    "intValue": 0,
    "myList": [],
    "myList2": ["info1", "info2"],
    "littleboolean": false,
    "myEmptyList": null,
    "text1": null,
    "text2": "hello",
    "value1":null,
    "value2:" null}
    '''
data = json.load(strjson)
pprint(data)
```

```
{
    "boolean1: null,
    "diccionario": {"papa":2000, "arroz": 5000},
    "intValue": 0,
    "myList": [],
    "myList2": ["info1", "info2"],
    "littleboolean": false,
    "myEmptyList": null,
    "text1": null,
    "text2": "hello",
    "value1":null,
    "value2:" null}
```

Para revisar un dato en especifico solo ponemos data["test2"] -> hello <br>
JSONPlaceholder para practicar peticiones. <br>

import requests para leer archivos JSON desde la web <br>
response = request.get(url) <br>
y con json.loads(response.text) se carga <br>

Para obtener registos del JSON: <br>
nombreJSON[:2] los dos primeros valores <br>

**Info de [w3schools](https://www.w3schools.com/python/python_json.asp)** <br>

JSON es una sintaxis para guardar e intercambiar datos. En python utilizamos la libreria **import json** para trabajar con datos de JSON.


## Librerias

Podemos importar una gran cantidad de librerias en Python que nos permiten realizar funciones de todo tipo

### **Numpy**

**import numpy as np** <br>

Se utiliza para computación científica en Python. Contiene arreglos en varias dimensiones, con herramientas para manipularlos.<br>

Metodos:
*   np.array(list) : Crea un array con "<class 'numpy.ndarry'>"
*   np.shape : Retorna el tamaño del array
*   np.zeros(tamaño): columna x fila o solo filas, de zeros tipo float
*   np.dtype : Retorna el tipo de los elementos dentro del array
*   np.sqrt(array): Aplica raiz cuadrada a cada elemento de la lista
*   np.add(array1, array2): Suma los valores de cada lista
*   np.linspace(start,stop, num, endpoint, retstep, stype, axis): Retorna numeros separados por espacios segun un intervalo especificado.
    *   start : Inicio de la secuencia
    *   stop: Final de la secuencia si endpoint es TRUE
    *   num: Cantidad para generar no puede ser negativo
    *   endpoint: Si finaliza o no
    *   retstep: Si es true retorna los pasos entre datos

Si creamos una variable con elementos de otro array a[0,1] los valores que cambien en esa variable se cambiaran tambien en el array general. <br>

Dos arrays se pueden sumar utilizando el operador + o **np.add(array1, array2)** si son del mismo tamaño. Tambien se puede hacer x("array") + 3 y se le sumara 3 a todos los valores de la lista.

```python
import numpy as np

lista = list(range(1,5)) #[1,2,3,4]
a = np.array(lista) # [1 2 3 4]
print(a.shape) # (4,)
print(a[0], a[1], a[2]) # 1 2 3

bidimensional = np.array([[1,2,3,4,5],[4,5,6,7,8]])
#Tienen que ser del mismo tamaño o da error
print(bidimensional)
# [[1 2 3 4 5]
# [4 5 6 7 8]]
print(bidimensional[0,0], bidimensional[1,0]) # 1 4

print("---------")
#Arreglo de diferente tipo

a = np.zeros((3,4)) #Devuelve una array de x tamaño lleno de 0
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]
print(a.shape) # (3,4)

a = np.zeros((2,3,4)) #Devuelve una array de x tamaño lleno de 0
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]]
print(a.shape) # (2,3,4)

print("---------")
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # Tamaño 3x4
b = a[:2, 1:3]
#[[2 3]
# [6 7]]
b[0,0] = -11
print(b,a, sep="\n")
#[[-11   3]
# [  6   7]]
#[[  1 -11   3   4]
# [  5   6   7   8]
# [  9  10  11  12]]
print("---------")

x = np.array([5,-4])
print(x.dtype) # int32
x = np.array([1.0,-2.0])
print(x.dtype) # float64
x = np.array([5,-4], dtype=np.float64)
print(x.dtype) # float64

print("---------")
x = np.array([[1,2,5],[3,4,6]], dtype=np.float64)
y = np.array([[5,6,-1],[7,8,-6]], dtype=np.float64)
print(np.add(x,y))
#Suma:
# [[ 6.  8.  4.]
# [10. 12.  0.]]
print(np.sqrt(x))
#[[1.         1.41421356 2.23606798]
# [1.73205081 2.         2.44948974]]
print("---------")

print(np.linspace(2,3,num=10, endpoint=True, retstep=False))
#[2.         2.11111111 2.22222222 2.33333333 2.44444444 2.55555556
# 2.66666667 2.77777778 2.88888889 3.        ]
print(np.linspace(2,3,num=10, endpoint=True, retstep=True))
#(array([2.        , 2.11111111, 2.22222222, 2.33333333, 2.44444444,
#       2.55555556, 2.66666667, 2.77777778, 2.88888889, 3.        ]), 0.1111111111111111)
```

### **Matplotlib**
**import matplotlib.pyplot as plt**<br>

Utilizada para crear visualizaciones estáticas o animadas en Python. Se puede graficar un área con uno o más ejes x,y o x,y,z. La forma mas facil de crear una figura con ejes es utilizar **pyploy** <br>

```python
plt.plot([1,2,3,4],[1,4,2,3]) # x,y
#plt.show() #Muestra la gráfica

x = np.linspace(0,2,50)
fig, ax = plt.subplots() #Crear la figura y ejes
ax.plot(x, x, label="linear") #Dibujando datos
ax.plot(x, x**2, label="quadratic")
ax.plot(x,x**3, label="cubic")
ax.set_xlabel("X") #Poner el nombre a el eje x
ax.set_ylabel("Y") #Poner el nombre a el eje y
ax.set_title("Figura de prueba\nIngrid-E") #Titulo a la figura
ax.legend() #Muesta los labels
#plt.show() #Muestra la gráfica
names = ["grupo_A", "grupo_B", "grupo_C"]
values = [3.4, 50.4, 23]

plt.subplot(131) #No entiendo que hace
plt.bar(names, values) #Grafica de barras
plt.subplot(132)
plt.scatter(names, values) # De puntos
plt.subplot(133)
plt.plot(names, values) #De lineas
plt.suptitle("Categorical Plotting")
plt.show()
```

## **Panda**
**import pandas as pd** <br>
Permite manipular datos de alto nivel, se utiliza para manipulación y análisis de datos.

```python
from typing import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

dictc = {"country": ["Brazil", "Russia", "India",
"China", "South Africa", "Colombia"],
"capital": ["Brasilia", "Moscow", "New Dehli",
"Beijing", "Pretoria", "Bogot ́a"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221, 1.142],
"population": [200.4, 143.5, 1252, 1357, 52.98, 49.65] }

brics = pd.DataFrame(dictc)
#        country    capital    area  population
#0        Brazil   Brasilia   8.516      200.40
#1        Russia     Moscow  17.100      143.50
#2         India  New Dehli   3.286     1252.00
#3         China    Beijing   9.597     1357.00
#4  South Africa   Pretoria   1.221       52.98
#5      Colombia   Bogot ́a   1.142       49.65

ventasPaises = pd.read_csv("SalesJan2009.csv")
ventasPaises.head(3)
#    Transaction_date   Product  Price  ...      Last_Login   Latitude   Longitude
# 0      1/2/2009 6:17  Product1   1200  ...   1/2/2009 6:08  51.500000   -1.116667
# 1      1/2/2009 4:53  Product1   1200  ...   1/2/2009 7:49  39.195000  -94.681940
# 2     1/2/2009 13:08  Product1   1200  ...  1/3/2009 12:32  46.188060 -123.830000
# 3     1/3/2009 14:44  Product1   1200  ...  1/3/2009 14:22 -36.133333  144.750000
# 4     1/4/2009 12:56  Product2   3600  ...  1/4/2009 12:45  33.520560  -86.802500
# ..               ...       ...    ...  ...             ...        ...         ...
# 992  1/22/2009 14:25  Product1   1200  ...   3/1/2009 3:37  54.583333   -5.933333
# 993   1/28/2009 5:36  Product2   3600  ...   3/1/2009 4:40 -20.360278   57.366111
# 994    1/1/2009 4:24  Product3   7500  ...   3/1/2009 7:21  42.946940  -76.429440
# 995   1/8/2009 11:55  Product1   1200  ...   3/1/2009 7:28  52.083333    0.433333
# 996  1/12/2009 21:30  Product1   1200  ...  3/1/2009 10:14  43.073060  -89.401110
#[997 rows x 12 columns]
cantidadPais = Counter(ventasPaises["Country"])
print(cantidadPais) # diccionario con la cantidad de veces que aparece
                    # un pais en el archivo
print(cantidadPais.most_common(3)) #[('United States', 462), ('United Kingdom', 100), ('Canada', 76)]

ventasPaises["Transaction_date"] = pd.to_datetime(ventasPaises["Transaction_date"])
A = (ventasPaises['Transaction_date']
        .dt.floor("d")
        .value_counts()
        .rename_axis("date")
        .reset_index(name="num ventas"))

G = A.plot(x="date", y="num ventas", color="green", title="Ventas por fecha")
plt.show()
```
## Funciones
8/07/2021 <br>

Existen dos tipos de funciones:
*   Incluidas en el lenguaje
*   Definidas por el usuario

Las funciones pueden tener o no argumentos y retornar o no valores


