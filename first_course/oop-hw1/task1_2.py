'''
Сделайте три простых класса из любой (одной) компьютерной темы, которая вам интересна, и которые логически связаны
друг с другом. В каждом классе должно быть не менее трёх (лучше 5-7) полей.
'''


# Простой класс для создания объекта пользователя музыкального сервиса Spotify
class User:
    name = 'default_name'
    email = 'default_email'
    password = 'default_password'
    list_favorite_tracks = []
    list_playlists = []


# Создадим простой класс для создания объекта трека музыкального сервиса Spotify
class Track:
    title = 'default_title'
    artist = 'default_artist'
    album = 'default_album'
    genre = 'default_genre'
    duration = 'default_duration'


# Создадим простой класс для создания объекта трека музыкального сервиса Spotify
class PLaylist:
    title = 'default_title'
    tracks = []
    author = 'default_author'
    description = 'default_description'
