'''
Напишите наглядный пример на основе задания 2, который демонстрирует побочный эффект от передачи объектов по ссылке.
'''


class User:
    name = 'default_name'
    email = 'default_email'
    password = 'default_password'
    list_favorite_tracks = []
    list_playlists = []


class Track:
    title = 'default_title'
    artist = 'default_artist'
    album = 'default_album'
    genre = 'default_genre'
    duration = 'default_duration'

    def __repr__(self):
        return f"{self.title} - {self.artist}"


class PLaylist:
    title = 'default_title'
    tracks = []
    author = 'default_author'
    description = 'default_description'


user1 = User()  # Создал первого пользователя
user1.name = 'Aidar'
user1.email = 'test123@gmail.com'
user1.password = 'spotify1234'

user2 = User()  # Создал второго пользователя
user2.name = 'Karim'
user2.email = 'test321@yandex.ru'
user2.password = 'spotify4321'

# Теперь создадим несколько объектов треков, которые впоследствии добавим в новый плейлист
track1 = Track()  # создал первый трек
track1.title = 'Малинки'
track1.artist = 'Группа Кино'
track1.album = 'Ненависть'
track1.genre = 'hard metal'
track1.duration = '3:30'

track2 = Track()  # создал второй 2 трек
track2.title = 'Space'
track2.artist = 'The Neighbourhood'
track2.album = 'road'
track2.genre = 'rap'
track2.duration = '2:31'

track3 = Track()  # создал второй 3 трек
track3.title = 'С новым годом!'
track3.artist = 'lana del ray'
track3.album = None
track3.genre = 'soft-rock'
track3.duration = '2:11'

'''
Ситуация: 
Предположим, что пользователь создал новый плейлист, в который он добавил два трека: track1 и track2.
Второму пользователю очень понравился плейлист user1, поэтому он добавил его к себе.
Вскоре user2 захотел добавить еще один трект в  плейлист user1.
Произойдут ли изменения в это плейлисте у user1?
'''

playlist1 = PLaylist()
playlist1.title = 'default_title'
playlist1.tracks.append(track1)  # добавление треков в плейлист
playlist1.tracks.append(track2)
playlist1.author = user1
playlist1.description = 'best playlist ever'
user1.list_playlists.append(playlist1)  # user1 добавил в свой аккаунт новый плелист

# user2 добавляет плейлист user1 к себе
user2.list_playlists.append(playlist1)
# user2 добавляет трек track3 в плейлист, который он "берет" от user1
user2.list_playlists[0].tracks.append(track3)

# Выводим содержимое плейлиста для user1 и user2
print(f"Содержимое плейлиста user1: {user1.list_playlists[0].tracks}")
print(f"Содержимое плейлиста user2: {user2.list_playlists[0].tracks}")

# user1, и user2 имеют один и тот же список треков в плейлистах.
# Это происходит, тк оба пользователя ссылаются на один и тот же объект playlist1
