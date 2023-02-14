import sqlite3
from datetime import datetime


def logger(msg):
     with open("Phonebook.logg", "a", encoding="utf-8") as file:    # Django stuff: *.log in .gitignore
        file.write(f"{datetime.now()}: {msg}\n")


def writing_txt():
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Phonebook;")
    all_results = cur.fetchall()
    with open("Phonebook.txt", "w", encoding="utf-8") as file:
        for result in all_results:
            file.write(f'Фамилия: {result[1]}\n\nИмя: {result[2]}\n\nТелефон: {result[3]}\n\nE-mail: {result[4]}\n\n\n')
    cur.close()
    conn.close()
    logger("Экспорт в формат txt завершен")


def writing_csv():
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Phonebook;")
    all_results = cur.fetchall()
    with open("Phonebook.csv", "w", encoding="utf-8") as file:
        for result in all_results:
            file.write(f'{result[1]};{result[2]};{result[3]};{result[4]}\n')
    cur.close()
    conn.close()
    logger("Экспорт в формат csv завершен")


def writing_db(user):
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("INSERT INTO Phonebook VALUES(?, ?, ?, ?, ?);", user)
    conn.commit()
    cur.close()
    conn.close()
    logger(f"Добавлен новый контакт {user}")


def reading_db():
    conn = sqlite3.connect("Phonebook.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Phonebook;")
    all_results = cur.fetchall()
    for result in all_results:
        print(f'Фамилия: {result[1]}\n\nИмя: {result[2]}\n\nТелефон: {result[3]}\n\nE-mail: {result[4]}\n\n\n')
    cur.close()
    conn.close()
    logger("Просмотр справочника завершен")
        