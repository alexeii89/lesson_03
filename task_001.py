number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))


def rezult(a, b):
    return a / b


try:
    print(rezult(number_one, number_two))
except ZeroDivisionError:
    print("На ноль делить нельзя")
