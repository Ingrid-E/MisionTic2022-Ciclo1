"""
	Twitter: @g1_alexander
	Github: @g1alexander
"""


def categorias(puntuacion):
    if puntuacion < 0:
        return "no puntuacion no puede ser menor a 0"
    if puntuacion >= 0 and puntuacion <= 20:
        return "uno"
    elif puntuacion > 20 and puntuacion <= 30:
        return "dos"
    elif puntuacion > 30 and puntuacion <= 50:
        return "tres"
    elif puntuacion > 50:
        return "cuatro"


intentos = int(input())
seg_puntuacion = intentos + intentos + 4
ter_puntuacion = (intentos + seg_puntuacion) // 5

if intentos < 0:
    print("no puedes tener '-' intentos")
else:
    print(
        f"""{intentos} {seg_puntuacion} {ter_puntuacion}
	{categorias(ter_puntuacion)}"""
    )
