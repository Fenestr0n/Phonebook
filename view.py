menu = '''Телефонный справочник:
1 - Просмотр
2 - Добавить
3 - Изменить
4 - Удалить
5 - Импорт
6 - Экспорт
7 - Выход
'''


def display_menu():
    while True:
        print(menu)    
        number = input(">>> ")
        if number.isdigit():
            if int(number) in (1, 2, 3, 4, 5, 6):
                return int(number)
            elif int(number) == 7:
                break


def get_view():
    with open("Phonebook.txt", 'r', encoding='utf-8') as file:
        print(file.read())
