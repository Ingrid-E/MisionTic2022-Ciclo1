"""
	Twitter: @g1_alexander
	Github: @g1alexander
"""

import json

entrada1 = input()
entrada2 = input()


def jet(catalogo, laminas):
    laminas_count = 0
    laminas_jet = ""
    catalogo = json.loads(catalogo)
    laminas = laminas.split(" ")
    for lamina in laminas:
        if lamina in catalogo:
            laminas_jet += f"{lamina} "
            laminas_count += catalogo[lamina]
    print(f"""{laminas_count}
    {laminas_jet[:-1]}""")


jet(entrada1, entrada2)
