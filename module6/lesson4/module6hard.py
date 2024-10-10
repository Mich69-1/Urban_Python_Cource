# Дополнительное практическое задание по модулю: "Наследование классов."
import math


class Figure:

    def __init__(self, color, *sides, side_count=0, sides_divider=1):
        if self.__is_valid_color(color):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]
        self.filled = True
        self.side_count = side_count
        self.sides_divider = sides_divider   # Для экземпляров с одинаковыми сторонами (куб или хитрое что)
        if self.__is_valid_sides(sides):
            self.__sides = list(sides) * self.sides_divider
        else:
            self.__sides = [1]*self.side_count

    def __len__(self):
        return sum(self.__sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, rgb):
        passed = False
        if len(rgb) != 3:
            return passed
        for i in rgb:
            if not (isinstance(i, int) and i in range(255)):
                return passed
        passed = True
        return passed

    def set_color(self, *rgb):
        if self.__is_valid_color(rgb):
            self.__color = list(rgb)

    def __is_valid_sides(self, sides):
        passed = False
        if len(sides) != self.side_count/self.sides_divider:
            return passed
        for i in sides:
            if not (isinstance(i, int) and i > 0):
                return passed
        passed = True
        return passed

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)*self.sides_divider  # sides_divider позволяет повторять равные стороны и группы

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides, side_count=1)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return self.__radius**2 * math.pi


class Triangle(Figure):

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides, side_count=3)

    def get_square(self):
        hl = len(self)/2               # hl - полупериметр треугольника
        a, b, c = self.get_sides()     # Стороны треугольника
        return math.sqrt(hl*(hl - a)*(hl - b)*(hl - c))


class Cube(Figure):
    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides, side_count=12, sides_divider=12)

    def get_volume(self):
        return self.get_sides()[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((245, 11, 124), 12, 13, 15)  # Ну пусть тоже будет, зря делал что ли

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка Герона и его формулы
print(triangle1.get_sides())
print(triangle1.get_square())
