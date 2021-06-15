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