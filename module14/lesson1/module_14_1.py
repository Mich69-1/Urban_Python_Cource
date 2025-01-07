# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER,
               balance INTEGER NOT NULL
               )
               ''')

# Добавляем в базу десять записей с username типа User1, User2 ... и т.д.
for i in range(1, 11):
    cursor.execute(f'''
                   INSERT INTO users (username, email, age, balance)
                   VALUES ('User{i}', 'example{i}@mail.ru', {i * 10}, 1000)
                   ''')

# Меняем balance у записей, через одну на 500 (начиная с первой!)
cursor.execute('UPDATE users SET balance = 500 WHERE id % 2 = 1')

# Удаляем первую запись и, далее, через две от нее - 4,7 ..
cursor.execute('DELETE FROM users WHERE id = 1')
cursor.execute('DELETE FROM users WHERE (id-1) % 3 = 0')

# Делаем выборку из базы записей, где возраст != 60
cursor.execute('SELECT username, email, age, balance FROM users WHERE age != 60')

# Выводим ее в формате: Имя:{username}|Почта:{email}|Возраст:{age}|Баланс:{balance}, без id
for i in cursor.fetchall():
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')

connection.commit()
connection.close()



