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
            elif d[i] > n and (i in ans):
                ans.remove(i)
        else:
            d[i] = 1
    return ans


print(f(arr, 10))
