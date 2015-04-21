import unittest

from warmup.identify_smith_numbers import prime_factors, sum_digits


class TestIdentifySmithNumbers(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(prime_factors(378), [2, 3, 3, 3, 7])
        self.assertEqual(prime_factors(4937775), [3, 5, 5, 65837])

        self.assertEqual(sum_digits(378), 18)
        self.assertEqual(sum_digits(4937775), 42)


if __name__ == '__main__':
    unittest.main()
