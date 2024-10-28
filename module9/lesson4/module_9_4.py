# Домашнее задание по теме "Создание функций на лету"

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for line_ in data_set:
                file.write(str(line_) + '\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
from random import choice
class MysticBall:

    def __init__(self, *strings):
        self.words = strings

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Не знаю')
print(first_ball())
print(first_ball())
print(first_ball())

