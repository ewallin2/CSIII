import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestMath(unittest.TestCase):
    def test_sqrt(self):
        inp = 144
        expected_result = 12
        self.assertEqual(get_sqrt(inp),expected_result)
        
        with self.assertRaises(TypeError):
            get_sqrt("a")

    def test_divide(self):
       inp1 = 4
       inp2 = 2
       expected_result = 2
       self.assertEqual(divide(inp1, inp2), 2)

       with self.assertRaises(ZeroDivisionError):
          divide(1,0)
          
if __name__ == '__main__':
  unittest.main()

