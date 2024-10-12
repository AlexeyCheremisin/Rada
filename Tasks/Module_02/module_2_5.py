"""
Задача "Матрица воплоти":

Напишите функцию get_matrix с тремя параметрами n, m и value,
которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
заполненную значениями value и возвращать эту матрицу в качестве результата работы.

Пункты задачи:
    1. Объявите функцию get_matrix и напишите в ней параметры n, m и value.
    2. Создайте пустой список matrix внутри функции get_matrix.
    3. Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
    4. В первом цикле добавляйте пустой список в список matrix.
    5. Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
    6. Во втором цикле пополняйте ранее добавленный пустой список значениями value.
    7. После всех циклов верните значение переменной matrix.
    8. Выведите на экран(консоль) результат работы функции get_matrix.
"""


def get_matrix(n, m, value):
    matrix = list()
    for i in range(n):
        matrix.append(list())
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(0, 1, 11)
result5 = get_matrix(7, 0, 99)
result6 = get_matrix(-1, 6, 32)
result7 = get_matrix(4, -2, 84)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
