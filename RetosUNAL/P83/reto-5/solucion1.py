def filtrar_laminas(laminas):
    filtro_laminas = []
    for n in range(len(laminas)):
        if laminas[n] not in filtro_laminas:
            filtro_laminas.append(laminas[n])
    return filtro_laminas


def validar_tipo(indices, laminas, tipo):
    validar_tipo = []
    for i in indices:
        if laminas[i] == tipo:
            validar_tipo.append(i)
    return validar_tipo


def listar_faltantes(lista_usuario, lista_intercambiables):
    listar_faltantes = []
    for n in range(len(lista_usuario)):
        if lista_usuario[n] not in lista_intercambiables:
            listar_faltantes.append(lista_usuario[n])
    return listar_faltantes


def numero_intercambiables(lista_usuario, lista_intercambiables):
    return len(listar_faltantes(lista_intercambiables, lista_usuario))
