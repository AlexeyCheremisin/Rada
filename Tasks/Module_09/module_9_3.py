# Домашнее задание по теме "Генераторные сборки"


if __name__ == "__main__":
    first = ['Strings', 'Student', 'Computers']
    second = ['Строка', 'Урбан', 'Компьютер']

    first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))
    print(list(first_result))

    second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j)
    print(list(second_result))
