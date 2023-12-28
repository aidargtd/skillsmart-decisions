# 4.3. Придумайте наглядный пример, который демонстрирует, как работает ad hoc полиморфизм.
import math

"""
Пусть функция poo будет высчитывать стоимость чая за 100 грамм
# Пример формулы для расчета рейтинга пуэра на основе возраста и процента содержания кофеина, она зависит от двух параметров
        rating = ((self.aging_years * 0.1) + self.caffeine_content) / 70
        # Пусть рейтинг * 5$ = цена за 100 грамм чая
        return f"Цена чая: {rating * 20}$ за сто грамм"
# Пример формулы для расчета рейтинга черного чая на основе возраста, процента содержания кофеина и страны происхождения, она зависит от трех параметров
        # Пусть рейтинг * 2$ = цена за 100 грамм чая, где rating от 1 до 10
        rating=(( country*caffeine*log2(1+age))/3000)*10

# Пример формулы для расчета рейтинга зеленого чая процента содержания кофеина, она зависит от одного параметра
        Но мы не сделали такой метод в коассе, поэтому будем вызывать ошибку
"""


class Tea:
    def __init__(self, type_tea):
        self.type_of_tea = type_tea

    def foo(self, *data):
        if len(data) == 2:
            aging_years = data[0]
            caffeine_percent = data[1]
            # Определние стоимости пуэра
            rating = ((aging_years * 0.1) + caffeine_percent) / 70
            return f"Цена чая: {int(rating * 5)}$ за сто грамм"
        elif len(data) == 3:
            age = data[0]
            caffeine_percent = data[1]
            origin = data[2]
            tea_producers = {"Китай": 5, "Индия": 5, "Шри-Ланка": 4, "Кения": 4, "Тайвань": 3, "Япония": 4, "Турция": 3,
                             "Индонезия": 2, "Вьетнам": 2}
            export_country = tea_producers.get(origin, 1)
            rating = ((export_country * caffeine_percent * math.log2(1 + age)) / 3000) * 10
            return f"Цена чая: {int(rating * 2)}$ за сто грамм"

        else:
            raise ValueError('Для такого набора данных метод foo не определен, стоимость не может быть посчитана:(')


# Определим снизу три дочерних класса
class BlackTea(Tea):
    def __init__(self, type_tea):
        super().__init__(type_tea)


class Puer(Tea):
    def __init__(self, type_tea):
        super().__init__(type_tea)


# Пусть в классе GreenTea не реализовали метод foo
class GreenTea(Tea):
    def __init__(self, type_tea):
        super().__init__(type_tea)


# Создадим экземпляры классов для каждого вида чая
black_tea = BlackTea("Чай черный")
puer_tea = Puer("Пуэр")
green_tea = GreenTea("Чай зеленый")

# Расчитаем стоимости различных видов чая за сто грамм
print(black_tea.foo(2019, 34, 'Индия'))
print(puer_tea.foo(1999, 51))
print(green_tea.foo(48))

# Для одного параметра метод foo не определен, следовательно, вызовется ошибка
