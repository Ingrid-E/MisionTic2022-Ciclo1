# Author: [Gabriel Morales](https://github.com/xgabrielmorales)

def pedidos(tipos_pizzas_pedidas):
    restantes = list()
    [restantes.append(tipo) for tipo in tipos_pizzas_pedidas if tipo not in restantes]
    return restantes

def debo_llevar(cod_rep_dispo, tipo_pizza_reserv, tipo_pizz_llevar):
    rep_dispo = list()
    for codigo_rep in cod_rep_dispo:
        if tipo_pizza_reserv[codigo_rep] == tipo_pizz_llevar:
            rep_dispo.append(codigo_rep)
    return rep_dispo

def faltan_repartidores(cod_rep_total, cod_rep_ocup):
    return [rep for rep in cod_rep_total if rep not in cod_rep_ocup]

def posible_intercambio(cod_rep_dispo, cod_rep_aux):
    inter_1 = len([rep for rep in cod_rep_aux   if rep not in cod_rep_dispo])
    inter_2 = len([rep for rep in cod_rep_dispo if rep not in cod_rep_aux])
    return min(inter_1, inter_2)
