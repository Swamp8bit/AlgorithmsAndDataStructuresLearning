from queue_linked_list import Queue
import unittest

class TestQueue(unittest.TestCase):
    #testing enqueue
    def test_queue_empty_list(self):
        q=Queue()
        self.assertIsNone(q.dequeue(), "It should be None")
        self.assertEqual(q.size(),0)
    
    def test_dequeue_default(self):
        q=Queue()
        self.assertEqual(q.size(),0, "the size is 0")
        q.enqueue(123)
        self.assertEqual(q.size(),1, "the size is 1")
        q.enqueue(1000)
        q.enqueue(-123)
        self.assertEqual(q.size(),3, "the size is 3")
        self.assertEqual(q.dequeue(), 123, "dequeue 123" )
        self.assertEqual(q.dequeue(), 1000, "dequeue 1000" )
        self.assertEqual(q.dequeue(), -123, "dequeue -123" )
        self.assertEqual(q.size(),0, "the size is 0")

    def test_lot_of_enqueue(self):
        q=Queue()
        length=1000
        for i in range(0,length):
            q.enqueue(i)
        self.assertEqual(q.size(),length,f"The size is {length}")


    def test_lof_of_dequeue(self):
        q=Queue()
        length=1000
        for i in range(0,length):
            q.enqueue(i)

        self.assertEqual(q.size(),length,f"The size is {length}")
        for i in range(0,length):
            check=q.dequeue()
            self.assertEqual(check, i, f"dequeue is {i}")
            check_size=length-i-1
            self.assertEqual(check_size, q.size(), f"size is {check_size}")


