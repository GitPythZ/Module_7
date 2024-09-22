from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        """
        Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
        Все данные в строке разделены запятой с пробелами.
        """
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self, file_name="products.txt"):
        self.__file_name = file_name

    def get_products(self):
        """
        Метод get_products(self), который считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        """
        file = open(self.__file_name, "r")
        try:
            return file.read()
        finally:
            file.close()

    def add(self, *products):
        """Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
        """
        for product in products:
            if product.name in self.get_products():
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                file = open(self.__file_name, "a")
                file.write(str(product) + "\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
