# Домашнее задание по теме "Введение в функциональное программирование"


def apply_all_func(int_list: [int | float], *functions) -> dict:
    result = {}
    for function in functions:
        key = function.__name__
        value = function(int_list)
        result[key] = value

    return result


if __name__ == "__main__":
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
