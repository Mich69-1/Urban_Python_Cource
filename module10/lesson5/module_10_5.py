# Домашнее задание по теме "Многопроцессное программирование"
from time import time
from datetime import timedelta
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line != '':
            all_data.append(line)
            line = file.readline()
    print(f'Файл {name} содержит {len(all_data)} строк')


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# t_start = time()
# for filename in filenames:
#     read_info(filename)
# t_end = time()
# print(f'Время выполнения: {timedelta(seconds=t_end - t_start)}')

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    t_start = time()
    pool.map(read_info, filenames)  # Непонятно, зачем тут контекстный менеджер with, map самодостаточен
    t_end = time()
    print(f'Время выполнения: {timedelta(seconds=t_end - t_start)}')
