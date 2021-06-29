"""
	Twitter: @blasanti258
	Github: @santigp258
"""
JUNIOR = input("Junior \n")
KATERINE = input("Katerine \n")
CUENTA = input("Apellidos \n")

count_JUN = 0
count_KAT = 0
final_string = ""

for i in CUENTA:
    if i in JUNIOR:
        count_JUN = count_JUN + 1
    if i in KATERINE:
        count_KAT = count_KAT + 1
    if (count_JUN > count_KAT):
        final_string = final_string + "J"
    elif (count_KAT > count_JUN):
        final_string = final_string + "K"
    else:
        final_string = final_string + "L"

print(final_string)