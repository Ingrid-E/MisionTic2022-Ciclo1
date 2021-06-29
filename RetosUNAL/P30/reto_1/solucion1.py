# Author: [Gabriel Morales](https://github.com/xgabrielmorales)

IV = int(input())

f1 = lambda x    : round(x)
f2 = lambda x    : (2 * x) + 4
f3 = lambda x, y : (x + y) // 5

FR1 = f1(IV)
FR2 = f2(FR1)
FR3 = f3(FR1, FR2)

print(f"{FR1} {FR2} {FR3}")

if ( 0 <= FR3 <= 20): print("uno")
if (21 <= FR3 <= 30): print("dos")
if (31 <= FR3 <= 50): print("tres")
if (FR3 > 50):        print("Cuatro")
