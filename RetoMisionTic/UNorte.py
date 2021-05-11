# Selección de becas para minorías

#Recive variable de entrada y calcula un puntaje para selecionar
#nuevos becarios

#Salario mínimo 2021->  908.526

#El calculo se toma de la siguiente forma:
#Multiplicar cada variable por su peso correspondiente, sumarlos
#y dividirlo entre la suma del los pesos.

# ((x*p_1)+(y*p_2)+(z*p_3))/(p_1+p_2+p_3)

# puntaje < 0.5 no apto
# puntaje >= 0.5 es apto continua el proceso

# Variable de salida: El candidato continua en el proceso de seleccion
# o "El candidato no  continua en el proceso de seleccion"
#Cualquier valor no tabulado el programa sera "Se presento un error"

#Ejemplos:
#   afrodescendiente 1 400000 -> El candidato continua en el proceso de ..
#       [(0.2*2)+(1*3)+(1*5)]/(2+3+5)= (0.4+3+5)
#   gitano 4 4542630 -> El candidato no continua en el proceso de ....

candidato = input().split()
etnia = candidato[0]
estrato = candidato[1]
ingresos = candidato[2]

reconocimientoEtnico = {
    "sinReconocimiento": 0,
    "afrodescendiente": 0.2,
    "indigena": 0.4,
    "raizal": 0.6,
    "palenquero": 0.8,
    "gitano": 1
}

estratoSocioEconomico = {
    "1": 1,
    "2": 0.8,
    "3": 0.5,
    "4": 0.2,
    "5": 0,
    "6": 0
}

def ingresoNucleoFamiliar(ingresos):
    salarioMinimo = 908526
    ingreso = int(ingresos)
    if ingreso < salarioMinimo :
        return 1
    elif ingreso >= 1 | ingreso < (2*salarioMinimo):
        return 0.8
    elif ingreso >= (2*salarioMinimo) | ingreso < (4*salarioMinimo):
        return 0.6
    elif ingreso >= (4*salarioMinimo) | ingreso < (5*salarioMinimo):
        return 0.2
    elif ingreso >= (5*salarioMinimo):
        return 0

def puntajeCandidato():
    sumatoriaPesoVariables = (reconocimientoEtnico[etnia]*2)+((estratoSocioEconomico[estrato])*3)+(ingresoNucleoFamiliar(ingresos)*5)
    sumatoriaPeso = 2+3+5
    resultado = sumatoriaPesoVariables/sumatoriaPeso
    
    if resultado < 0.5 :
        print("El candidato no continua en el proceso de seleccion")
    elif resultado >= 0.5 :
        print("El candidato continua en el proceso de seleccion")

puntajeCandidato()



