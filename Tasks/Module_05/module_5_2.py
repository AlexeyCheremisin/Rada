# Домашняя работа по уроку "Специальные методы классов"

class House:
    def __init__(self, name: str, number_of_floor: int):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self) -> int:
        return self.number_of_floor

    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}."

    def go_to(self, new_floor: int):
        if 1 < new_floor < self.number_of_floor:
            for i in range(new_floor):
                print(f"Этаж номер {i + 1}")
        else:
            print("Такого этажа не существует.")


if __name__ == "__main__":
    house_1 = House("ЖК Эльбрус", 10)
    house_2 = House("ЖК Акация", 20)

    # __srr__
    print(house_1)
    print(house_2)

    # __len__
    print(len(house_1))
    print(len(house_2))
