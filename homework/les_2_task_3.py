# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

def reverse(num):
    result = ""
    if num > 9:
        while num != 0:
            result = f"{result}{num % 10}"
            num //= 10
    else:
        return num
    return result


num = int(input("Введите любое положительное целое число: "))
print(reverse(num))
