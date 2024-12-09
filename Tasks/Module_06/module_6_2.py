# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."


class Vehicle:

    __COLOR_VARIANTS = ["WHITE", "SILVER", "BLACK", "GREY", "BLUE", "RED", "BROWN", "GREEN"]

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color.upper()

    def get_model(self) -> str:
        return f"Модель {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color.upper()
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5


if __name__ == "__main__":
    vehicle_1 = Sedan("Fedos", "Toyota Mark II", 500, "blue")
    vehicle_1.print_info()

    vehicle_1.set_color("Orange")
    vehicle_1.set_color("BLACK")
    vehicle_1.owner = "Pashok"

    vehicle_1.print_info()
