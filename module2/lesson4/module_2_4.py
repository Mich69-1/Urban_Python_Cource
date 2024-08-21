# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

# Дано
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Найти простые (primes)  и не простые (not_primes) числа
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for j in range(2, i):
        is_prime = True
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i > 1:
        primes.append(i)
    elif i > 1:
        not_primes.append(i)

# Вывод результатов
print(f'Простые: {primes}')
print(f'Не простые: {not_primes}')
