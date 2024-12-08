# Дополнительное практическое задание по модулю: "Классы и объекты."

from time import sleep


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname.strip()
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title.strip()
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:   

    users = []
    videos = []
    current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname.strip() and user.password == hash(password):
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        flag = True
        for user in self.users:
            if user.nickname == nickname.strip():
                print(f"Пользователь {nickname.strip()} уже существует.")
                flag = False
                break
        if flag:
            new_user = User(nickname.strip(), hash(password), age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args: Video):
        for element in args:
            flag = True
            for video in self.videos:
                if element.title == video.title:
                    flag = False
                    break
            if flag:
                self.videos.append(element)

    def get_videos(self, word: str) -> list[str]:
        result = []
        for video in self.videos:
            if word.strip().lower() in video.title.lower():
                result.append(video.title)

        return result

    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео.")
        else:
            result = None
            for video in self.videos:
                if title.strip() == video.title:
                    result = video
                    break
            if result:
                flag = True
                if result.adult_mode:
                    if self.current_user.age >= 18:
                        flag = True
                    else:
                        flag = False
                        print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                if flag:
                    for s in range(result.duration):
                        sleep(1)
                        print(f"{result.time_now + 1}", end=" ")
                        result.time_now += 1
                    print("Конец видео")
                    result.time_now = 0


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
