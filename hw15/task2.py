import random

arr = [random.randint(1, 10) for _ in range(100)]


def f(values, n):
    d = {}
    ans = []
    for i in values:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    for j in d.keys():
        if d[j] >= n:
            ans.append(j)
    return ans

