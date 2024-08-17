# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = 1, 2, 'строка', [1, '2nd elem'], False
print('Immutable tuple:', immutable_var)

# Попытка изменить элемент кортежа вызывает ошибку - класс tuple неизменяемый
# immutable_var[2] = 'не строка'

# Однако, если объект кортежа сам по себе является изменяемым типом (list), то элементы этого объекта можно менять
# "Вассал моего вассала - не мой вассал"
immutable_var[3][1] = True
print('Immutable tuple with list member changed:', immutable_var)

# Список
mutable_list = [1, 'second', True, 2.12, [1, 2, 2]]
mutable_list[0] = 'first'
mutable_list[-1] = False
print('Mutable list:', mutable_list)

