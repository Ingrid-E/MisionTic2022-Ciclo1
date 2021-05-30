# Reto 1.Grupo P2: Profesor Juan Esteban Caicedo Palacio
# Límite de entrega: Wednesday, 2 de June de 2021, 12:00
# Número máximo de ficheros: 1
# Tipo de trabajo: Individual
# Juan, Pedro y Camila son estudiantes del colegio municipal “Mis Tapitas”. Al recibir las calificaciones de la asignatura de matemáticas, encontraron que su profesor les había puesto un acertijo para calcular la nota de cada uno.

# Para esto, el profesor definió las siguientes condiciones:

# Se conoce la calificación obtenida por Juan como número entero

# La calificación obtenida por Juan es igual, a la nota obtenida por Pedro menos cuatro, todo esto divido entre dos

# La nota de Pedro es igual a cinco veces la nota de Camila menos la nota obtenida por Juan

# Además, el profesor definió un escalafón de acuerdo a la calificación obtenida:

# Si obtiene una nota entre 0 y 20 se encontrará en el rango ‘uno’

# Si obtiene una nota entre 21 y 30 se encontrará en el rango ‘dos’

# Si obtiene una nota entre 31 y 50 se encontrará en el rango ‘tres’

# Si obtiene una nota mayor a 50 se encontrará en el rango ‘cuatro’.

# De esta manera, ellos acuden a usted como programador de Misión TIC 2022 para que les ayude a crear un programa en el cual puedan calcular fácilmente la nota y el rango en el que se encuentra la nota de Camila.



# Entrada:

# La entrada será la calificación obtenida por Juan.

# Salida:

# Tres enteros que representan las calificaciones de los tres estudiantes. Además, se debe imprimir en la siguiente línea el rango en la que se encuentra la nota de Camila.



# Entrada                           Salida

#32                                 32 68 20
#                                   uno

#29                                 29 62 18
#                                   dos


#Solución 

#La entrada es la calificación de Juan

print("== Entrada ==")
calificacion_juan = int(input())

#Con los datos del enunciado se llega a 
#calificacion_juan = (calificacion_pedro - 4)/2

calificacion_pedro = (calificacion_juan*2) + 4

#calificacion_pedro = 5*calificacion_camila - calificacion_juan

calificacion_camila = int((calificacion_pedro + calificacion_juan)/5)


#Salida 
print("== Salida ==")

print(f"{calificacion_juan} {calificacion_pedro} {calificacion_camila}")

def calcular_rango(nota):
    if(nota >= 0 and nota <= 20):
        print("uno")
    elif(nota <= 30):
        print("dos")
    elif(nota <= 50):
        print("tres")
    else:
        print("cuatro")

calcular_rango(calificacion_camila)