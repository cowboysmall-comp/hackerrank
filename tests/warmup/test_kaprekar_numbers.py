import unittest

from warmup.kaprekar_numbers import count_digits, split_digits, kaprekar_numbers


class TestLonelyInteger(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(count_digits(45), 2)
        self.assertEqual(count_digits(50), 2)
        self.assertEqual(count_digits(45 ** 2), 4)

        self.assertEqual(split_digits(45), [4, 5])
        self.assertEqual(split_digits(45 ** 2, 10 ** 2), [20, 25])

        self.assertEqual(kaprekar_numbers(1, 100), [1, 9, 45, 55, 99])
        self.assertEqual(kaprekar_numbers(200, 300), [297])
        self.assertEqual(kaprekar_numbers(200, 296), [])


if __name__ == '__main__':
    unittest.main()
