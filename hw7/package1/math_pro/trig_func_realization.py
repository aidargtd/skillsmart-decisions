from hw7.package1.math_easy.simple_functions import factorial
import math

CONST_PI = math.pi


def sin_degrees(x, accuracy=20):
    """Подсчет синуса угла x (в градусах) с использованием ряда Маклорена."""
    x = x % 360
    if x == 90:
        return 1
    elif x == 270:
        return -1
    x = math.radians(x)
    sin_x = 0
    for i in range(accuracy):
        sign = (-1) ** i
        sin_x += sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return sin_x


def cos_degrees(x, accuracy=20):
    """Подсчет косинуса угла x (в градусах) с использованием ряда Маклорена."""
    if x % 360 == 90 or x % 360 == 270:  # Корректировка для углов близких к 90 и 270 градусам
        return 0

    x = math.radians(x)  # Преобразование в радианы
    cos_x = 0
    for i in range(accuracy):
        sign = (-1) ** i
        cos_x += sign * (x ** (2 * i)) / factorial(2 * i)
    return cos_x
