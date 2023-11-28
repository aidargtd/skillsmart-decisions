"""
 Реализуйте композицию для двух иерархий классов из предыдущего занятия. Напишите код для работы
 с объектами соответствующих классов, из которого наглядно понятна идея композиции.
"""


# Родительский класс - чай
class Tea:
    def __init__(self, tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves):
        self.type_of_tea = tea_type
        self.origin = origin
        self.color_of_brew = color
        self.brewing_method = brew_method
        self.caffeine_content = percent_of_caffeine
        self.type_of_leaves = type_leaves


# Дочерний класс для класса "чай", Зеленый чай
class Puer(Tea):
    def __init__(self, tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves, aging_years):
        super().__init__(tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves)
        self.aging_years = aging_years  # Возраст пуэра в годах

    def calculate_cost_of_puer(self):
        rating = ((self.aging_years * 0.1) + self.caffeine_content) / 30
        return f"Цена чая: {rating * 10}$ за сто грамм"


# Родительский класс - аксессуар для чая
class TeaAccessory:
    def __init__(self, name, material):
        self.name = name
        self.material = material


# Дочерний класс для класса "аксессуар для чая", Заварочный чайник
class Teapot(TeaAccessory):
    def __init__(self, name, material, volume, tea_amount):
        super().__init__(name, material)
        self.volume = volume
        self.tea_amount = tea_amount

    def calculate_water_to_tea_ratio(self):
        # Рассчитываем соотношение воды к количеству чая
        water_to_tea = self.volume / self.tea_amount
        if 40 < water_to_tea < 60:
            return 'Все в норме!'
        else:
            return 'Надо поменять соотношения'


"""
В прошлом дз я делал два класса Tea и TeaAccessory, но я не совсем понимаю, как сделать
их комопозицию, да и не совсем понимаю зачем.
Так что я использовал предыдущее дз, где я уже делал комопзицию функций.
Например, в классе User в методах, связанных с плейлистами треками, я запрашивал
на входе объекты классов Track и Playlist.

Также в классе Playlist для того, чтобы добавить трек в плейлист или удалить его,
надо вызвать метод, который запрашивает объект трека.
"""


class User:
    def __init__(self, user_name, user_email, user_password):
        self.name = user_name
        self.email = user_email
        self.password = user_password
        self.list_favorite_tracks = []
        self.list_playlists = []

    def change_user_name(self, updated_name):
        self.name = updated_name

    def change_user_email(self, updated_email):
        self.name = updated_email

    def change_user_password(self, updated_password):
        self.password = updated_password

    def add_track_to_favorites(self, track_object):
        self.list_favorite_tracks.append(track_object)

    def del_track_from_favorites(self, track_object):
        if track_object in self.list_favorite_tracks:
            del self.list_favorite_tracks[self.list_favorite_tracks.index(track_object)]
            # очевидно, что это будет долго работать, но интуитивно понятно
        else:
            print('Трека нет в любимых')

    def add_playlist_to_list_playlists(self, playlist_object):
        self.list_playlists.append(playlist_object)

    def del_playlist_from_list(self, playlist_object):
        if playlist_object in self.list_playlists:
            del self.list_playlists[self.list_playlists.index(playlist_object)]
            # очевидно, что это будет долго работать, но интуитивно понятно
        else:
            print('Плейлиста нет в списке')


user1 = User('Aidar', 'test123@gmail.com', 'spotify1234')  # Создал первого пользователя


# class Track отвечает за публикацию трека на музыкальную площадку
class Track:
    def __init__(self, title, artist, album, genre, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

        # Создадим базовые функции изменения данных о треке, они будут работать аналогично смены данных пользователя

    def change_title_track(self, updated_title):
        self.title = updated_title

    def change_artist_track(self, updated_artist):
        self.artist = updated_artist

    def change_album_track(self, updated_album):
        self.artist = updated_album

    def change_genre_track(self, updated_genre):
        self.genre = updated_genre

    # Создадим функцияю удаления трека с музыкальной площадки, объект будет в памяти, но данные будут неизвестные

    def del_track(self):
        self.title = 'Трек больше не доступен'
        self.artist = None
        self.album = None
        self.genre = None
        self.duration = None

    def __repr__(self):
        return f"{self.title} - {self.artist}"


class Playlist:
    def __init__(self, title, author, description, flag):
        self.title = title
        self.tracks = []
        self.author = author
        self.description = description
        self.flag_change_by_others = flag
        # если значение flag == True, то плейлист public. Иначе private, т.е без возможности редактирования

    # В классе плейлиста можно создать методы по редактированию данных
    def change_title_playlist(self, updated_title):
        self.title = updated_title

    def change_author_playlist(self, updated_author):
        self.author = updated_author

    def change_description_playlist(self, updated_description):
        self.description = updated_description

    def add_track_to_playlist(self, track_object, user_object):
        # проверка возможности добавления треков в плейлист для других пользователей
        if (self.author == user_object) or (self.flag_change_by_others):
            self.tracks.append(track_object)
        else:
            print('Вы не можете добавлять треки в этот плейлист, так как автор ограничил доступ')

    def __repr__(self):
        return str(self.tracks)
