# Домашнее задание по уроку "Распаковка позиционных параметров".

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# 1 - Функция с параметрами по умолчанию
print_params(25, "frg", [12, 2, False])
print_params(a = "fgrt")
print_params()

# 2 - Распаковка параметров
values_list = [23.5, '100$', False]
values_dict = {'a': 23.5, 'b': '200$', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3 - Распаковка + отдельные параметры
values_list_2 = [100, '300%']
print_params(*values_list_2, 'И ещё')

