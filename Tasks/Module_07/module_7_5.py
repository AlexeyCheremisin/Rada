# Домашнее задание по теме "Файлы в операционной системе"
from os import walk, path
from time import strftime, localtime

if __name__ == "__main__":
    directory = "."
    for root, dirs, files in walk(directory):
        for file in files:
            file_path = path.join(root, file)
            file_time = path.getmtime(file_path)
            formatted_time = strftime("%d.%m.%Y %H:%M", localtime(file_time))
            file_size = path.getsize(file_path)
            parent_dir = path.dirname(file_path)
            print(
                f"Обнаружен файл: {file}, "
                f"Путь: {file_path}, "
                f"Размер: {file_size} байт, "
                f"Время изменения: {formatted_time}, "
                f"Родительская директория: {parent_dir}"
            )
