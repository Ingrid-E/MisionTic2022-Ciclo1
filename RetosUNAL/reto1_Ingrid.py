# Reto 1: Grupo P21

# Planta de tratamiento de agua potable, adicionan cada dia 3 quimicos.
# Tanque B: Kilos de floculante
# Tanque C: Kilos de cal
# Tanque Salida: Litros de cloro

# KC - 4 = 2(KF)
# KC + KF = 5(LC)

# Dependiendo del dia de la semana, el consumo de agua varia.
# 4 categorías:
# uno : Cloro <= 20 litros
# dos : 20 < Cloro >= 30
# tres : 30 < Cloro >= 50
# cuatro : cloro > 50

# Entrada: Kilos de floculante
# Salida:
# - 3 números enteros, números de KF, KC, LC
# - Categoría del cloro

kilos_floculante = int(input())
kilos_cal = 2 * kilos_floculante + 4
litros_cloro = (kilos_cal + kilos_floculante) // 5


def categoria_cloro(cloro):
    if cloro <= 20:
        print("uno")
    elif cloro > 20 and cloro <= 30:
        print("dos")
    elif cloro > 30 and cloro <= 50:
        print("tres")
    else:
        print("cuatro")


print(kilos_floculante, kilos_cal, litros_cloro)
categoria_cloro(litros_cloro)
