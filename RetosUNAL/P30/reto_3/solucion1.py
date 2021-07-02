# Author: [Gabriel Morales](https://github.com/xgabrielmorales)

register = input().replace(" ", "")
reporte, num_reporte = str(), str()
contador = -1

def crear_reporte(cliente, num_ingresos):
    global reporte, num_reporte
    reporte     += f"{cliente} "
    num_reporte += f"{num_ingresos} "

for index in range(len(register)):
    if index == len(register) - 1:
        crear_reporte(register[index], index - contador)
        break
    if register[index] != register[index + 1]:
        crear_reporte(register[index], index - contador)
        contador = index

print(reporte)
print(num_reporte)
