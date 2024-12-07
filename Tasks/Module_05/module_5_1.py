# Домашняя работа по уроку "Атрибуты и методы объекта"

class House:
    def __init__(self, name: str, number_of_floor: int):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor: int):
        if 1 < new_floor < self.number_of_floor:
            for i in range(new_floor):
                print(f"Этаж номер {i + 1}")
        else:
            print("Такого этажа не существует.")


if __name__ == "__main__":
    house_1 = House("ЖК Эльбрус", 30)
    house_2 = House("Домик в деревне", 2)
    house_1.go_to(18)
    house_2.go_to(10)
    
