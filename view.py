from random import randint

menu = '''Телефонный справочник:
1 - Просмотр
2 - Добавить
3 - Экспорт в txt
4 - Экспорт в csv
5 - Выход
'''


def display_menu():
    while True:
        print(menu)    
        number = input(">>> ")
        if number.isdigit():
            if int(number) in (1, 2, 3, 4, 5):
                return int(number)



def add_user():
    user = []
    user_id = randint(10, 10000)
    user.append(user_id)
    last_name = input("Введите фамилию: ")
    user.append(last_name)
    first_name = input("Введите имя: ")
    user.append(first_name)
    phone_number = input("Введите номер телефона: ")
    user.append(phone_number)
    email = input("Введите E-mail: ")
    user.append(email)
    print()
    return user

def export():
    print("Экспорт спрвочника завершен\n")