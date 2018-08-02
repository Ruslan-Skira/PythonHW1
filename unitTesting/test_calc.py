import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):

        self.assertEqual(calc.add(10,5), 15)

    def test_second(self):
        self.assertGreaterEqual(2, 2, "it is great")

if __name__ == '__main__':
    unittest.main()