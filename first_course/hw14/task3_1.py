"""
3.1. Напишите программу, которая получает на вход два типа (расширения) графических форматов, находит в текущем каталоге
все графические файлы, соответствующие первому расширению, и конвертирует их в графический формат по второму расширению.
"""
import os
from PIL import Image


def f(old_format, new_format):
    for item in os.listdir():
        if item.endswith(old_format):
            im = Image.open(item)
            im.save(item.split('.')[0] + new_format)


# print(f(".png", ".jpg"))
