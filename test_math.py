import unittest
import math as m



class TestCast(unittest.TestCase):

    def log_fun(self):
        print(m.factorial(16))
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()