## RETO #2 - P30

### Descripción

El gobernante del país de Nuncalandia debe vacunar a la población de su
país, pero lamentablemente solo tiene vacunas para la mitad de ellos.
Mientras planeaba como hacerlo, vio en su biblioteca el juego de
Scrabble y se le ocurrió su propio juego para determinar a quién
vacunar. El juego consiste en lo siguiente:

1. Se eligen aleatoriamente dos personas `J` y `K` para competir en el
   juego.

2. El gobernante elige aleatoriamente un conjunto de letras del
   Scrabble.

3. Cada persona escoge diferentes letras del Scrabble con las cuales
   competirá en el juego.

4.  El juego consiste en `m` confrontaciones, que dependen de la
	cantidad de letras elegidas por el gobernante.

5. Para cada confrontación, se compara la letra del gobernante con las
   letras de las personas, y si la letra del gobernante es una de las
   escogidas por la persona, ella se lleva un punto. Al final de cada
   confrontación, el gobernante escribía en su libreta la persona que
   llevaba más puntos. Si la persona `J` llevaba más puntos escribía la
   letra “J”, si `K` llevaba más puntos escribía “K”, y si llevaban los
   mismos puntos escribía “L”.

6. Al final, la persona con más puntos es quien tiene acceso a la
   vacuna.

### Tarea

Elabora un programa que muestre, dadas las letras con las que juega la
persona `J`, las letras con las que juega la persona `K`, y las letras
del gobernante (como cadena de caracteres), una cadena de caracteres que
represente quien lleva más puntos al final de cada confrontación.

### Entrada

Tres cadenas de caracteres. La primera representa las letras escogidas
por la persona `J`, la segunda las letras escogidas por la persona `K`,
y la tercera el conjunto de letras escogidas por el gobernante.

### Salida

Una cadena de caracteres con los símbolos (`J`, `K`, `L`) que representa
los puntos al final de cada confrontación.
