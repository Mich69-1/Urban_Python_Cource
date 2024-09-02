# Дополнительное практическое задание по модулю: "Подробнее о функциях."

def expand_and_sum(data_s):
    if any(isinstance(sub, (list, tuple, dict, set)) for sub in data_s):  # Преобразование в список без вложенных структур
        elem = data_s.pop(0)
        if isinstance(elem, dict):
            data_s.extend(list(elem.items()))
        elif isinstance(elem, (list, tuple, set)):
            data_s.extend(list(elem))
        else:
            data_s.append(elem)
        return expand_and_sum(data_s)  # return обязателен!
    else:
        structure_sum = 0
        for i in data_s:
            if isinstance(i, (int, float)):
                structure_sum += i
            else:
                structure_sum += len(i)
        return structure_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = expand_and_sum(data_structure)
print(result)
print(data_structure)
