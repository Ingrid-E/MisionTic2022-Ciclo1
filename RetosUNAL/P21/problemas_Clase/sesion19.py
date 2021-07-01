import json
from os import sep

'''Archivo JSON'''
with open('files/EstructuraJSON.Json', 'r', encoding='utf-8') as archivo:
    estructuraJSON = json.load(archivo)

'''
Imprima los nombres completos (nombre y apellidos) de las personas
que practican el deporte ingresado por el usuario.
'''
def practicanDeporte(deporte):
    personas = []
    for persona in estructuraJSON:
        if deporte.title() in estructuraJSON[persona]['deportes']:
            personas.append(persona)
    return personas

#deporte = input('Deporte: ')
#print(*practicanDeporte(deporte), sep="\n")

'''
Imprima los nombres completos (nombre y apellidos) de las personas
que est ́en en un rango de edades dado por el usuario.
'''
def rangoDeEdades(rango):
    personas = []
    for persona in estructuraJSON:
        edad = estructuraJSON[persona]['edad']
        if edad >= int(rango[0]) and edad <= int(rango[1]):
            personas.append(persona)
    return personas

#rangoEdad = input("Rango de edad, escribirlo como: 0 10\n").split()
#print(*rangoDeEdades(rangoEdad))
'''
Cree un JSON de deportes como sigue:
    {
        "Ajedrez": ["jadiazcoronado",...,"dmlunasol"],
        "Futbol": ["jadiazcoronado",...],
        "Gimnasia": ["jadiazcoronado",...,"dmlunasol"],
        ....
        "Baloncesto": ["dmlunasol"...],
    }
'''
def deportePersona():
    deportes = {}
    for persona in estructuraJSON:
        personas = []
        deporte = estructuraJSON[persona]['deportes']
        for x in deporte:
            if x not in deportes.keys():
                deportes[x] = []
            deportes[x].append(persona)
    with open('files/newJSON.Json', 'w', encoding="utf-8") as newArchive:
        json.dump(deportes, newArchive, indent= 4)

#deportePersona()
'''
Desarrolle un programa que lea dos archivos JSON, y encuentre los
componentes clave:valor que son iguales en ambos. Genere un nuevo
archivo JSON con las coincidencias exactas entre los dos archivos.
'''

def valoresIguales(archivo1, archivo2):
    with open(archivo1, 'r', encoding="utf-8") as a, open(archivo2, 'r',encoding="utf-8") as b:
        file1 = json.load(a)
        file2 = json.load(b)

    return checkDict(file1, file2)

def checkDict(dic1, dic2):
    claves1 = list(dic1.keys());valores1 = list(dic1.values())
    claves2 = list(dic2.keys());valores2 = list(dic2.values())
    valoresIguales = {}
    for x in range(len(claves1)):
        clave = claves1[x]
        if clave in claves2:
            y = claves2.index(clave)
            if isinstance(valores1[x], dict) and checkDict(valores1[x],valores2[y]) != 0:
                valoresIguales[clave] = checkDict(valores1[x],valores2[y])
            if isinstance(valores1[x], list):
                valoresIguales[clave] = checkList(valores1[x],valores2[y])
            elif valores1[x] == valores2[y]:
                valoresIguales[clave] = valores1[x]
    if len(valoresIguales) == 0:
        return 0
    return valoresIguales


def checkList(list1, list2):
    iguales = []
    for valor in list1:
        if valor in list2:
            iguales.append(valor)
    return iguales


#print(valoresIguales('files/persona1.Json', 'files/persona2.Json'))

'''
Desarrolle un programa que lea un archivo JSON, en el cual se
encuentran las notas de los estudiantes del curso. Cada llave
corresponde al código de cada estudiante, y su valor es una lista con
las notas obtenidas en las actividades del curso. Se debe generar un
nuevo archivo JSON que para uno de los estudiantes solo guarde el
promedio de las notas obtenidas.
'''
def promedioNotas(archivo):
    with open(archivo, 'r', encoding="utf-8") as file:
        notasEstudiantes = json.load(file)

    promedio = {}
    for estudiante in notasEstudiantes:
        sumaNotas = 0
        cantidad = len(notasEstudiantes.get(estudiante))
        for notas in notasEstudiantes.get(estudiante):
            sumaNotas += notas
        promedio[estudiante] = sumaNotas/cantidad
    return promedio

#print(promedioNotas('files/notas.Json'))
'''
Desarrollar un programa que lea un archivo JSON que contiene una
serie de cadenas de caracteres en minúscula, cada una con su propia
llave. Estas llaves tienen una codificación, a forma de encriptación, en
donde las vocales est ́an descritas como otros símbolos: $ en vez de a,
# en vez de e, * en vez de i, ¬ en vez de o, y + en vez de u. Una vez
le ́ıdo el archivo, realice una desecriptación de todas las cadenas, es
decir, convierta los símbolos a sus vocales correspondientes (si la
cadena de entrada es ”h¬l$”, la cadena resultante ser ́ıa ”hola”), y
guarde el resultado en un nuevo archivo JSON.
'''
#Sin terminar aun
def encriptacion():
    codificacion = json.dumps({'$':'a', '#':'e', '*':'i', '¬':'o', '+':'u'})
    encriptacion = {'n¬mbr#':['s$r$', 'm$r*n'],'#st+d*¬s':['s*c¬l¬g*$','n+tr*c*¬n'],'#mpr#s$s':['h¬sp*t$l','cl*n*c$'],'c+mpl#$ñ¬s':['#n#r¬','01']}

    for clave in encriptacion:
        for valor in encriptacion.get(clave):
            for letra in valor:
                nombre = ''
                if letra in codificacion:
                    nuevaLetra = codificacion.get(letra)
                    nombre += nuevaLetra
            print(valor)
encriptacion()