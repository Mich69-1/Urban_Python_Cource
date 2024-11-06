# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            payment = randint(50, 500)
            self.balance += payment
            print(f'Пополнение: {payment}. Баланс: {self.balance}')
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            take_req = randint(50, 500)
            print(f'Запрос на {take_req}')
            if take_req <= self.balance:
                self.balance -= take_req
                print(f'Снятие: {take_req}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
