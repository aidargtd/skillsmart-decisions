fi = open('cats.txt', 'rt', encoding='utf-8')


class Cat:
    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound

    def __repr__(self):
        return f'{self.name} : вес {self.weight} кг : частота {self.sound} Гц'


a = []
for s in fi:
    data = s.split()
    a.append(Cat(data[0], float(data[1]), int(data[2])))
fi.close()
print(a)
