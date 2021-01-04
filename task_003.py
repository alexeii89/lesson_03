def my_func(a, b, c):
    array = [a, b, c]
    array = sorted(array, reverse=True)
    rezult = array[0] + array[1]
    return rezult


def my_func_v2(*args):
    my_array = list(args)
    z = max(my_array)
    my_array.remove(z)
    return z + max(my_array)


def my_func_v3(*args):
    my_array = list(args)
    my_array.remove(min(my_array))
    return sum(my_array)


print(my_func(int(input("1 число: ")),
              int(input("2 число: ")),
              int(input("3 число: "))))

print(my_func_v2(int(input("1 число: ")),
                 int(input("2 число: ")),
                 int(input("3 число: "))))

print(my_func_v3(int(input("1 число: ")),
                 int(input("2 число: ")),
                 int(input("3 число: "))))
