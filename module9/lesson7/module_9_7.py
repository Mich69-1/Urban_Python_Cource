# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(a, b, c):
        number = func(a, b, c)
        if number % 2 == 0:
            if number == 2:
                print('Простое')
                return number
        d = 3
        while d * d <= number and number % d != 0:
            d += 2
        if d * d > number:
            print('Простое')
            return number
        print('Составное')
        return number
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
