"""
	Twitter: @g1_alexander
	Github: @g1alexander
"""
# variables -----
count_j = 0
count_k = 0
resultado = ""

# entradas -----
junior = input().upper()
kathe = input().upper()
pacientes = input().upper()


for letra in pacientes:
    for j in junior:
        for k in kathe:
            if j == letra and k == letra:
                pacientes = pacientes.replace(letra, "l")

for letra in pacientes:
    for j in junior:
        if j == letra:
            pacientes = pacientes.replace(letra, "j")

for letra in pacientes:
    for k in kathe:
        if k == letra:
            pacientes = pacientes.replace(letra, "k")

for letra in pacientes:
    if letra == "j":
        count_j += 1
    elif letra == "k":
        count_k += 1
    elif letra == "l":
        count_k += 1
        count_j += 1
    if count_j > count_k:
        resultado += "J"
    if count_j < count_k:
        resultado += "K"
    if count_j == count_k:
        resultado += "L"

print(resultado)
