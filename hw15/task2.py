import random

arr = [random.randint(1, 10) for _ in range(100)]


def f(values, n):
    d = {}
    ans = set()
    for i in values:
        if d.get(i):
            d[i] += 1
            if d[i] == n:
                ans.add(i)
        else:
            d[i] = 1
            if d[i] == n:
                ans.add(i)
    return ans


print(f(arr, 10))
