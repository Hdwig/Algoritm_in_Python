a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a == b or b == c or c == a:
    print("Введены одинаковые числа")
elif a > b:
    if c > b:
        if a > c:
            print(c)
        else:
            print(a)
    else:
        print(b)
else:
    if c > a:
        if c > b:
            print(b)
        else:
            print(c)
    else:
        print(a)
