"""
	Twitter: @blasanti258
	Github: @santigp258
"""
import json

entrada1 = input()
entrada2 = input()


def calculate(catalogo, fichas):
    fichas = fichas.split(" ")
    catalogo= json.loads(catalogo)
    total = 0
    fichas_pend = []
    for x in fichas:
      if x in catalogo:
        fichas_pend.append(x) 
        total += catalogo[x]
    print(f"{total}\n {' '.join(str(e) for e in fichas_pend)}")


calculate(entrada1, entrada2)