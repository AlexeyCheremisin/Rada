# Домашняя работа по уроку "Перегрузка операторов"

class House:
    def __init__(self, name: str, number_of_floor: int):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self) -> int:
        return self.number_of_floor

    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}."

    def __eq__(self, other) -> bool:
        if not isinstance(other, House):
            raise TypeError("Тип обьекта должен быть <House>.")
        return self.number_of_floor == other.number_of_floor

    def __lt__(self, other) -> bool:
        if not isinstance(other, House):
            raise TypeError("Тип обьекта должен быть <House>.")
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other) -> bool:
        if not isinstance(other, House):
            raise TypeError("Тип обьекта должен быть <House>.")
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other) -> bool:
        if not isinstance(other, House):
            raise TypeError("Тип обьекта должен быть <House>.")
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other) -> bool:
        if not isinstance(other, House):
            raise TypeError("Тип обьекта должен быть <House>.")
        return self.number_of_floor <= other.number_of_floor

    def __ne__(self, other) -> bool:
        if not isinstance(other, House):
            raise TypeError("Тип обьекта должен быть <House>.")
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Тип обьекта должен быть <int>.")
        self.number_of_floor += value
        return self

    def __radd__(self, value: int):
        return self + value

    def __iadd__(self, value: int):
        return self + value

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

    print(house_1 == house_2)  # __eq__

    house_1 = house_1 + 10  # __add__
    print(house_1)
    print(house_1 == house_2)

    house_1 += 10  # __iadd__
    print(house_1)

    house_2 = 10 + house_2  # __radd__
    print(house_2)

    print(house_1 > house_2)  # __gt__
    print(house_1 >= house_2)  # __ge__
    print(house_1 < house_2)  # __lt__
    print(house_1 <= house_2)  # __le__
    print(house_1 != house_2)  # __ne__
