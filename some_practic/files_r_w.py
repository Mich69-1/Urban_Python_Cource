import json

# Запись словаря в файл
def write_dict_to_file(filename, dictionary):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)

# Чтение словаря из файла
def read_dict_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Пример использования
f_ = "my_dictionary.json"  # Имя файла
a_ = {"key1": "value1", "key2": "value2", "key3": "балам-балам"}  # Словарь для записи

# Запись словаря в файл
write_dict_to_file(f_, a_)

# Чтение словаря из файла
loaded_dict = read_dict_from_file(f_)
print(loaded_dict)