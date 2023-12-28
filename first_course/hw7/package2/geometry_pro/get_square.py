"""
Пусть в данном суб-пакете будут реализован класс подсчета площадей с помощью тригонометрии у некоторых фигур
"""
from hw7.package1.math_pro import trig_func_realization


def ger_triangle_pr(a, b, angle):
    """Подсчет периметра труегольника."""
    return 1 / 2 * a * b * trig_func_realization.sin_degrees(angle)


def get_rhombus_pr(side, angle):
    """Подсчет периметра ромба."""
    return (side ** 2) * trig_func_realization.sin_degrees(angle)


def get_parallelogram_square(a, b, angle):
    """Подсчет периметра параллелограмма."""
    return a * b * trig_func_realization.sin_degrees(angle)
