"""
	Twitter: @g1_alexander
	Github: @g1alexander
"""

cadena = input()
cadena = cadena.split(" ")
newcadena = []
countList = []
count = 0

for n in range(len(cadena)):
    if cadena[n] not in newcadena:
        newcadena.append(cadena[n])
    elif cadena[n - 1] != cadena[n]:
        newcadena.append(cadena[n])

    if cadena[n - 1] == cadena[n]:
        count += 1
    else:
        if count != 0:
            countList.append(count)
            count = 1
        else:
            count += 1

    if (n == len(cadena) - 1):
        countList.append(count)

countList = [str(x) for x in countList]
print(f"""
{" ".join(newcadena)}
{" ".join(countList)}""")
