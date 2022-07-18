# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

ls = [random.randint(-100, 100) for i in range(30)]
x = 0
while x != 2:
    num = ls[0]
    for i in ls:
        if num > i:
            num = i
    print(f"наименьшее число под номером {x}: {num}")
    ls.pop(ls.index(num))
    x += 1
