# Задача "Однокоренные"


def single_root_words(root_word: str, *other_words: tuple[str]) -> list[str]:
    """
    Функция состовляет новый список из списка *other_words, которые содержат root_word
    или наоборот root_word содержит одно из этих слов.
    :param root_word: строка проверяем ее на вхождение в слова из *other_words
                      или слово root_word содержит одно из этих слов.
    :param other_words: строки для проверки.
    :return: новый список с однокоренными словами.
    """
    if not all(isinstance(word, str) for word in other_words):
        raise TypeError("Все аргументы *other_words должны быть строками!")
    same_words = list()
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)
    if len(same_words) == 0:
        for word in other_words:
            if word.lower() in root_word.lower():
                same_words.append(word)
    return same_words


if __name__ == "__main__":
    result_1 = single_root_words("rich", "richiest", "orichalcum", "cheers", "richies")
    result_2 = single_root_words("Disablement", "Able", "Mable", "Disable", "Bagel")
    print(result_1)
    print(result_2)
