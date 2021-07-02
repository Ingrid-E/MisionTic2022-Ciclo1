'''
Ingrid Echeverri Montoya
    *Github: @IngridE
    *Twitter: @Ingrid_E_

Contamos con x millones de pesos para invertir en 2 proyectos.
    1- Comprar un apartamento
        * 360 millones de pesos
        * Cada año su valor sube t1%
        * Prestamo de 120 cuotas mensuales con tasa de interés t2%
    2- Invertir todo en un proyecto
        * 120 meses retornan t3% del valor invertido.
        * 120 meses en arriendo por valor D
        * Cada año el arriendo sube t4%

    Teniendo:
        * 80 millones <= C <= 100 millones
        * 0.2 <= t1 <= 3.0
        * 3.5 <= t2 <= 6.5
        * 40 <= t3 <= 60
        * 1.0 <= t4 <= 3.0
        * 600 <= D <= 1500.000

Elaborar un programa que reporte si comprar vivienda o invertir en
el proyecto es más rentable.

    -> "Es más rentable invertir en vivienda con una diferencia de:
        $" + valor de ganancia (con dos decimales)
    -> "Es más rentable el proyecto, con una diferencia de:
        $" + valor de ganancia (con dos decimales)

El arriendo y sus incrementos se realizan anticipado y el préstamo mas
vencido al igual que la valoración del apartamento.


Entrada:
    Valor c
    Valor t1
    Valor t2
    Valor t3
    Valor t4
    Valor D

Salida:
    Es más rentable invertir en vivienda con una diferencia de: $500000.0
                                    o
    Es más rentable el proyecto, con una diferencia de: $500000.0

Ejemplos:
1-  Entrada:
        80000000
        0.2
        3.5
        40
        1.0
        600000
    Salida:
        Es más rentable el proyecto, con una diferencia de: $80136907.05

2-  Entrada:
        100000000
        3.0
        6.5
        60
        3.0
        1500000
    Salida:
        Es más rentable invertir en vivienda con una diferencia de: $80850950.00

Como obtener esa diferencia?

*   Ganancias Apartamento = Prestamo Total - Valor Apartamento Final
*   Ganancias Proyecto = Total Arriendo - Proyecto Final
*   Ganancias Apartamento - Ganancias Proyecto

Calcular Mensual Vigente = [(1+t2/100)^(30/360)]-1
Prestamo Mensual = Valor Pendiente
Interés Mensual = Prestamo Mensual * Mensual Vigente
Cuota Mensual = P_I*(MV*(1+MV^(120)))/((1+MV^(120))-1)
Valor Pendiente Mensual = Prestamo Mensual + Interés Mensual - Cuota Mensual
Valor Apartamento Anual = Valor Apt Anterior + ((Valor Apt Anterior * t1)/100)
Valor Arriendo Anual = ((Valor Arriendo Anterior * t4)/100)+t4
Proyecto al final = Valor Proyecto + ((Valor Proyecto * t3)/100)
'''

tests = [[80000000,0.2,3.5,40,1.0,600000],[100000000,3.0,6.5,60,3.0,1500000],[95000000,1.3,5,55,2,1268175.65]]

#Entradas:
dinero = float(input("C:")) #C
interes_apartamento = float(input("t1:")) #t1
interes_prestamo = float(input("t2:")) #t2
interes_proyecto = float(input("t3:")) #t3
interes_arriendo = float(input("t4:")) #t4
arriendo = float(input("D:")) #D

arriendo_total = 0.0

mensual_vigente = ((1+interes_prestamo/100)**(30/360))-1
valor_apartamento = 360000000
prestamo_Inicial = -dinero+ valor_apartamento
valor_pendiente = prestamo_Inicial
cuota_Total = 0

def prestamo_Mensual()->float:
    prestamo = valor_pendiente
    return prestamo

def interes_Mensual()-> float:
    interes = prestamo_Mensual() * mensual_vigente
    return interes

def cuota_Mensual()-> float:
    mensual = (mensual_vigente+1)**120
    cuota = prestamo_Inicial*(mensual_vigente*mensual)/(mensual-1)
    return cuota

def valor_Pendiente_Mensual()->None:
    global valor_pendiente
    valor_pendiente = prestamo_Mensual() +  interes_Mensual() - cuota_Mensual()

def valor_Apartamento_Anual()->None:
    global valor_apartamento
    valor_apartamento = valor_apartamento + ((valor_apartamento * interes_apartamento)/100)

def arriendo_Anual()->None:
    global arriendo, arriendo_total
    arriendo = arriendo+((arriendo*interes_arriendo)/100)

def valor_Proyecto()->float:
    proyecto = dinero + ((dinero * interes_proyecto)/100)
    return proyecto

def resultado():
    global arriendo_total
    for i in range(0,120+1):
        if i%12 == 0 and i!=0:
            arriendo_Anual()
            valor_Apartamento_Anual()
        arriendo_total += arriendo
        prestamo_Mensual()
        interes_Mensual()
        cuota_Mensual()
        valor_Pendiente_Mensual()

    cuota_Total = cuota_Mensual()*120+dinero
    ganancias_apartamento = valor_apartamento - cuota_Total
    ganancias_proyecto = valor_Proyecto()-arriendo_total

    if ganancias_apartamento > ganancias_proyecto:
        print("Es más rentable invertir en vivienda, con una diferencia de: $",round(ganancias_apartamento-ganancias_proyecto,2), sep='')
    elif ganancias_proyecto > ganancias_apartamento:
        print("Es más rentable el proyecto, con una diferencia de: $",round(ganancias_proyecto-ganancias_apartamento,2), sep='')
    else:
        print("Los dos proyectos son rentables")
resultado()

