# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"

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

# Удаляем запись с id=6
cursor.execute('DELETE FROM users WHERE id = 6')

# Подсчитываем количество записей в таблице
cursor.execute('SELECT COUNT(*) FROM users')
total_users = cursor.fetchone()[0]

# Подсчитываем сумму всех балансов (полей balance)
cursor.execute('SELECT SUM(balance) FROM users')
all_balances = cursor.fetchone()[0]

# Подсчитываем средний баланс и выводим
print(f'Средний баланс: {all_balances/total_users}')



connection.commit()
connection.close()