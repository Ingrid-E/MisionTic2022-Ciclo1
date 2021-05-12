#Clasificación de nódulos tiroideos y acciones a tomar

#TI-RADS prueba de clasificación de nódulos tiroideos.
#Desarrollar un programa para la emisión de alertas tempranas
#segun la tablas.

#El programa debe leer las variables de cada caracteristica.
#Debe decir el nivel de sospecha y si requiere AAF

#Nota: para los focos ecogénicos utilice 4 variables y las 
#que no apliquen deben tener valor de 0 y las que apliquen 
#valor de 1. 

#Ejemplos: 
# C1 E1 F2 M3 0 1 0 0 2 -> Moderadamente sospechoso, AAF
# C1 E1 F1 M1 0 1 1 0 1 -> Levemente sospechoso, seguimiento
# C1 E1 F1 M1 1 0 0 0 2 -> Benigno, no AAF

variables = input().split()
composicion = variables[0]
ecogenicidad = variables[1]
forma = variables[2]
margen = variables[3]
focosE = [variables[4],variables[5],variables[6],variables[7]]
aaf = variables[8]

composiciones = {
    "C1": 0,
    "C2": 0,
    "C3": 0.5,
    "C4":1
}

ecogenicidades = {
    "E1": 0,
    "E2": 0.5,
    "E3": 1,
    "E4": 1.5
}

formas = {
    "F1": 0,
    "F2": 1.5
}

margenes = {
    "M1": 0,
    "M2": 0,
    "M3": 1,
    "M4": 1.5
}

focosErcogenicos = [0,0.5,1,1.5]

def sumatoriaFocos():
    sumatoria = 0
    for x in range (0,len(focosE)):
        if focosE[x] == "1":
            sumatoria = sumatoria + focosErcogenicos[x]
    return sumatoria

def clasificacion():
    
    puntaje = composiciones[composicion] + ecogenicidades[ecogenicidad] + formas[forma] + margenes[margen] + sumatoriaFocos()
    if puntaje == 0 and puntaje < 1:
        print("Benigno, no AAF")
    elif puntaje >= 1 and puntaje < 1.5:
        print("No sospechoso, no AAF")
    elif puntaje >= 1.5 and puntaje < 2:
        calificacionAAF("Levemente sospechoso")
    elif puntaje >= 2 and puntaje <= 3:
        calificacionAAF("Moderadamente sospechoso")
    elif puntaje > 3:
        calificacionAAF("Altamente sospechoso")

def calificacionAAF(tipo):

    if tipo == "Levemente sospechoso":
        if int(aaf) >= 2.5: print(tipo + ", AAF")
        elif int(aaf) <2.5: print(tipo + ", seguimiento")
    elif tipo == "Moderadamente sospechoso":
        if int(aaf) >= 1.5: print(tipo + ", AAF")
        elif int(aaf) < 1.5: print(tipo + ", seguimiento")
    elif tipo == "Altamente sospechoso":
        if int(aaf) >=1: print(tipo + ", AAF")
        elif int(aaf) < 1: print(tipo + ", seguimiento")

clasificacion()






