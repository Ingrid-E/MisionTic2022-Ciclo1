# Reto1

El gobierno de un país con el fin de incrementar las oportunidades laborales de la nación decidió ofrecer cursos de programación para todos. Dentro de uno de los cursos existe un profesor que quiere categorizar a sus estudiantes según su nivel académico para crear grupos de trabajo que tengan un mismo nivel. Para poder categorizarlos, les manda 2 ejercicios que deben resolver en la plataforma de programación de la clase (Replit); a partir del número total de intentos que cada estudiante tuvo a la hora de resolver los ejercicios, el profesor le dará a cada uno 3 puntuaciones le asignará su categoría.

La primera puntuación que le asigna es igual al número de intentos realizados, la segunda puntuación es el doble de la primera más un coeficiente de ayuda de 4 puntos, finalmente la tercera puntuación la obtiene a partir de sacar la quinta parte a la suma de los dos factores anteriores.

Para decirle a sus estudiantes en qué categoría quedó, el profesor se basa en la tercera puntuación obtenida. Si la puntuación está entre 0 y 20, el estudiante quedará en el grupo uno; entre 21 y 30, en el grupo dos; entre 31 y 50, en el grupo tres y en caso de que tenga más de 50 le asignará el grupo cuatro.

Realice un programa que permita al profesor obtener las puntuaciones y su grupo asociado a partir del número total de intentos de cada estudiante en la resolución de los ejercicios de clase.

Nota: En caso de obtener decimales en alguna puntuación tome como valor solo el entero correspondiente (función piso).

**Entrada:**
Número de intentos totales por estudiante.

**Salida:**
Las tres puntuaciones que el profesor requiere y el grupo al que asigna al estudiante.
**Ejemplo:**

| Entrada | Salida         |
| ------- | -------------- |
| 58      | 58 120 35 tres |
| 26      | 26 56 16 uno   |
