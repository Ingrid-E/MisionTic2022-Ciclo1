# Antonio Gonzalez Restrepo - github.com/antorpo/

cadena = (input()).split()
resultados = []
cuenta = 0

for i in range(len(cadena)):

    if i == 0: 
        resultados.append([cadena[i], 1])
    elif resultados[cuenta][0] == cadena[i]:
        resultados[cuenta][1] += 1
    else:
        resultados.append([cadena[i], 1])
        cuenta += 1

simbolos = ' '.join(x[0] for x in resultados)
frecuencia = ' '.join(str(x[1]) for x in resultados)

print(simbolos)
print(frecuencia)