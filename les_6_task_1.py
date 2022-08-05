import random
import sys
print(sys.version, sys.platform)
# 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] win32
# size = 480(all)


def pro(ls):
    print(ls)
    max1 = 0
    for i in ls:
        if i > max1:
            max1 = i
    min1 = max1
    for k in ls:
        if k < min1:
            min1 = k
        else:
            continue
    ind_min = ls.index(min1)
    ind_max = ls.index(max1)
    ls[ind_max], ls[ind_min] = ls[ind_min], ls[ind_max]
    print(ls)
    print("*" * 50)
    x = locals().values()
    y = 0
    for i in x:
        print(f"type = {i.__class__}, size = {sys.getsizeof(i)}, object = {i}")
        y += sys.getsizeof(i)
    print(y)


lss = [random.randint(0, 100) for i in range(30)]
pro(lss)
