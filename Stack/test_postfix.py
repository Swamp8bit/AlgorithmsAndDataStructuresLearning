from postfix import calculate_postfix
import unittest
class TestPostfix(unittest.TestCase):
    def test_expression(self):
        self.assertEquals(calculate_postfix("8 2 + 5 * 9 +="), 59)
    def test_expression_default(self):        
        self.assertEquals(calculate_postfix("1 2 + 3 *"), 9)