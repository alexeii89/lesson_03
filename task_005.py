def my_func(arr):
    global rez
    try:
        arr = arr.split(" ")
        z = arr.index("q")
        arr = arr[:z]
        my_arr = list(map(int, arr))
        rez = rez + sum(my_arr)
        return rez, False
    except ValueError:
        my_arr = list(map(int, arr))
        rez = rez + sum(my_arr)
        return rez, True

rez = 0
while True:
    flag = True
    arr = input("введите строку чисел, разделенных пробелом: ")
    rez, flag = my_func(arr)
    if flag == False:
        print(rez)
        break
    else:
        print(rez)



