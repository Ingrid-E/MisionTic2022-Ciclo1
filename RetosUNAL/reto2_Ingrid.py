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
playerOne = input("Player 1: ").upper()
isString(playerOne)
playerTwo = input("Player 2: ").upper()
isString(playerTwo)
machine = input("Machine: ").upper()
isString(machine)

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

wordGame()

print(resultado)
