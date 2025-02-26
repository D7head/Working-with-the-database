import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

def add_user(name, email):
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    print(f"Пользователь {name} успешно добавлен.")

def view_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("Пользователи не найдены.")

def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print(f"Пользователь с ID {user_id} удален.")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить пользователя")
        print("2. Просмотреть пользователей")
        print("3. Удалить пользователя")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            name = input("Введите имя пользователя: ")
            email = input("Введите email пользователя: ")
            add_user(name, email)
        elif choice == '2':
            view_users()
        elif choice == '3':
            user_id = int(input("Введите ID пользователя для удаления: "))
            delete_user(user_id)
        elif choice == '4':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

conn.close()