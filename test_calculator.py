import unittest
from calculator import add, sub

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,1),0)
    def test_sub(self):
        self.assertEqual(sub(5,2),3)

if __name__ == '__main__':
    unittest.main()
