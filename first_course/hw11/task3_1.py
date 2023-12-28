import random

for i in range(1, 11):
    f = open('{}.txt'.format(i), 'wt')
    for _ in range(3):
        f.write(str(random.randint(-100, 100)) + '\n')
