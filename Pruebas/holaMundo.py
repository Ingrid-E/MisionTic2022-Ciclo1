'''
Casino, desea implementar un nuevo juego con dos jugadores.
Cada jugador debe escoger al azar un conjunto de letras.
Esperar -> una maquina muestre aleatoriamente una letra en mayúscula.
Si la letra que se mostró es una de las letras del jugador,
entonces se le suma un punto.

Para llevar bien las cuentas:
    La maquina cada vez que muestra una letra, muestra en una
    tririlla una letra dependiendo de quien va ganando.

Dependiendo de quien va ganando:
Jugador1 -> P
Jugador2 -> S
Empate -> E

Entrada:
1- Letras Jugador 1
2- Letras Jugador 2
3- Letras que mostraría la maquina

Salida: Cadena del resultado final.

Ejemplo 1:
P- HBKM
S- MFZK

EOBZYFYUFRRCHGO

EEPEESSSSSSSSSS


'''


jugador1=input("Jugador 1: ")
jugador2=input("Jugador 2: ")
cadenamaquina=input("Máquina: ")
suma1=0
suma2=0
for i in cadenamaquina:
  if i in jugador1:
    suma1 += 1
  if i in jugador2:
    suma2 += 1
  if suma1>suma2:
    print("P",end="")
  elif suma1<suma2:
    print("S",end="")
  elif suma1==suma2:
    print("E",end="")

playerOne = input("Player 1: ")
playerTwo = input("Player 2: ")
machine = input("Machine: ")

for i in machine:
    if jugador[i] == machine

