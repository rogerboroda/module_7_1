import os

class Product:
    """
    Класс Product:
    Имеет конструктор для инициализации объектов с атрибутами name, weight и category
    Метод __str__ возвращает строку
    """

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    """
    Класс Shop:
    Содержит инкапсулированный атрибут file_name = 'products.txt'
    Метод get_products открывает файл для чтения и возвращает все продукты в виде строки.
    Метод add принимает список объектов Product, проверяет их наличие в файле и добавляет, если они еще не существуют.
    """

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if not os.path.exists(self.__file_name):  # Проверяем, существует ли файл
            return ''
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        existing_products = self.get_products().splitlines() if self.get_products() else []

        for product in products:
            product_str = str(product)
            if any(product.name == line.split(', ')[0] for line in existing_products):
                print(f'Продукт {product_str} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(product_str + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato, 50.5, Vegetables уже есть в магазине
# Продукт Spaghetti, 3.4, Groceries уже есть в магазине
# Продукт Potato, 5.5, Vegetables уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables