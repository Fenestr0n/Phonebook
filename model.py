def writing_txt(user):
    with open("Phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(f'Фамилия: {user[0]}\n\nИмя: {user[1]}\n\nТелефон: {user[2]}\n\nE-mail: {user[3]}\n\n\n')