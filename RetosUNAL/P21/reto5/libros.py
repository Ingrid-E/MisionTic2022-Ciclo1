def autores(listaAutores):
    sinRepetir = []
    for autor in listaAutores:
        if autor not in sinRepetir:
            sinRepetir.append(autor)
    return sinRepetir


def mefaltandeunautor(librosFaltantes, listaAutores, autor):
    librosAutor = []
    for libro in librosFaltantes:
        if listaAutores[libro] == autor:
            librosAutor.append(libro)
    return librosAutor

def losnecesito(librosIntercambio,misRepetidos):
    librosFaltantes = []
    for libro in librosIntercambio:
        if libro not in misRepetidos:
            librosFaltantes.append(libro)
    return librosFaltantes

def puedocambiar(susRepetidos, misRepetidos):

    interesan = [[],[]]
    for libro in susRepetidos:
        if libro not in misRepetidos:
            interesan[0].append(libro)
    for libro in misRepetidos:
        if libro not in susRepetidos:
            interesan[1].append(libro)
    print(interesan[0], interesan[1])
    if len(interesan[0]) > len(interesan[1]):
        return len(interesan[1])
    else:
        return len(interesan[0])

print(puedocambiar([6, 36, 37, 27, 14, 21, 23, 39, 26, 29, 9, 20, 8, 28, 25],[9, 3, 16, 35, 23, 21, 20, 8, 28, 34, 30, 11, 19, 2, 12, 31, 33, 24]))




