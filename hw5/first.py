# """
# Add Digits from leetcode
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#
#
#
# Example 1:
#
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
# """
#
#
# def add_digits(num):
#     while len(str(num)) != 1:
#         num = sum([int(i) for i in str(num)])
#     return num
#
#
# n = int(input('Введите число: '))
# print(add_digits(n))
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Вторая проверка вывода сообщения на русском языке')
