# Домашнее задание по теме "Позиционирование в файле".


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    count = 0
    for i in strings:
        count += 1
        strings_positions[(count, file.tell())] = i
        file.write(i + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
