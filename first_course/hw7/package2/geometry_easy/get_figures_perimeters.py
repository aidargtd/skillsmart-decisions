"""
Пусть в данном суб-пакете будут реализован класс подсчета периметров различных фигур
"""
from hw7.package1.math_pro.trig_func_realization import CONST_PI


def ger_triangle_pr(a, b, c):
    """Подсчет периметра труегольника."""
    return a + b + c


def get_rectangle_pr(a, b):
    """Подсчет периметра прямоугольника."""
    return 2 * (a + b)


def get_square_pr(side):
    """Подсчет периметра квадрата."""
    return 4 * side


def get_circle_pr(radius):
    """Подсчет периметра круга (длины окружности)."""
    return 2 * CONST_PI * radius


def get_rhombus_pr(side):
    """Подсчет периметра ромба."""
    return 4 * side
