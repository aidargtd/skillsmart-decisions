"""
Напишите функцию, которая получает на вход два параметра: имя файла архива и расширение файла, сканирует текущий
каталог в поисках файлов с подходящим расширением, и добавляет их в архив (исходно этот архив не существует).
"""
import os
from zipfile import ZipFile


def f(archive_name, file_ext):
    with ZipFile(f'{archive_name}.zip', 'w') as zipfile:
        for file in os.listdir(os.getcwd()):
            if file.endswith(file_ext):
                zipfile.write(os.path.join(os.getcwd(), file))
