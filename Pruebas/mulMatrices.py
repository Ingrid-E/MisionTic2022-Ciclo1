'''
Multiplicación de dos matrices.

Para multiplicar las matrices con tamaño columnas*filas:
-Las filas de la primera matriz deben ser igual a las columnas de la segunda matriz,
 si no, la multiplicación no es valida.

La multiplicación de una matriz es:
    Elementos_Columna * Elementos_Fila
    (b_00) * (a_00, a_01, a_02) = (a_00*b_00)+(a_01*b_00)+(a_02*b_00)
'''

def multiplicarMatrices(A,B):
    resultado = []
    #Tamaño de la matriz A
    filasA = len(A); columnasA = len(A[0])
    #Tamaño de la matriz B
    filasB = len(B); columnasB = len(B[0])

    if columnasA == filasB: #Condición para saber si son multiplicables.
        for fila in range(filasA): #Recorre cada fila de la matriz A
            nuevaFila = []
            for columna in range(columnasB): #Recorre cada columna de la matriz B
                sumElm = 0;
                for elemento in range(columnasA):  #Recorre cada elemento de fila A, y columna B
                    sumElm += A[fila][elemento] * B[elemento][columna]
                nuevaFila.append(sumElm)
            resultado.append(nuevaFila)
    else:
        print('Error: La filas de la matriz A no son iguales a las columnas de la matriz B')

    return resultado

matrizA = [
            [12, 7, 3],
            [ 4, 5, 6],
            [ 7, 8, 9]
          ]

matrizB = [
            [ 5, 8, 1, 2],
            [ 6, 7, 3, 0],
            [ 4, 5, 9, 1]
          ]

print(multiplicarMatrices(matrizA, matrizB))


A = [[12, 7, 3],
    [4 ,5, 6],
    [7,8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]



    