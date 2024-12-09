# Домашнее задание по теме "Зачем нужно наследование"


class Plant:
    def __init__(self, name: str, edible=False):
        self.name = name
        self.edible = edible


class Animal:
    def __init__(self, name: str, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food: Plant):
        if food.edible:
            print(f"{self.name} съел {food.name}.")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}.")
            self.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name: str, edible=True):
        super().__init__(name, edible)


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
