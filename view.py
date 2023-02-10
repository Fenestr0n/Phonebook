menu = '''Телефонный справочник:
1 - Просмотр
2 - Добавить
3 - Экспорт
4 - Выход
'''


def display_menu():
    while True:
        print(menu)    
        number = input(">>> ")
        if number.isdigit():
            if int(number) in (1, 2, 3, 4):
                return int(number)


def get_view():
    with open("Phonebook.txt", 'r', encoding='utf-8') as file:
        print(file.read())


def add_user():
    user = []
    last_name = input("Введите фамилию: ")
    user.append(last_name)
    first_name = input("Введите имя: ")
    user.append(first_name)
    phone_number = input("Введите номер телефона: ")
    user.append(phone_number)
    email = input("Введите E-mail: ")
    user.append(email)
    return user



