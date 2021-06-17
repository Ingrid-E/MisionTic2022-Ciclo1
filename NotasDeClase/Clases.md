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
```
dosElevado(5):
    prod = 1
    for i in range (1,5+1): **Repetir 5 veces**
        prod = 1 * 2 -> 2   **-1**
        prod = 2 * 2 -> 4   **-2**
        prod = 4 * 2 -> 8   **-3**
        prod = 8 * 2 -> 16  **-4**
        prod = 16 * 2 -> 32 **-5 STOP**
    return **prod**
```
Como prod = 35, entonces nos retorna **35**

