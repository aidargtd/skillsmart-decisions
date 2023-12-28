import unittest
from my_sort import merge_sort
import random


class SortTests(unittest.TestCase):

    def setUp(self):
        print(f'Начало теста, {str(self).split()[0]}')

    def tearDown(self):
        print(f'Конец теста!, {str(self).split()[0]}')

    def test_random_list(self):
        random_list = [random.randint(-10000, 10000) for _ in range(random.randint(0, 80))]
        self.assertListEqual(merge_sort(random_list), sorted(random_list))

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_large_values(self):
        input_list = list(range(10 ** 5, 0, -1))
        out_list = list(range(1, 10 ** 5 + 1))
        self.assertListEqual(merge_sort(input_list), out_list)

    def test_word_list(self):
        self.assertListEqual(merge_sort(['Шарпы', 'Питон', 'Плюсы']), ['Питон', 'Плюсы', 'Шарпы'])


if __name__ == '__main__':
    unittest.main()
