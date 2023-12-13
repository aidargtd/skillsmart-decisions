"""
4.1. Напишите функцию с тремя параметрами (путь к каталогу, расширение файла и булев флажок), которая возвращает список из двух списков имён:
список всех файлов с заданным расширением в заданном каталоге (включая файлы из его подкаталогов одного уровня вложенности, если флажок = True),
и список всех подкаталогов в заданном каталоге (включая подкаталоги одного уровня вложенности, если флажок = True).
"""
import os


def f(path, file_ext, flag):
    ans = []
    list1 = []
    list2 = []
    if not os.path.exists(path):
        return 'Указанный каталог не существует'
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            return 'В вашем каталоге присутствуют подкаталоги'


import os


def list_files_and_directories(path, file_ext, flag):
    list1 = []
    list2 = []

    if not os.path.exists(path):
        return 'Указанный каталог не существует', []

    for i in os.listdir(path):
        full_path = os.path.join(path, i)
        if os.path.isfile(full_path) and i.endswith(file_ext):
            list1.append(i)
        elif os.path.isdir(full_path):
            list2.append(i)
            if flag:
                # Просмотр элементов в подкаталогах
                for j in os.listdir(full_path):
                    flag_path = os.path.join(full_path, j)
                    if os.path.isfile(flag_path) and j.endswith(file_ext):
                        list1.append(j)
                    elif os.path.isdir(flag_path):
                        list2.append(j)

    return [list1, list2]
