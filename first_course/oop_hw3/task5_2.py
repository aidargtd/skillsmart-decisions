"""
5.2. Постройте две небольшие и косвенно логически связанные иерархии классов в вашей программе
(например, Животное - Кот/Собака, и Переноска животных - Сумка для котика/Чемодан для собаки).
Не выдумывайте никакие абстрактные сущности, только запутаетесь. Возьмите простые физические вещи,
например, автомобиль и двигатель, тарелка и еда, кошелёк и деньги и т. п.
У родительского класса в каждой иерархии должно быть не менее двух наследников.
В каждом дочернем классе должно быть не менее двух оригинальных методов,
характеризующих уникальность
этих классов, их отличие от родительского.
"""


class Tea:
    """Родительский класс - чай"""

    def __init__(self, tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves):
        self.type_of_tea = tea_type
        self.origin = origin
        self.color_of_brew = color
        self.brewing_method = brew_method
        self.caffeine_content = percent_of_caffeine
        self.type_of_leaves = type_leaves


class BlackTea(Tea):
    """Дочерний класс для класса "чай", Черный чай"""

    def __init__(self, tea_type, origin, color, brew_method,
                 percent_of_caffeine, type_leaves, strength):
        super().__init__(tea_type, origin, color, brew_method,
                         percent_of_caffeine, type_leaves)
        self.strength = strength  # Уровень крепости чая(0/10)
        self.TIME_SEC_ZERO_STRENGTH_TEA = 0
        self.TIME_SEC_LOW_STRENGTH_TEA = 80
        self.TIME_SEC_MEDIUM_STRENGTH_TEA = 120
        self.TIME_SEC_HARD_STRENGTH_TEA = 180

    def determine_brew_time_in_seconds(self):
        """Метод для подсчета времени заваривания чая"""
        if self.strength == 0:
            return self.TIME_ZERO_STRENGTH_TEA_SEC
        elif 0 < self.strength < 4:
            return self.TIME_SEC_LOW_STRENGTH_TEA
        elif 3 < self.strength < 7:
            return self.TIME_SEC_MEDIUM_STRENGTH_TEA
        else:
            return self.TIME_SEC_HARD_STRENGTH_TEA

    def add_milk(self):
        if self.strength <= 7:
            return True
        else:
            return False


class Puer(Tea):
    """Дочерний класс для класса "чай", Зеленый чай"""

    def __init__(self, tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves, aging_years,
                 toppings=False):
        super().__init__(tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves)
        self.aging_years = aging_years  # Возраст пуэра в годах
        self.recommendation_toppings = toppings  # Запрашивает значение True or False
        self.TOPPING_GINGER = 1
        self.TOPPING_STRAWBERRY = 2
        self.TOPPING_HONEY = 3
        self.TOPPING_RASPBERRY = 4

    def calculate_cost_of_puer_dollars(self):
        """Метод для подсчета стоимости чая"""
        # Пример формулы для расчета рейтинга на основе возраста и процента содержания кофеина
        rating = ((self.aging_years * 0.1) + self.caffeine_content) / 15
        # Пусть рейтинг * 50$ = цена за 100 грамм чая
        return rating * 50

    def add_topping_for_drink(self, topping_num):
        "Если метод возвращает True, значит человек добавил топинг, иначе False"
        if topping_num == self.TOPPING_GINGER:
            return True
        elif topping_num == self.TOPPING_STRAWBERRY:
            return True
        elif topping_num == self.TOPPING_HONEY:
            return True
        elif topping_num == self.TOPPING_RASPBERRY:
            return True
        else:
            return False


class TeaAccessory:
    """Родительский класс - аксессуар для чая"""

    def __init__(self, name, material):
        self.name = name
        self.material = material


class Teapot(TeaAccessory):
    """Дочерний класс для класса "аксессуар для чая", Заварочный чайник"""

    def __init__(self, name, material, volume, tea_amount):
        super().__init__(name, material)
        self.volume = volume
        self.tea_amount = tea_amount

    def calculate_water_to_tea_ratio(self):
        """Рассчитываем соотношение воды к количеству чая"""
        water_to_tea = self.volume / self.tea_amount
        if 40 < water_to_tea < 60:
            return True
        else:
            return False

    def detect_bad_material(self):
        """Если вернулось значение True, значит материал плохой"""
        if self.material.lower() == 'пластик':
            return True
        else:
            return False


class Teacup(TeaAccessory):
    """Дочерний класс для класса "аксессуар для чая", Чашка"""

    def __init__(self, name, material, volume):
        super().__init__(name, material)
        self.volume = volume

    def detect_bad_material(self):
        """Если вернулось значение True, значит материал плохой"""
        if self.material.lower() == 'пластик':
            return True
        else:
            return False

    def detect_bad_volume(self):
        """Если вернулось значение True, значит объем хороший"""
        if 150 <= self.volume <= 400:
            return True
        else:
            return False
