def int_func(string):
    my_array = list(string)
    for i in range(len(my_array)):
        if 122 >= ord(my_array[0]) >= 97:
            z = ord(my_array[0])
            my_array[0] = chr(z - 32)
        elif ord(my_array[i]) <= 90:
            z = ord(my_array[i])
            my_array[i] = chr(z + 32)
    return "".join(my_array)


strings = input("строка из слов, разделенных пробелом, из латинских букв: ").split(" ")

for i in range(len(strings)):
    strings[i] = int_func(strings[i])
print(" ".join(strings))
