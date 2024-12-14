# Домашнее задание по теме "Try и Except"

def add_everything_up(a: str | int | float, b: str | int | float) -> str | int | float:
    try:
        result = a + b
    except TypeError:
        result = str(a) + str(b)
    return result


if __name__ == "__main__":
    print(add_everything_up(999.0888, "строчка"))
    print(add_everything_up("каштан", 88844))
    print(add_everything_up(88.99, 0.01))
