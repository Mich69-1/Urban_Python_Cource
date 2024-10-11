# Домашнее задание по теме "Режимы открытия файлов"

import os

class Product:

    def __new__(cls, name, weight, category):
        if not (isinstance(name, str
                           ) and isinstance(weight, float
                                            ) and isinstance(category, str
                                                             ) and weight > 0):
            print('Некорректные данные, товар не принят!')
            return
        return super().__new__(cls)

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name
        if not os.path.exists(self.__file_name):
            file = open(self.__file_name, 'a+')
            file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        current_content = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if not (product.name in current_content):
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине' )
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())