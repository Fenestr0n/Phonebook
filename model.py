import sqlite3


def writing_txt(user):
    with open("Phonebook.txt", "a", encoding="utf-8") as file:
        file.write(f'Фамилия: {user[0]}\n\nИмя: {user[1]}\n\nТелефон: {user[2]}\n\nE-mail: {user[3]}\n\n\n')


def writing_csv(user):
    with open("Phonebook.csv", "a", encoding="utf-8") as file:
        file.write(f'{user[0]};{user[1]};{user[2]};{user[3]}\n')


def writing_db(user):
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("INSERT INTO Phonebook VALUES(?, ?, ?, ?, ?);", user)
    conn.commit()


def reading_db():
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Phonebook;")
    all_results = cur.fetchall()
    for result in all_results:
        print(f'Фамилия: {result[1]}\n\nИмя: {result[2]}\n\nТелефон: {result[3]}\n\nE-mail: {result[4]}\n\n\n')