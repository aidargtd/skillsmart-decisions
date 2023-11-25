'''
Дополните два класса, которые вы спроектировали в предыдущем задании, методами, подходящими для логики работы с ними.
В каждом классе должно быть не менее трёх методов. Добавьте в каждый класс конструктор.
Если предыдущий вариант оказался не очень удачным (так как вы создавали классы, исходя из списка их атрибутов),
придумайте новые классы. Создайте несколько объектов этих классов, повызывайте их методы, выведите вычисляемые с
помощью методов значения на экран.
'''


# class User отвечает за создание пользователя музыкального сервиса
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
print('*** Вызовем функцию изменения данных пользователя, а именно смену пароля, остальные работают аналогично')

print(f'Изначальный пароль пользователя: {user1.password}')
user1.change_user_password('test_pass_1234')
print(f'Новый пароль пользователя после вызова метода: {user1.password}')
print()


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


# Создадим несколько объектов треков
track1 = Track('Малинки', 'Группа Кино', 'Ненависть', 'hard metal', '3:30')
track2 = Track('Space', 'The Neighbourhood', 'road', 'rap', '2:31')
track3 = Track('С новым годом!', 'lana del ray', None, 'soft-rock', '2:11')
track4 = Track('be different', 'steve', 'generation', 'pop', '4:51')

print(
    f'*** Ситуация: пусть пользователь добавил трек в "Любимое", но в итоге автор трека решил удалить его с '
    f'музыкальной площадки, После этого пользователь вызвал функцию по удалению трека из любимых')

user1.add_track_to_favorites(track1)
user1.add_track_to_favorites(track2)

print('Выведем список треков, добавленных треков в любимое, первым пользователем:')
print(user1.list_favorite_tracks)

print('Теперь удалим трек 1 с площадки')
track1.del_track()

print('Выведем список треков после удаления трека 1:')
print(user1.list_favorite_tracks)

print('Вызовем функцию удаления трека из любимого и выведем новое содержимое любимых треков: ')
user1.del_track_from_favorites(track1)
print(user1.list_favorite_tracks)


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
        self.artist = updated_description

    def add_track_to_playlist(self, track_object, user_object):
        # проверка возможности добавления треков в плейлист для других пользователей
        if (self.author == user_object) or (self.flag_change_by_others):
            self.tracks.append(track_object)
        else:
            print('Вы не можете добавлять треки в этот плейлист, так как автор ограничил доступ')

    def __repr__(self):
        return str(self.tracks)


print()
print('***Ситуация: Пусть user1 создал плейлист без возможности редактирования треков')
playlist1 = Playlist('Легендарные треки', user1, 'Треки для хорошего дня', False)
playlist1.add_track_to_playlist(track4, user1)
playlist1.add_track_to_playlist(track3, user1)
user1.add_playlist_to_list_playlists(playlist1)
print(f'Плейлисты пользователя user1: {user1.list_playlists}')
print(
    f'Создадим второго юзера, который добавил нередактируемы плейлист первого пользователя:')
user2 = User('Karim', 'djhsjd123@gmail.com', '12345678')
user2.add_playlist_to_list_playlists(playlist1)
print('Пусть второй пользователь решил добавить трек2 в этот плейлист.')

print('Cообщение при попытке добавить трек пользователем 2 -->')
user2.list_playlists[0].add_track_to_playlist(track2, user2)
