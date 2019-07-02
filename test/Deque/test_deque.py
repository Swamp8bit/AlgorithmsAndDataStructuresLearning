from src.Deque.deque_stacks import DequeStacks
from src.Deque.deque_scratch import Deque
import unittest

class TestDeque(unittest.TestCase):
    #testing endeque
    def setUp(self):
        self.deques={}
        test_deque1=Deque()
        test_deque2=DequeStacks()        
        self.deques["DequeDefault"]=test_deque1
        self.deques["DequeStacks"]=test_deque2
        

    def test_deque_empty_list(self):           
        for q_name,q in self.deques.items():
            with self.subTest(q_name):
                self.assertIsNone(q.removeFront(), f"In deque {q_name} Remove from Front, it should return None")
                self.assertIsNone(q.removeTail(), f"In deque {q_name} Remove fromt Tail nothing, it should return None")
                self.assertIsNone(q.getFront(), f"In deque {q_name} Front should be None")
                self.assertIsNone(q.getTail(), f"In deque {q_name} Tail should be None")
                self.assertEqual(q.size(),0, f"In  deque {q_name} the size is 0")
    
    def test_deque_default_add(self):
        for q_name,q in self.deques.items():
            with self.subTest(q_name):                
                self.assertEqual(q.size(),0, f"In  deque {q_name} the size is 0")
                v1=7432
                v2=4123
                q.addFront(v1)
                self.assertEqual(q.size(),1, f"In  deque {q_name} the size is 1")
                self.assertEqual(q.getFront(),v1, f"In  deque {q_name} the size is 7432")
                self.assertEqual(q.getTail(),v1, f"In  deque {q_name} the tail is 7432")
                q.addTail(v2)
                self.assertEqual(q.size(),2, f"In  deque {q_name} the size is 2")
                self.assertEqual(q.getFront(),v1, f"In  deque {q_name} the size is {v1}")
                self.assertEqual(q.getTail(),v2, f"In  deque {q_name} the tail is {v2}")
                # q.removeFront(1000)
                # q.endeque(-123)
                # self.assertEqual(q.size(),3, f"In  deque {q_name} the size is 3")
                # self.assertEqual(q.dedeque(), 123, f"In  deque {q_name} dedeque 123" )
                # self.assertEqual(q.dedeque(), 1000, f"In  deque {q_name} dedeque 1000" )
                # self.assertEqual(q.dedeque(), -123, f"In  deque {q_name} dedeque -123" )
                # self.assertEqual(q.size(),0, f"In  deque {q_name} the size is 0")

    # def test_endeque_lot(self):
    #     for q_name,q in self.deques.items():
    #         with self.subTest(q_name):
    #             length=1000
    #             q.endeque(1)
    #             q.dedeque()
    #             q.dedeque()
    #             self.assertEqual(q.size(),0,f"In  deque {q_name} The size is 0")
    #             q.endeque(1)
    #             self.assertEqual(q.size(),1,f"In  deque {q_name} The size is 1")
    #             for i in range(1,length):
    #                 q.endeque(i)
    #                 self.assertEqual(q.size(),i+1, f"In  deque {q_name} The size is {i+1}")
    #             self.assertEqual(q.size(),length, f"In  deque {q_name} The size is {length}")


    # def test_lof_of_dedeque(self):
    #     for q_name,q in self.deques.items():
    #         with self.subTest(q_name):
    #             length=1000
    #             for i in range(0,length):
    #                 q.endeque(i)

    #             self.assertEqual(q.size(),length, f"In  deque {q_name} The size is {length}")
    #             for i in range(0,length):
    #                 check=q.dedeque()
    #                 self.assertEqual(check, i, f"In  deque {q_name} dedeque is {i}")
    #                 check_size=length-i-1
    #                 self.assertEqual(check_size, q.size(), f"In  deque {q_name} size is {check_size}")

    # def test_lof_of_dedeque_with_additional_checks(self):
    #     for q_name,q in self.deques.items():
    #         with self.subTest(q_name):
    #             length=1000
    #             q.endeque(1)
    #             q.dedeque()
    #             q.dedeque()
    #             self.assertEqual(q.size(),0, f"In  deque {q_name} The size is 0")

    #             for i in range(0,length):
                        
    #                 q.endeque(i)
    #                 self.assertEqual(q.size(),i+1, f"In  deque {q_name} The size is {i+1}")
        

    #             self.assertEqual(q.size(),length,f"In  deque {q_name} The size is {length}")
    #             for i in range(0,length):
    #                 check=q.dedeque()
    #                 self.assertEqual(check, i, f"In  deque {q_name} dedeque is {i}")
    #                 check_size=length-i-1
    #                 self.assertEqual(check_size, q.size(), f"In  deque {q_name} size is {check_size}")


