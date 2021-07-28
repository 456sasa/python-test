import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_functioan.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name("first","last")
        self.assertEqual(formatted_name,"first lastzz")
    

if __name__ == '__main__':
    unittest.main()