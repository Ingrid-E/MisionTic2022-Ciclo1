import json

productos: dict = json.loads(input())
requeridos = (input()).split()
encontrados = []
total = 0

for producto in requeridos:
    if producto in productos:
        total += productos[producto]
        encontrados.append(producto)

print(total)
print(' '.join(encontrados))
