# Подробнее о функциях.

amount = 0


def calculate_structure_data(structure):
    global amount
    if isinstance(structure, (list, set, tuple)):
        for elem in structure:
            calculate_structure_data(elem)
    elif isinstance(structure, dict):
        for key in structure.keys():
            calculate_structure_data(key)
        for value in structure.values():
            calculate_structure_data(value)
    elif isinstance(structure, int):
        amount = amount + structure
    elif isinstance(structure, str):
        amount = amount + len(structure)
    return amount


if __name__ == "__main__":
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
    result = calculate_structure_data(data_structure)
    print(result)
