# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

# Ввод чисел2
first = int(input("Введите число 1: "))
second = int(input("Введите число 2: "))
third =  int(input("Введите число 3: "))

# Сравнение и вывод
if first == second and first == third:
    print(3, "числа равны")
elif first == second or first == third or second == third:
    print(2, "числа равны")
else:
    print(0, "чисел равны")