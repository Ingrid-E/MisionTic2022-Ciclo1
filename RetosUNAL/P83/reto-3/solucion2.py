"""
	Twitter: @blasanti258
	Github: @santigp258
"""

CADENA = input("ingrese una cadena\n").replace(" ", "")
cad = ""
count_cad = ""
count = 0
for index in range(len(CADENA)):
    if (CADENA[index] not in cad):
        cad = cad + " " + CADENA[index]
    elif (CADENA[index - 1] != CADENA[index]):
        cad = cad + " " + CADENA[index]
    if (CADENA[index - 1] == CADENA[index]):
        count += 1
    else:
        if (count != 0):
            count_cad = count_cad + " " + str(count)
        count = 1
    if (index + 1 == len(CADENA)):
        count_cad = count_cad + " " + str(count)

print(f"{cad}\n{count_cad}")