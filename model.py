import sqlite3


def writing_txt():
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Phonebook;")
    all_results = cur.fetchall()
    with open("Phonebook.txt", "w", encoding="utf-8") as file:
        for result in all_results:
            file.write(f'Фамилия: {result[1]}\n\nИмя: {result[2]}\n\nТелефон: {result[3]}\n\nE-mail: {result[4]}\n\n\n')


def writing_csv(user):
    with open("Phonebook.csv", "w", encoding="utf-8") as file:
        file.write(f'{user[1]};{user[2]};{user[3]};{user[4]}\n')


def writing_db(user):
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("INSERT INTO Phonebook VALUES(?, ?, ?, ?, ?);", user)
    conn.commit()
    cur.close()
    conn.close()


def reading_db():
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Phonebook;")
    all_results = cur.fetchall()
    for result in all_results:
        print(f'Фамилия: {result[1]}\n\nИмя: {result[2]}\n\nТелефон: {result[3]}\n\nE-mail: {result[4]}\n\n\n')
    cur.close()
    conn.close()
    