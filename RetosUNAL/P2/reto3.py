# Por estos días, se juega la Copa América de Fútbol en donde participan
# todos los países suramericanos. Entre ellos está la selección de Colombia
# y se quiere saber, cuántas veces se ha enfrentado a las diferentes selecciones
# en el torneo desde la primera edición. Para esto se utilizará la letra inicial
# del país, por ejemplo:

# Brasil

# Chile

# Brasil

# Venezuela

# Argentina

# Brasil

# Perú

# Perú

# Chile

# Así, para este ejemplo se pudo encontrar la siguiente secuencia, cada letra va
# separada por un espacio: B C B V A B P P C

# Como se sabe la Copa América de Fútbol, se ha realizado en innumerables ediciones,
# se desea saber cuántas veces ha enfrentado consecutivamente la selección de
# Colombia en las ediciones anteriores a otros equipos. Para esto, la Conmebol
# decidió contratarlo para que desarrolle este programa en el que recibirá como
# entrada la inicial de cada país separada por un espacio en blanco, y
# deberá imprimir dos líneas, la primera deberá ser la inicial de los países
# representados y en la segunda línea se debe imprimir el conteo de enfrentamientos
# entre Colombia y las demás selecciones (Todos van separados por espacios en blanco).

entrada_usuario = input()
entrada_lista = entrada_usuario.split(" ")

salida_letra = ""
salida_numero = ""

contador = 1

letra_actual = ""

# Para cada letra de la entrada
for i in range(len(entrada_lista)):

    if i == 0:
        #Si es 0 empezar con esa letra
        letra_actual = entrada_lista[0]
    elif entrada_lista[i] == letra_actual:
        #Si la letra actual es igual a la entrada
        contador += 1
        if i == len(entrada_lista) - 1:
            #Si es la ultima letra
            salida_letra += f"{letra_actual}"
            salida_numero += f"{contador}"

    else:
        #Si no es igual
        salida_letra += f"{letra_actual} "
        salida_numero += f"{contador} "

        contador = 1
        letra_actual = entrada_lista[i]

print(salida_letra)
print(salida_numero)