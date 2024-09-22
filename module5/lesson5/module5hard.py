# Дополнительное практическое задание по модулю: "Классы и объекты."

from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title, duration, adult_mode=False, time_now=0):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __eq__(self, other):
        return self.title == other.title


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if len(self.users):
            for i in self.users:
                if i.nickname == nickname and i.password == hash(password):
                    self.current_user = i
                    print(f"{nickname} успешно авторизован")
                    return
            print("Неверное имя пользователя или пароль!")

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if len(self.users):
            for i in self.users:
                if i.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    return
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def add_videos(self, *args):
        for i in args:
            found = False
            for j in self.videos:
                if i == j:
                    found = True
                    break
            if not found:
                self.videos.append(i)

    def get_videos(self, s_string):
        found_titles = []
        for i in self.videos:
            if s_string.lower() in i.title.lower():
                found_titles.append(i.title)
        return found_titles

    def watch_video(self, video_title):
        if self.current_user:
            for i in self.videos:
                if i.title == video_title:
                    if i.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                    else:
                        for j in range(i.duration):
                            i.time_now = j+1
                            print(i.time_now, end=' ')
                            sleep(1)
                        print('Конец видео')
                        return
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add_videos(v1, v2)

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
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


