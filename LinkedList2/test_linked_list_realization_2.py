import unittest
from linked_list_realization_2 import LinkedList2, Node
class TestLinkedList2(unittest.TestCase):
    def test_find_empty(self):
        test_list=LinkedList2()
        test_list.find(3)
        self.assertIsNone(test_list.find(3), "List is empty it should be None")

    def test_find_one(self):
        test_list=LinkedList2()
        n1=Node(2)
        test_list.add_in_tail(n1)
        self.assertEqual(test_list.find(2), n1, "n1 should be equal to finding")

    def test_find_one_in_the_middle(self):
        pass
    
    def test_find_one_in_the_end(self):
        pass

