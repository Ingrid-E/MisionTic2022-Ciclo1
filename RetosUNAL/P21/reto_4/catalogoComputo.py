'''
Ingrid Echeverri
Github: @Ingrid-E
Twitter: @Ingrid_E_

Reto 4 P21 UNAL
'''
import json

proveedor = json.loads(input('Proveedor: '))
equiposSolicitados = input('Equipos: ').split(' ')

def valorEquipos(productos, compras) -> None:
    '''
    Imprime el valor total de los precios de los productos requeridos en
    la lista de productos y los productos disponibles para comprar.

    @productos -> dict con los productos y precios
    @compras -> lista con los productos que se quieren comprar.
    '''
    valorTotal = 0;
    disponibles = []
    for producto in compras:
        if producto in productos:
            valorTotal += productos.get(producto)
            disponibles.append(producto)
    print(valorTotal)
    print(*disponibles)

valorEquipos(proveedor, equiposSolicitados)

