# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

ls = [random.randint(0, 100) for i in range(30)]
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
