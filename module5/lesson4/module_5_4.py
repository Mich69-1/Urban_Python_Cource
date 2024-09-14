# Домашняя работа по уроку "Перегрузка операторов."


class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    @staticmethod
    def type_depended_return(obj):  # Функция проверки типа, чтобы не загромождать
        if isinstance(obj, House):
            return obj.number_of_floors
        elif isinstance(obj, int):
            return obj
        else:
            print('Некорректный тип данных: нужен дом или целое число!')
            return 0

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == self.type_depended_return(other)

    def __lt__(self, other):
        return self.number_of_floors < self.type_depended_return(other)

    def __le__(self, other):
        return self.number_of_floors <= self.type_depended_return(other)

    def __gt__(self, other):
        return self.number_of_floors > self.type_depended_return(other)

    def __ge__(self, other):
        return self.number_of_floors >= self.type_depended_return(other)

    def __ne__(self, other):
        return self.number_of_floors != self.type_depended_return(other)

    def __add__(self, other):
        self.number_of_floors += self.type_depended_return(other)
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def go_to(self, new_floor):
        if self.type_depended_return(new_floor) > self.number_of_floors or self.type_depended_return(new_floor) < 1:
            print('Такого этажа не существует')
            return
        for i in range(self.type_depended_return(new_floor)):
            print(i+1)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# И последний..
del h1
