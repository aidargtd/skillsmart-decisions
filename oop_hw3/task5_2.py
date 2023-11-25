"""
5.2. Постройте две небольшие и косвенно логически связанные иерархии классов в вашей программе
(например, Животное - Кот/Собака, и Переноска животных - Сумка для котика/Чемодан для собаки).
Не выдумывайте никакие абстрактные сущности, только запутаетесь. Возьмите простые физические вещи,
например, автомобиль и двигатель, тарелка и еда, кошелёк и деньги и т. п..
У родительского класса в каждой иерархии должно быть не менее двух наследников.
В каждом дочернем классе должно быть не менее двух оригинальных методов, характеризующих уникальность
этих классов, их отличие от родительского.
"""


# Родительский класс - чай
class Tea:
    def __init__(self, tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves):
        self.type_of_tea = tea_type
        self.origin = origin
        self.color_of_brew = color
        self.brewing_method = brew_method
        self.caffeine_content = percent_of_caffeine
        self.type_of_leaves = type_leaves


# Дочерний класс для класса "чай", Черный чай
class BlackTea(Tea):
    def __init__(self, tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves, strength):
        super().__init__(tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves)
        self.strength = strength  # Уровень крепости чая(0/10)

    def determine_brew_time(self):
        if self.strength == 0:
            return 'Можете не заваривать'
        elif 0 < self.strength < 4:
            return 'Заваривайте чай 1 минуту 20 сек'
        elif 3 < self.strength < 7:
            return 'Заваривайте чай 2 минуты'
        else:
            return 'Заваривайте чай 3 минуты'

    def add_milk(self):
        if self.strength <= 7:
            return 'Можете добавить немного молока по желанию, ' \
                   'только добавьте к времени заварки 10-20 секунд в зависимости от крпкости'
        else:
            return 'При добавлении молока ваша желаемая терпкость не сохранится, так что не стоит его добавлять'


# Дочерний класс для класса "чай", Зеленый чай
class Puer(Tea):
    def __init__(self, tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves, aging_years,
                 toppings=False):
        super().__init__(tea_type, origin, color, brew_method, percent_of_caffeine, type_leaves)
        self.aging_years = aging_years  # Возраст пуэра в годах
        self.recommendation_toppings = toppings  # Запрашивает значение True or False

    def calculate_cost_of_puer(self):
        # Пример формулы для расчета рейтинга на основе возраста и типа листьев
        rating = self.aging_years * 0.8 + (len(self.type_of_leaves) - 5) * 0.2
        # Пусть рейтинг * 50$ = цена за 100 грамм чая
        return f"Цена чая: {rating * 50}$ за сто грамм"

    def show_recommendations_for_drink(self):
        if self.recommendation_toppings == True:
            return 'Пуэр очень хорошо сочетается с ягодами(малина, клубника, шиповник), а также мятой и имбирем.'
        else:
            return 'Приятного чаепития!'


# Родительский класс - аксессуар для чая
class TeaAccessory:
    def __init__(self, name, material):
        self.name = name
        self.material = material


# Дочерний класс для класса "аксессуар для чая", Заварочный чайник
class Teapot(TeaAccessory):
    def __init__(self, name, material, volume, tea_amount):
        super().__init__(name, material)
        self.volume = volume
        self.tea_amount = tea_amount

    def calculate_water_to_tea_ratio(self):
        # Рассчитываем соотношение воды к количеству чая
        water_to_tea = self.volume / self.tea_amount
        if 40 < water_to_tea < 60:
            return 'Все в норме!'
        else:
            return 'Надо поменять соотношения'

    def detect_bad_material(self):
        if self.material.lower() == 'пластик':
            return 'Пластик при нагревании выделяет плохие вещества, поменяйте заварочный чайник!!!'
        else:
            return 'Все в норме!'


# Дочерний класс для класса "аксессуар для чая", Чашка
class Teacup(TeaAccessory):
    def __init__(self, name, material, volume):
        super().__init__(name, material)
        self.volume = volume

    def detect_bad_material(self):
        if self.material.lower() == 'пластик':
            return 'Пластик при нагревании выделяет плохие вещества, поменяйте заварочный чайник!!!'
        else:
            return 'Все в норме!'

    def detect_bad_volume(self):
        if 150 <= self.volume <= 400:
            return 'Все в норме!'
        else:
            return 'Ваша кружка не подходит для идеального наслаждения чаем'
