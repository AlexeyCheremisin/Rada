# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"


def personal_sum(numbers: list | tuple) -> (int | float, int):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {number}")
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers: list | tuple) -> float | int | None:
    try:
        sum_ = personal_sum(numbers)
        result = sum_[0] / (len(numbers) - sum_[1])
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        result = None

    return result


if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
    print(f'Результат 3: {calculate_average(567)}')
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
