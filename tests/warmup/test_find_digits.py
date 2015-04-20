import unittest

from warmup.find_digits import count_digits


class TestFindDigits(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(count_digits(12), 2)
        self.assertEqual(count_digits(1012), 3)


if __name__ == '__main__':
    unittest.main()
