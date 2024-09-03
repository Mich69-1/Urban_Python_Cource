# Деление на 0 выдает бесконечность

from math import inf
def divide_t(first, second):
    if second:
         return first / second
    else:
        return inf
