"""
	Twitter: @blasanti258
	Github: @santigp258
"""
import math

def validacion(puntos):
    try:
        int(puntos)
        return True
    except:
        return False


def categoria(puntuacion):
    if 0 <= puntuacion <= 20:
        return "uno"
    elif 21 <= puntuacion <= 30:
        return "dos"
    elif 31 <= puntuacion <= 50:
      return "tres"
    else:
      return "cuatro"

puntuacion = input("Puntuación\n")

check = validacion(puntuacion)
while (check == False):
    puntuacion = input("Ingrese un valor entero \n")
    check = validacion(puntuacion)

#puntuacion
primera = int(puntuacion)
segunda = (primera * 2) + 4
tercera = math.floor((primera + segunda) / 5)

cat = categoria(tercera)
print(f"{primera} {segunda} {tercera} {cat}")