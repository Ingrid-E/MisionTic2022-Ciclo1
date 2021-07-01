# Author: [Gabriel Morales](https://github.com/xgabrielmorales)

import json

lista_plaza = json.loads(input())
lista_ingre = input().replace(" ", "")

suma, ingre_dispo = int(), str()

for ingre in lista_ingre:
    if ingre in lista_plaza:
        suma += lista_plaza[ingre]
        ingre_dispo += f"{ingre} "

print(suma)
print(ingre_dispo)
