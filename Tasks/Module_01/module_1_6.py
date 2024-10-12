"""
Практическое задание по теме: "Словари и множества"

Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.

1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_6.py' и напишите весь код в нём.

2. Работа со словарями:

  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.

Например: Имя(str)-Год рождения(int).

  - Выведите на экран словарь my_dict.

  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.

  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.

 - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.

  - Выведите на экран словарь my_dict.

3. Работа с множествами:

  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.

  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).

  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.

  - Удалите один любой элемент из множества my_set.

  - Выведите на экран измененное множество my_set.
"""

my_dict = {
    "January": 31,
    "February": (28, 29),
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
print(my_dict)
print(my_dict['February'])
print(my_dict.get('Январь'))
my_dict.update(
    {
        "Январь": 31,
        "Февраль": (28, 29)
    }
)
print(my_dict.pop('January'))
print(my_dict)

my_set = {'String', 'String', 2, 3, 1, 3, 2, 1, 4, 5, (1, 2), (1, 2)}
print(my_set)
my_set.update({7, (4, 3)})
my_set.remove(1)
print(my_set)
