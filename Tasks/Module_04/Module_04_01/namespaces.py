# Домашнее задание по уроку "Пространство имен"

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()    # Здесь функция inner_function часть локального пространства имен функции test_function.

if __name__ == "__main__":
    test_function()
    inner_function() # Ошибка функция не видна из глобального пространства имен.
