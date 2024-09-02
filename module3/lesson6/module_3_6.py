import copy

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def expand_and_sum(data_s):
    data_copy = copy.deepcopy(data_s)
    if any(isinstance(sub, (list, tuple, dict, set)) for sub in data_copy):
        elem = data_copy.pop(0)
        if isinstance(elem, (list, tuple, dict, set)):
            data_copy.extend(list(elem))
            expand_and_sum(data_copy)
        else:
            data_copy.append(elem)
            expand_and_sum(data_copy)
    else:
        print(data_copy)
        return data_copy


result = expand_and_sum(data_structure)
print(result)
