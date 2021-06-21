'''
Ingrid Echeverri Montoya
    *Github: @IngridE
    *Twitter: @Ingrid_E_

Reto 2: Ciclos
Resumen:
    Un casino quiere implementar un juego con 2 jugadores.
    Cada jugador escoge un conjunto de letras.
    La maquina escoge al azar un conjunto de letras.

    Por cada letra del jugador, que sale en la maquina, gana un punto.
    La maquina imprime con cada letra quien va ganando.
    P - Jugador 1
    S - Jugador 2
    E - Empate.

    Input:
        -Letras Jugador 1
        -Letras Jugador 2
        -Letras Maquina
    Output:
        -Resultado del juego

    Ejemplo:

    Input:
        Jugador 1 -> HBKM
        Jugador 2 -> MFZK
        Maquina -> EOBZYFYUFRRCHGO
    Output:
        -> EEPEESSSSSSSSSS

'''

def isString(string:str) -> None:
    '''
    Revisa si la cadena contiene solo letras del alfabeto y no contiene
    numeros, símbolos, etc.. Se llama recursivamente hasta que el input solo
    contenga letras.

    @param string: Cadena que se revisa
    '''
    containsNumbers = False
    for i in string:
        if not str(i).isalpha():
            containsNumbers = True
    if containsNumbers == True:
        print("Incorrect Input, use only letters!")
        string = input("->")
        isString(string)

#Llamada por consola de las variables
#playerOne = input("Player 1: ").upper()
#isString(playerOne)
#playerTwo = input("Player 2: ").upper()
#isString(playerTwo)
#machine = input("Machine: ").upper()
#isString(machine)

#Donde se guardara el puntaje y resultado final.
puntaje = [0, 0]
resultado = ""


def wordGame() -> None :
    '''
    Compara las palabras de los jugadores con la palabra de la maquina, calcula
    su puntaje y resultado. Utiliza 2 ciclos for para comparar cada letra de la maquina,
    con todas las letras de la palabra de los jugadores.
    '''
    for i in machine:
        for j in range(len(playerOne)):
            if i == playerOne[j]:
                puntaje[0] += 1
            if i == playerTwo[j]:
                puntaje[1] += 1
        if puntaje[0] == puntaje[1]:
            resultado += "E"
        elif puntaje[0] > puntaje[1]:
            resultado += "P"
        else:
            resultado += "S"

#wordGame()

#print(resultado)

'''
Ingrid Echeverri Montoya
    *Github: @IngridE
    *Twitter: @Ingrid_E_

Reto 2: Grupo P21
Resumen:
    Se va a elegir el consejo de administración, a partir de dos planchas, cada uno con
    n candidatos que se identifica con una letra única. Con cada voto el programa incrementa
    un contador.

    Entrada:
        - Serie de letras integrantes plancha 1
        - Serie de letras integrantes plancha 2
        - Serie de letras de los votos.

    Con cada letra de voto, se imprime quien va ganando.
        P = Plancha 1
        N = Plancha 2
        I = Empate

    Salida:
        -Letra de quien va ganando por cada voto.
'''

def isString(string:str) -> None:
    '''
    Revisa si la cadena contiene solo letras del alfabeto y no contiene
    numeros, símbolos, etc.. Se llama recursivamente hasta que el input solo
    contenga letras.

    @param string: Cadena que se revisa
    '''
    containsNumbers = False
    for i in string:
        if not str(i).isalpha():
            containsNumbers = True
    if containsNumbers == True:
        print("Input incorrecto, porfavor ingresa solo letras!")
        string = input("->")
        isString(string)

plancha1 = input("Plancha uno: ").upper()
isString(plancha1)
plancha2 = input("Plancha dos: ").upper()
isString(plancha2)
votos = input("Votos: ").upper()
isString(votos)

puntaje = [0,0]

PlanchaUno = "ADFBC"
PlanchaDos = "KLMNP"
Inicial = "AXDDMNMCSSDFMPBLNBPHRANB"





def resultadoVotacion() -> str :
    '''
        Revisar cada uno de los votos, y ver quien va ganando.
        @returns string: Resultado de quien iba ganando por cada voto.
    '''
    resultado = ""
    for i in votos:
        if plancha1.find(i) != -1 :
            puntaje[0] += 1
        if plancha2.find(i) != -1 :
            puntaje[1] += 1

        if puntaje[0] == puntaje[1]:
            resultado += "I"
        elif puntaje[0] > puntaje[1]:
            resultado += "P"
        else:
            resultado += "N"
    return resultado

print(resultadoVotacion())









votosUno = 1
votosDos = 1
salida=""

for i in Inicial: #Primer for
    for j in range(len(PlanchaUno)): #Segundo for
        if i == PlanchaUno[j]:
            votosUno += 1
        if i == PlanchaDos[j]:
            votosDos += 1
    if votosUno == votosDos:
        salida += "I"
    elif votosUno > votosDos:
        salida += "P"
    else:
        salida += "N"

print(salida)


