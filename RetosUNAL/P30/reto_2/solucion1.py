# Author: [Gabriel Morales](https://github.com/xgabrielmorales)

J, K = input(), input()
letters = input()

J_points, K_points = int(), int()

for letter in letters:
    J_points += 1 if letter in J else 0
    K_points += 1 if letter in K else 0

    # Tricotomía
    if J_points < K_points:  print("K", end="")
    if J_points == K_points: print("L", end="")
    if J_points > K_points:  print("J", end="")
