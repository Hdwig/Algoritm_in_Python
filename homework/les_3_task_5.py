# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

ls = [random.randint(-100, 100) for i in range(50)]
k = -100
new_ls = [i for i in ls if i < 0]
for i in new_ls:
    if k < i:
        k = i
print(new_ls)
print(k)

