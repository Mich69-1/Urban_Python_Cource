# Домашнее задание по уроку "Пространство имен"

def test_function(a = 'Я из test_function'):
    def inner_function():
        nonlocal a
        print("Я в области видимости функции test_function")
        print(a)
        a = 'Меня поменяли в inner_function!'
        print(a)
    inner_function()


test_function()
test_function('И я из test_function')

# inner_function() - Error, name 'inner_function' is not defined