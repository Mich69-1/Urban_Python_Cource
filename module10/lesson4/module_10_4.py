# Домашнее задание по теме "Очереди для обмена данными между потоками."

import threading
from random import randint
from time import sleep
from queue import Queue


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(1, 10))  # Задержка в 1-10 секунд


class Cafe:

    def __init__(self, *args):
        self.tables = [i for i in args]
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    # Выводим в консоль название гостя и номер стола
                    break
            if guest.is_alive() is False:  # Если гость не попал за столик и поток не запущен
                self.queue.put(guest)  # Добавляем гостя в очередь
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while self.queue.empty() is False or all(table.guest is None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive() is not True:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\n'
                          f'Стол номер {table.number} свободен')
                    table.guest = None
                    if self.queue.empty() is False:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita',
                'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests_ = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests_)
# Обслуживание гостей
cafe.discuss_guests()
