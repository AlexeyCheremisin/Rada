# Задача "Распаковка".


def print_params(a=1, b="строка", c=True):
    print(a, b, c)


if __name__ == "__main__":
    print_params()

    print_params(a=2)
    print_params(b="test")
    print_params(c=False)

    print_params(a="Test", b=4, c=[1, 3])
    print_params(b=25)
    print_params(c=[1, 2, 3])

    values_list = [False, 5.76, "Test"]
    values_dict = {"a": "1111", "b": ("%", "#"), "c": 9.1}

    print_params(*values_list)
    print_params(**values_dict)

    values_list_2 = ["Test", True]
    print_params(*values_list_2, 42)
