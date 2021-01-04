def my_func(x, y):
    y = y * -1
    i = 0
    rez = 1
    while i < y:
        rez = rez * x
        i += 1
    return 1 / rez


def my_func_v2(x, y):
    return x ** y


x = int(input("Введите натуральное положительное число x: "))

while x <= 0 and x != type(int):
    if x == 0:
        print("основание отрицательной степени не должно ровняться 0")
        x = int(input("Введите натуральное положительное число x: "))
    else:
        print("Ошибка!")
    x = int(input("Введите натуральное положительное число x: "))

y = int(input("Введите целое отрицательное число y: "))

while y > 0 and y != type(int):
    print("Ошибка!")
    y = int(input("Введите натуральное отрицательное число y: "))

print(round(my_func(x, y), 5))
