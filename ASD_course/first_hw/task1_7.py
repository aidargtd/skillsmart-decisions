import unittest
from ASD_course.first_hw.all_tasks_wo_7 import Node, LinkedList


class Tests(unittest.TestCase):
    def test_del(self):
        s_list = LinkedList()

        s_list.delete(10)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.delete(1)
        self.assertEqual(s_list.head.value, 2)

        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(4))
        s_list.delete(4, all=True)
        self.assertEqual(s_list.head.value, 2)
        self.assertIsNone(s_list.head.next)

        s_list.delete(2)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_clean_list(self):
        s_list = LinkedList()

        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_find_all(self):
        s_list = LinkedList()

        self.assertEqual(len(s_list.find_all(1)), 0)

        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(0))
        s_list.add_in_tail(Node(0))
        self.assertEqual(len(s_list.find_all(0)), 2)

    def test_len(self):
        s_list = LinkedList()
        self.assertEqual(s_list.len(), 0)
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(3))
        self.assertEqual(s_list.len(), 3)

    def test_insert(self):
        s_list = LinkedList()
        s_list.insert(None, Node(1))
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 1)

        s_list.insert(1, Node(2))
        self.assertEqual(s_list.head.next.value, 2)
        self.assertEqual(s_list.tail.value, 2)


if __name__ == '__main__':
    unittest.main()
