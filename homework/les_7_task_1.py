import random


def unshuffle(mass):
    mn = 0
    for i in range(len(mass) - 1):
        mn += 1
        for j in range(len(mass) - mn):
            if mass[j] > mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]
    return mass


mass = [i for i in range(-5, 5)]
random.shuffle(mass)
print(mass)
print(unshuffle(mass))
