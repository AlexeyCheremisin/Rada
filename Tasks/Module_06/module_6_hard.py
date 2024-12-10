# Дополнительное практическое задание по модулю*
from math import pi, sqrt


class Figure:

    sides_count = 0
    __sides = []
    __color = (0, 0, 0)
    filled = False

    def __init__(self, color: (int, int, int), *sides: int):
        if self.__is_valid_color(*color):
            self.__color = color
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1 for _ in range(self.sides_count)]

    def get_color(self) -> (int, int, int):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        rng = list(range(256))
        return r in rng and g in rng and b in rng

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides) -> bool:
        result = False
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                result = True
                if not (isinstance(side, int) and side > 0):
                    result = False
                    break
        return result

    def get_sides(self) -> [int]:
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides: [int]):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):

    sides_count = 1

    def __init__(self, color: (int, int, int), *sides: int):
        super().__init__(color, *sides)
        self.__radius = 2 * pi * self.get_sides()[0]

    def get_square(self) -> float:
        return pi * (self.__radius ** 2)

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color: (int, int, int), *sides: int):
        super().__init__(color, *sides)


    def get_square(self) -> float:
        a, b, c = tuple(self.get_sides())
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):

    sides_count = 12

    def __init__(self, color: (int, int, int), side: int):
        super().__init__(color, side)
        if isinstance(side, int) and side > 0:
            self.__sides = [side for _ in range(self.sides_count)]
        else:
            self.__sides = [1 for _ in range(self.sides_count)]

    def get_sides(self) -> [int]:
        return self.__sides

    def set_sides(self, new_side: int):
        if isinstance(new_side, int) and new_side > 0:
            self.__sides = [new_side for _ in range(self.sides_count)]

    def get_volume(self) -> int:
        return self.__sides[0] ** 3

if __name__ == "__main__":
    # Color
    print("# Color")
    circle_1 = Circle((100, 100, 100), 3)
    circle_2 = Circle((50, 50, 350), 40)
    print(circle_1.get_color())
    print(circle_2.get_color())

    triangle_1 = Triangle((40, 40, 40), 1, 2, 3)
    triangle_2 = Triangle((70, -40, 40), 4, 5, 6)
    print(triangle_1.get_color())
    print(triangle_2.get_color())

    cube_1 = Cube((230, 50, 70), 4)
    cube_2 = Cube((256, 50, 70), 4)
    print(cube_1.get_color())
    print(cube_2.get_color())

    # Sides
    print("\n# Sides")
    circle_1 = Circle((100, 100, 100), 3)
    circle_2 = Circle((100, 100, 100), 40, 50, 70)
    print(circle_1.get_sides())
    print(circle_2.get_sides())

    triangle_1 = Triangle((100, 100, 100), 1, 2, 3)
    triangle_2 = Triangle((100, 100, 100), 4, 5)
    print(triangle_1.get_sides())
    print(triangle_2.get_sides())

    cube_1 = Cube((100, 100, 100), 4)
    cube_2 = Cube((100, 100, 100), -4)
    print(cube_1.get_sides())
    print(cube_2.get_sides())

    # Length and Square
    print("\n# Length and Square")
    print(len(circle_1))
    print(circle_1.get_square())
    print(len(circle_2))
    print(circle_2.get_square())
    print("___________________")
    print(len(triangle_1))
    print(triangle_1.get_square())
    print(len(triangle_2))
    print(triangle_2.get_square())
    print("___________________")
    print(len(cube_1))
    print(cube_1.get_volume())
    print(len(cube_2))
    print(cube_2.get_volume())

    # Setters
    print("\n# Setters")
    circle_1 = Circle((100, 100, 100), 30)
    print(circle_1.get_sides())
    circle_1.set_sides(40)
    print(circle_1.get_sides())
    circle_1.set_sides(10, 20, 30)
    print(circle_1.get_sides())
    circle_1.set_sides(-6)
    print(circle_1.get_sides())
    print("___________________")

    triangle_1 = Triangle((100, 100, 100), 30, 40, 50)
    print(triangle_1.get_sides())
    triangle_1.set_sides(60, 50, 70)
    print(triangle_1.get_sides())
    triangle_1.set_sides(100, 200)
    print(triangle_1.get_sides())
    triangle_1.set_sides(60, -50, 70)
    print(triangle_1.get_sides())
    print("___________________")

    cube_1 = Cube((100, 100, 100), 55)
    print(cube_1.get_sides())
    cube_1.set_sides(44)
    print(cube_1.get_sides())
    cube_1.set_sides(-44)
    print(cube_1.get_sides())
    