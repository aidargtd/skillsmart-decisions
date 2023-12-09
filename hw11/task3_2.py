num1, num2 = map(int, input('Введите два числа от 1 до 10: ').split())
while not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
    print('Вы ввели некорректные данные, попробуйте снова:')
    num1, num2 = map(int, input('Введите два числа от 1 до 1: ').split())
s = 0
for i in num1, num2:
    f = open('{}.txt'.format(i), 'rt')
    try:
        s += int(f.readline()) + int(f.readline()) + int(f.readline())
    except ValueError:
        print('В вашем файле есть ошибки')
    finally:
        f.close()
print(s)
