# Домашнее задание по теме "Множественное наследование"

from random import choice


class Animal:

    live = True
    sound = None
    __DEGREE_OF_DANGER = 0

    def __init__(self, speed: int, degree_of_danger=__DEGREE_OF_DANGER):
        self._cords = [0, 0, 0]
        self.speed = speed
        self.__DEGREE_OF_DANGER = degree_of_danger

    def move(self, dx, dy, dz):
        dz_ = self._cords[2] + (dz * self.speed)
        if dz_ < 0:
            print("It's too deep, I can't dive:(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = dz_

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self.__DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful:)")
        else:
            print("Be careful, I'm attacking you O_O")

    def speak(self):
        print(self.sound)


class Bird(Animal):

    beak = True

    def lay_eggs(self):
        print(f"Here are(is), {choice([1, 2, 3, 4])} eggs for you")


class AquaticAnimal(Animal):

    __DEGREE_OF_DANGER = 3

    def __init__(self, speed, degree_of_danger=__DEGREE_OF_DANGER):
        super().__init__(speed, degree_of_danger)

    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz * self.speed/2))


class PoisonousAnimal(Animal):

    __DEGREE_OF_DANGER = 8

    def __init__(self, speed, degree_of_danger=__DEGREE_OF_DANGER):
        super().__init__(speed, degree_of_danger)


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):

    sound = "Click-click-click"


if __name__ == "__main__":
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()
