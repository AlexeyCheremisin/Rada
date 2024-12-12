# Домашнее задание по теме "Позиционирование в файле"


def custom_write(file_name: str, strings: [str]) -> {(int, int): str}:
    dict_ = {}
    file = open(file_name, "w", encoding="utf-8")
    for index in range(len(strings)):
        dict_[(index + 1, file.tell())] = strings[index]
        file.write(f"{strings[index]}\n")
    file.close()
    return dict_


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)

    for elem in result.items():
        print(elem)
