# Дополнительное практическое задание по модулю: "Базовые структуры данных."

# Исходные данные: списки оценок даны в алфавитном порядке, множесво имен не отсортировано
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в сортированный список
students_sorted = sorted(students)

# Вычисляем средние баллы и получаем их список
grades_average = list(map(lambda x: sum(x)/len(x), grades))

# Получаем из сортированного списка набор кортежей
students_grades = zip(students_sorted, grades_average)

# Преобразуем zip-объект в словарь и выводим
students_grades = dict(students_grades)
print(students_grades)

