# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(str_pair[0]) - len(str_pair[1]))
                for str_pair in zip(first, second) if len(str_pair[0]) != len(str_pair[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))