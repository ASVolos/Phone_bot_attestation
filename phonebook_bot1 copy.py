# добавление +, просмотр+,  импорт-, поиск+, удаление+, изменение данных-.
import sqlite3 as sq
from easygui import*

# con.close()]

# Открырываем созданный файл:
with sq.connect("phonebook.db") as con:
    cur = con.cursor()
    cur.execute("""
    """)

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    phone TEXT,
    address TEXT
)""")

# Взаимодействие с программой 'Справочник' через терминал VSc:
def interface():
    var = 0
    while var != '5':
        print(
                "Варианты взаимодействия:\n"
                "1. Добавить контакт\n"
                "2. Вывести телефонную книгу в терминале\n"
                "3. Поиск контакта по параметру\n"
                "4. Удалить контакт\n"
                "5. Выход\n"
                ) 
    
        var = input("Выберите вариант действия: ")
        while var not in ('1', '2', '3', '4', '5'):
            print("Некорректный код варианта взаимодействия")
            var = input("Выберите вариант действия: ")
        print()

        match var:
            case '1':
                add_contact()
            case '2':
                show_all_phonebook()
            case '3':
                seach_contact()
            case '4':
                delete_contact()
            case '5':
                print("До свидания")
        print()

cur.execute("SELECT * FROM phonebook;")
contacts = cur.fetchall()

# Вывод телефонного справочника в терминал:
def show_all_phonebook():
    cur.execute("SELECT * FROM phonebook;")
    contacts = cur.fetchall()
    for contact in contacts:
        print(*contact)

# Дообавление контакта в справочник:
def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес(город): ")
    cur.execute("""INSERT INTO phonebook VALUES (?, ?, ?, ?, ?)""", (surname, name, patronymic, phone, address))
    con.commit()
    print()
    print("Контакт успешно добавлен!")

# Поиск контакта:
def seach_contact():
    cur.execute("SELECT * FROM phonebook;")
    contacts = cur.fetchall()
    search = input("Введите данные для поиска: ").title()
    name_yes = 0
    for contact in contacts:
        if search in contact:
                print(*contact)
                name_yes += 1
    if name_yes == 0:
        print(f'Данного контакта "{search}" нет в справочнике')
    print()

# Удаление контакта:
def delete_contact():
    cur.execute("SELECT * FROM phonebook;")
    contacts = cur.fetchall()
    search = input("Введите данные контакта, который желаете удалить: ").title()
    name_for_del = None
    for contact in contacts:
        if search in contact:
            name_for_del = contact[0]
    if name_for_del is not None:
        cur.execute("DELETE FROM phonebook WHERE surname = ?", (name_for_del,))
        print(f"Контакт {contact} успешно удален.")
        con.commit()
    else:
        print("Контакт не найден.")


if __name__ == "__main__":
    interface()
