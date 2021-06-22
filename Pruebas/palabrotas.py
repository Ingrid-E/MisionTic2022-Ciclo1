palabrotas = []
i = 0

with open('listaPalabrotas.txt', mode = 'r') as lista_Palabrotas:
    for palabra in lista_Palabrotas.readlines():
        palabrotas.append(palabra.strip('\n').upper())
palabrotas = tuple(palabrotas)

def contienePalabrota(texto):
    comentario = texto.split(' ')
    palabrota = False
    for palabra in comentario:
        if palabra.upper() in palabrotas:
            palabrota = True
    if palabrota:
        print("Tu texto a sido censurado por contener una palabra ofensiva")
    else:
        print(texto)

contienePalabrota("Esto es una mierda")


