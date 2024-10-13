"""
Задача "Счётчик вызовов":

Вам необходимо написать 3 функции:
    1. Функция count_calls подсчитывающая вызовы остальных функций.
    2. Функция string_info принимает аргумент - строку и возвращает кортеж из:
       длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    3. Функция is_contains принимает два аргумента: строку и список, и возвращает True,
       если строка находится в этом списке, False - если отсутствует. Регистром строки
       при проверке пренебречь: UrbaN ~ URBAN.

Пункты задачи:
    1. Создать переменную calls = 0 вне функций.
    2. Создать функцию count_calls и изменять в ней значение переменной calls.
       Эта функция должна вызываться в остальных двух функциях.
    3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
    4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
    5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
    6. Вывести значение переменной calls на экран(в консоль).
"""

calls = 0  # Счетчик вызовов.


def count_calls() -> int:
    """
    Подсчитываем вызовы остальных функций.
    :return: количество вызовов всех функций.
    """
    global calls
    calls += 1
    return calls


def string_info(string: str) -> tuple:
    """
    Принимает аргумент строку и возвращает кортеж.
    :param string: любая строка.
    :return: кортеж состоящий из длины строки, строки в верхнем регистре, строки в нижнем регистре.
    """
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list) -> bool:
    """
    Проверяет, что строка находится в списке, без учета регистра.
    :param string: строка.
    :param list_to_search: список в котором ищем переданную строку.
    :return: True - строка найдена в списке, Else - строка не найдена.
    """
    count_calls()
    list_ = list()
    for elem in list_to_search:
        if isinstance(elem, str):
            list_.append(elem.lower())
        else:
            list_.append(elem)
    return string.lower() in list_


if __name__ == "__main__":
    print(string_info('Forest'))
    print(string_info('Река'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
    print(is_contains('cycle', ['recycling', 'cyclic']))
    print(calls)
