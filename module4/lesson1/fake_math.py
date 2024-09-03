# Деление на 0 выдает ошибку

def divide_t(first, second):
    if second:
         return first / second
    else:
        return 'На 0 делить нельзя!'
