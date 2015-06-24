import unittest

from algorithms.implementation.find_digits import count_digit_dividers


class TestFindDigits(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(count_digit_dividers(12), 2)
        self.assertEqual(count_digit_dividers(1012), 3)


if __name__ == '__main__':
    unittest.main()
