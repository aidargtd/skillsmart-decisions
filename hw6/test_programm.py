def add_digits(num):
    while len(str(num)) != 1:
        num = sum([int(i) for i in str(num)])
    return num


n = int(input('Введите число: '))
print(add_digits(n))