import random
import sys
print(sys.version, sys.platform)
# 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] win32
# size = 476(all)


def pro(ls):
    x = 0
    y = ls[0]
    z = 0
    while z != len(ls):
        i = ls[z]
        z = z + 1
        if i > x:
            x = i
        elif i < y:
            y = i
        else:
            continue
    ind_min = ls.index(y)
    ind_max = ls.index(x)
    ls[ind_max], ls[ind_min] = ls[ind_min], ls[ind_max]
    print(ls)
    print(x)
    print(y)

    print("*" * 50)
    x = locals().values()
    y = 0
    for i in x:
        print(f"type = {i.__class__}, size = {sys.getsizeof(i)}, object = {i}")
        y += sys.getsizeof(i)
    print(y)


lss = [random.randint(0, 100) for i in range(30)]
print(lss)
pro(lss)
