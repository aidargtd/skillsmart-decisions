import random
from itertools import product

words = [''.join(j) for j in product('abcde', repeat=4)]

d = {}
arr_with_keys = set()
while len(arr_with_keys) != 100:
    arr_with_keys.add(random.randint(0, 1000))

for i in arr_with_keys:
    d[i] = random.choice(words)

for i in sorted(arr_with_keys):
    print('Ключ {}, значение {}'.format(i, d.pop(i)))

print('Итоговое значение словаря после удаления всех элементов: {}'.format(d))
