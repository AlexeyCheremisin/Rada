# Task 1

# 1st program
print(9 ** 0.5 * 5)

# Task 2

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# Task 3

# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))
print(2 * 2 + 2 == 2 * (2 + 2))

# Task 4

# 4th program
s = '123.456'
s_to_float = float(s)   # Преобразование во float.
mult_by_10 = s_to_float * 10    # Умножим на 10 для смещения 4 в целую часть.
to_int = int(mult_by_10)    # Преобразуем в int для избавления от дробной части.
print(to_int % 10)  # Получим 4, как остаток от деления на 10.
