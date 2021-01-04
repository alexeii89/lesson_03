def information_user(**kwargs):
    return kwargs


print(information_user(name=input("Введите имя: "),
                       lastname=input("Введите фамилию: "),
                       year=input("год рождения: "),
                       city=input("введите город проживания: "),
                       email=input("Введите email: "),
                       phone=input("Ввдедите телефон: ")))
