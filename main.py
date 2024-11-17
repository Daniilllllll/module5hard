import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time = 0
        self.adult_mode = adult_mode



class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f"Привет, {nickname}")
                return
        print("Введены некорректные данные!")

    def registr(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему")

    def exit (self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add (self, *videos):
        for video in videos:
            if not any(i.title == video.title for i in self.videos):
                self.videos.append(video)
            else:
                print(f"Видео с названием {video.title} уже существует!")

    def get_video(self, keyword):
        keyword = keyword.lower()
        itog = [
            video.title for video in self.videos
            if keyword in video.title.lower()
        ]
        return itog

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы продолжить.")
            return

        video = next((i for i in self.videos if i.title == title), None)
        if not video:
            print("Видео не найдено.")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("К сожалению придётся подождать до 18 лет(")
            return

        print(f"Воспроизведение видео: {title}")
        while video.time_now < video.duration:
            print(f"Проигрывается {title}, секунда {video.time_now + 1} из {video.duration}")
            video.time_now += 1
            time.sleep(1)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_video('лучший'))
print(ur.get_video('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.registr('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.registr('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.registr('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')