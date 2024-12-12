# Домашнее задание по теме "Оператор "with"
import re


class WordsFinder:

    def __init__(self, *file_names: str):
        self.file_names = file_names

    def get_all_words(self) -> {str: [str]}:
        all_words = {}
        for file in self.file_names:
            with open(file, encoding="utf-8") as f:
                text = f.read()
                text = text.lower()
                text = re.sub(r"[.,!?:;=]", "", text)
                text = text.replace(" - ", " ")
                all_words[file] = text.split()
        return all_words

    def find(self, word: str) -> {str: int}:
        dict_ = self.get_all_words()
        for key, value in dict_.items():
            if word.lower() in value:
                dict_[key] = value.index(word.lower()) + 1
        return dict_

    def count(self, word: str) -> {str: int}:
        dict_ = self.get_all_words()
        for key, value in dict_.items():
            if word.lower() in value:
                dict_[key] = value.count(word.lower())
        return dict_


if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
