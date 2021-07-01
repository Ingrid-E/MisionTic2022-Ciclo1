# Por estos días, se juega la Copa América de Fútebol en donde participan todos los países suramericanos. 

# Muchos coleccionistas y aficionados están completando el álbum de la Copa América de Futebol de Panini ¡El original!.

# Ellos cuentan con una lista con la inicial de los jugadores de las fichas faltantes y encontraron innumerables tiendas virtuales en internet en donde pueden comprarlas a un precio dado. Para esto ellos quisieran saber que láminas pueden comprar y el precio total por la compra.

# Para esto, le piden su ayuda para que realice un programa que dado un diccionario (en formato JSON) que tiene las parejas inicial_ficha:precio de todas las láminas vendidas por la tienda, y que dada la lista de iniciales de los jugadores faltantes (separados por espacios), imprima el precio total  de las fichas  que pueden comprar en esta tienda y las iniciales de las láminas compradas (separadas por espacio):

import json

#input
fichas = json.loads(input()) 
mis_fichas = str(input())

precio_total = 0
fichas_disponibles = []
for i in mis_fichas.split(" "):
    precio_ficha = fichas.get(i)
    if precio_ficha:
        precio_total += precio_ficha
        fichas_disponibles.append(i)

#output
print(precio_total)
print(' '.join(str(f) for f in fichas_disponibles))

