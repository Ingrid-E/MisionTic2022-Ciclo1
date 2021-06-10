"""
	Twitter: @g1_alexander
	Github: @g1alexander
"""


def validarValor(nombreValor, valor):
    if valor < 0:
        return print(f"tu {valor} del {nombreValor} no puede ser menor a 0")
    return True


nombre = input("ingresa nombre del producto: ")
cu = int(input("ingresa el costo unitario: "))
pvp = int(input("ingresa el precio de venta al publico: "))
uni_disp = int(input("ingresa las unidades disponibles: "))

producto = {"nombre": nombre, "cu": cu, "pvp": pvp, "uni_disp": uni_disp}
print("-----------")


validacion1 = validarValor("costo unitario", producto["cu"])
validacion2 = validarValor("precio de venta", producto["pvp"])
validacion3 = validarValor("unidades disponibles", producto["uni_disp"])

if validacion1 and validacion2 and validacion3:
    ganancias = (producto["pvp"] - producto["cu"]) * producto["uni_disp"]
    print(
        f"""Producto: {producto["nombre"]}
CU: ${producto["cu"]}
PVP: ${producto["pvp"]}
Unidades Disponibles: ${producto["uni_disp"]}
Ganancia: ${ganancias}"""
    )
else:
    print("ingresa valores positivos")
