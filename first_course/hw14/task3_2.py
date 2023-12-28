import os
from PIL import Image, ImageDraw, ImageFont

"""
3.1. Напишите программу, которая получает на вход два типа (расширения) графических форматов, находит в текущем каталоге 
все графические файлы, соответствующие первому расширению, и конвертирует их в графический формат по второму расширению.

3.2. Дополните предыдущую функцию рисованием в центре изображения незаполненного квадрата, внутри которого будут 
написаны две строчки (вторая с новой строки):

Hello,
World!
"""

import os
from PIL import Image, ImageDraw


def f(old_format, new_format):
    for item in os.listdir():
        if item.endswith(old_format):
            with Image.open(item) as im:
                draw = ImageDraw.Draw(im)
                width, height = im.size
                square_size = 400
                square_left = (width - square_size) // 2
                square_top = (height - square_size) // 2
                draw.rectangle([square_left, square_top, square_left + square_size, square_top + square_size],
                               outline=(0, 0, 0), width=10)

                text = "Hello,\nWorld!"
                draw.multiline_text((square_left + 20, square_top + 20), text, fill='black',
                                    font=ImageFont.truetype("arial.ttf", 90))
                new_name = item.split('.')[0] + new_format
                im.save(new_name)
                del draw


# f(".png", ".jpg")
