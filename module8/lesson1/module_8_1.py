# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    result = 0
    try:
        result = round(a + b, 3)
    except TypeError:
        result = str(a) + str(b)
    finally:
        return result


def add_unlimited_up(*a):
    result = 0
    try:
        for i in a:
            result += i
    except TypeError:
        result = ''
        for i in a:
            result += str(i)
    finally:
        return result


# Основное задание
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# Эксперимент
print(add_unlimited_up(23, 37.2, 25))
print(add_unlimited_up(23, 37.2, 25, 'Я все испортил!', 25.6))
