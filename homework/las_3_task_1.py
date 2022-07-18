# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

for k in range(2, 10):
    list_simple = []
    for i in range(2, 100):
        if i % k == 0:
            list_simple.append(i)
        else:
            continue
    print(f"список чисел кратных '{k}': {list_simple}")
