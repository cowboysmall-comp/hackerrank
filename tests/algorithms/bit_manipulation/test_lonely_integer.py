import unittest

from algorithms.bit_manipulation.lonely_integer import lonely_integer


class TestLonelyInteger(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(lonely_integer([1]), 1)
        self.assertEqual(lonely_integer([1, 1, 2]), 2)
        self.assertEqual(lonely_integer([0, 0, 1, 2, 1]), 2)
        self.assertEqual(lonely_integer([4, 9, 95, 93, 57, 4, 57, 93, 9]), 95)


if __name__ == '__main__':
    unittest.main()
