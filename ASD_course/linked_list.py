import unittest


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """task1.4"""
        node = self.head
        ans = []
        while node is not None:
            if node.value == val:
                ans.append(node.value)
            node = node.next
        return ans

    def delete(self, val, all=False):
        """task1.1&1.2"""
        node = self.head
        left = None
        while node is not None:
            if node.value == val:
                if left is None:
                    self.head = node.next
                else:
                    left.next = node.next
                    if node.next is None:
                        self.tail = left
                if not all:
                    break
            else:
                left = node
            node = node.next
        if self.head is None:
            self.tail = None

    def clean(self):
        """task1.3"""
        self.head = None
        self.tail = None

    def len(self):
        """task1.5"""
        node = self.head
        counter = 0
        while node is not None:
            counter += 1
            node = node.next
        return counter

    def insert(self, afterNode, newNode):
        """task1.6"""
        node = self.head
        if afterNode is None:
            if node is None:
                self.add_in_tail(newNode)
            else:
                newNode.next = node
                self.head = newNode
                self.head.next = newNode.next
        else:
            while node is not None:
                if node.value == afterNode:
                    if node.next is None:
                        self.tail = newNode
                    newNode.next = node.next
                    node.next = newNode
                    break
                node = node.next
            return None


def f(s1, s2):
    """task 1.8"""
    ans = []
    if s1.len() == s2.len():
        node1 = s1.head
        node2 = s2.head
        while node1 is not None and node2 is not None:
            ans.append(node1.value + node2.value)
            node1 = node1.next
            node2 = node2.next
    return ans


class Tests(unittest.TestCase):
    def test_del(self):
        s_list = LinkedList()
        # Удаление из пустого списка
        s_list.delete(10)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

        # удаление одного элемента
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.delete(1)
        self.assertEqual(s_list.head.value, 2)

        # удаление элементов с одинаковым значением
        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(4))
        s_list.delete(4, all=True)
        self.assertEqual(s_list.head.value, 2)
        self.assertIsNone(s_list.head.next)

        # Проверка при удалении последнего элемента
        s_list.delete(2)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_clean_list(self):
        s_list = LinkedList()
        # Очистка пустого списка
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

        # Поиск в пустом списке
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
