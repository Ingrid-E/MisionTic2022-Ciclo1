'''
Ingrid Echeverri
Github: @Ingrid-E
Twitter: @Ingrid_E_

Reto 3 P21 UNAL
'''

#modelos_vendidos = input('Modelos Vendidos:').split(' ')
'''
Función que cuenta cada cuanto se repite un numero en secuencia
'''
def conteoModelos(modelos):
    #Lista que contiene los numeros sin repetirse en secuencia
    #y la cantidad de veces que se repite en secuencia
    secuenciaModelos = [[],[]]
    cantidadEnSecuencia = 0; #Contador de repetición
    for modelo in range(len(modelos)):
        cantidadEnSecuencia += 1;
        if modelo == len(modelos)-1 or modelos[modelo] != modelos[modelo+1] :
            secuenciaModelos[0].append(modelos[modelo]) #Valor
            secuenciaModelos[1].append(cantidadEnSecuencia) #Cantidad de veces que se repite
            cantidadEnSecuencia = 0 #Reiniciar suma

    print(" ".join(x for x in secuenciaModelos[0]))
    print(" ".join(str(x) for x in secuenciaModelos[1]))

#conteoModelos(modelos_vendidos)
