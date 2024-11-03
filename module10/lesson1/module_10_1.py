# Домашнее задание по теме "Введение в потоки".

from time import sleep, time
from datetime import timedelta
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


t_start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
t_end = time()
print(f'Работа потоков {timedelta(seconds=t_end - t_start)}')
ww_thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
ww_thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
ww_thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
ww_thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
t_start = time()
ww_thread1.start()
ww_thread2.start()
ww_thread3.start()
ww_thread4.start()
ww_thread1.join()
ww_thread2.join()
ww_thread3.join()
ww_thread4.join()
t_end = time()
print(f'Работа потоков {timedelta(seconds=t_end - t_start)}')
