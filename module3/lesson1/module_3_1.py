# Домашняя работа по уроку "Пространство имён"


calls = 0   # счетчик вызовов функций


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    in_list_to_search = False
    for i in range(len(list_to_search)):
        in_list_to_search = string.lower() == str(list_to_search[i]).lower()
        if in_list_to_search:
            return in_list_to_search
    return in_list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches
print(calls)
