'''
Условие: Разделите видимость полей (сделайте все поля приватными) и методов во всех классах вашей программы.

Решение: в каждом из трех классов я сделал все поля приватными, а также сделал методы сеттеры-геттеры для
управления этими полями.
'''


class User:
    def __init__(self, user_name, user_email, user_password):
        self.__name = user_name
        self.__email = user_email
        self.__password = user_password
        self.__list_favorite_tracks = []
        self.__list_playlists = []

    # Геттеры и сеттеры для полей класса User

    def set_user_name(self, updated_name):
        self.__name = updated_name

    def get_user_name(self):
        return self.__name

    def set_user_email(self, updated_email):
        self.__email = updated_email

    def get_user_email(self):
        return self.__email

    def set_user_password(self, updated_password):
        self.__password = updated_password

    # Методы для работы с любимыми треками и плейлистами
    def add_track_to_favorites(self, track_object):
        self.__list_favorite_tracks.append(track_object)

    def get_favorites_track(self):
        return self.__list_favorite_tracks

    def del_track_from_favorites(self, track_object):
        if track_object in self.__list_favorite_tracks:
            self.__list_favorite_tracks.remove(track_object)
        else:
            print('Трека нет в любимых')

    def add_playlist_to_list_playlists(self, playlist_object):
        self.__list_playlists.append(playlist_object)

    def get_playlists(self):
        return self.__list_playlists

    def del_playlist_from_list(self, playlist_object):
        if playlist_object in self.__list_playlists:
            self.__list_playlists.remove(playlist_object)
        else:
            print('Плейлиста нет в списке')


class Track:
    def __init__(self, title, artist, album, genre, duration):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__genre = genre
        self.__duration = duration

    # Геттеры и сеттеры для полей класса Track

    def set_title_track(self, updated_title):
        self.__title = updated_title

    def get_title_track(self):
        return self.__title

    def set_artist_track(self, updated_artist):
        self.__artist = updated_artist

    def get_artist_track(self):
        return self.__artist

    def set_album_track(self, updated_album):
        self.__album = updated_album

    def get_album_track(self):
        return self.__album

    def set_genre_track(self, updated_genre):
        self.__genre = updated_genre

    def get_genre_track(self):
        return self.__genre

    def set_duration_track(self, updated_duration):
        self.__duration = updated_duration

    def get_duration_track(self):
        return self.__duration

    def delete_track(self):
        self.__title = 'Трек больше не доступен'
        self.__artist = None
        self.__album = None
        self.__genre = None
        self.__duration = None

    def __repr__(self):
        return f"{self.__title} - {self.__artist}"


class Playlist:
    def __init__(self, title, author, description, flag):
        self.__title = title
        self.__tracks = []
        self.__author = author
        self.__description = description
        self.__flag_change_by_others = flag

    # Геттеры и сеттеры для полей класса Playlist

    def set_title_playlist(self, updated_title):
        self.__title = updated_title

    def get_title_playlist(self):
        return self.__title

    def set_author_playlist(self, updated_author):
        self.__author = updated_author

    def get_author_playlist(self):
        return self.__author

    def set_description_playlist(self, updated_description):
        self.__description = updated_description

    def get_description_playlist(self):
        return self.__description

    def set_flag_change_by_others(self, flag):
        self.__flag_change_by_others = flag

    def get_flag_change_by_others(self):
        return self.__flag_change_by_others

    def add_track_to_playlist(self, track_object, user_object):
        if self.__author == user_object or self.__flag_change_by_others:
            self.__tracks.append(track_object)
        else:
            print('Вы не можете добавлять треки в этот плейлист, так как автор ограничил доступ')

    def __repr__(self):
        return str(self.__tracks)
