# Домашнее задание по теме "Потоки на классах"

import threading
from time import sleep


class Knight(threading.Thread):
    ENEMIES = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        day_count = 0
        enemies_left = self.ENEMIES
        print(f'{self.name} на нас напали!')
        while enemies_left > 0:
            day_count += 1
            enemies_left -= self.power
            print(f'{self.name} сражается {day_count} день(дня)..., осталось {enemies_left} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
