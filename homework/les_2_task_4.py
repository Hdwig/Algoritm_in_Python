# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

def summ(n):
    if n == 1:
        num = n
    else:
        num = 1
        result = num
        while n > 1:
            num = num / -2
            result += num
            n -= 1
    return result


n = int(input("Введите количетво элементов для суммирования: "))
print(summ(n))
