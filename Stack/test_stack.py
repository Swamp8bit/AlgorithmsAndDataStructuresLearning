from stack_linked_list import Stack
import unittest
class TestStack(unittest.TestCase):
    def test_stack_peek(self):
        pass

    def test_push(self):
        pass
    
    def test_pop_one_element(self):
        stack=Stack()
        stack.push(1)
        stack.pop()
        self.assertEqual(stack.end, None)
        self.assertEqual(stack.start, None)
        self.assertEqual(stack.size(),0)
    
    def test_pop_two_element(self):
        stack=Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(),2,"We should pop 2")
        self.assertEqual(stack.peek(),1)
        self.assertEqual(stack.size(),1)
        self.assertEqual(stack.pop(),1,"We should pop 1")
        self.assertEqual(stack.size(),0)
        
        