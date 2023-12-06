def merge(a, b):
    i, j = 0, 0
    c = [0] * (len(a) + len(b))
    while i < len(a) or j < len(b):
        if (j == len(b)) or (i < len(a) and a[i] < b[j]):
            c[i + j] = a[i]
            i += 1
        else:
            c[i + j] = b[j]
            j += 1
    return c


def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    l = a[: n // 2]
    r = a[n // 2:]
    l = merge_sort(l)
    r = merge_sort(r)
    return merge(l, r)
