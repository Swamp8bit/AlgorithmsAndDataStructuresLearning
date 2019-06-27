from queue_linked_list import Queue
import unittest

class TestQueue(unittest.TestCase):
    #testing enqueue
    def test_queue_empty_list(self):
        q=Queue()
        self.assertIsNone(q.dequeue(), "It should be None")
    
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

