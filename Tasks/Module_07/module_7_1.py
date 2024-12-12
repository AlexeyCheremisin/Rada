# Домашнее задание по теме "Режимы открытия файлов"


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.__name = name
        self.__weight = weight
        self.__category = category

    def __str__(self) -> str:
        return f"{self.__name}, {self.__weight}, {self.__category}"

    def get_name(self) -> str:
        return self.__name


class Shop:

    __file_name = "product.txt"

    def __init__(self):
        file = open(self.__file_name, "w")
        file.write("")
        file.close()

    def get_products(self) -> str:
        file = open(self.__file_name, "r")
        rows = file.read()
        file.close()
        return f"{rows}"

    def add(self, *products: Product):
        for product in products:
            if str(product) not in self.get_products():
                file = open(self.__file_name, "a")
                file.write(f"{str(product)}\n")
                file.close()
            else:
                print(f"Продукт {product.get_name()} уже есть в магазине.")


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)

    s1.add(p1, p2, p3)

    print(s1.get_products())
