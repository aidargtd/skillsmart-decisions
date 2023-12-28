import os


def del_catalog(path):
    if not os.path.exists(path):
        return 'Указанный каталог не существует'

    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            return 'В вашем каталоге присутствуют подкаталоги'

    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            os.remove(os.path.join(path, i))

    os.rmdir(path)
    return 'Каталог был удален'


