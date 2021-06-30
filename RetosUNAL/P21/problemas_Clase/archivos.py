'''
Dado el archivo de texto files/SalesJan2009.csv, procese el archivo
para obtener las compras realizadas en un país dado. Ejemplo:

Entrada: United Kingdom
Salida: 100
'''
import csv
salesJan2009 = []
with open('files/SalesJan2009.csv', 'r') as ventas:
    descripcion = ventas.readline().split(',')
    archivo = csv.reader(ventas)
    for datos in archivo:
        count = 0
        Dict = {}
        #print(datos[0])
        for i in datos:
            Dict[descripcion[count]] = i
            count += 1
        salesJan2009.append(Dict)

def contarCantidad(dato, tipo):
    cantidad = 0;
    for fila in salesJan2009:
        if fila[tipo] == dato:
            cantidad += 1
    return cantidad


print(contarCantidad('United Kingdom', 'Country'))
print(contarCantidad('Visa', 'Payment_Type'))
