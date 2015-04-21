import unittest

from warmup.sherlock_and_gcd import gcd, gcd_multiple


class TestSherlockAndGCD(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(gcd(2, 3), 1)
        self.assertEqual(gcd(2, 4), 2)

        self.assertEqual(gcd_multiple([2, 3, 5, 7]), 1)
        self.assertEqual(gcd_multiple([3, 6, 9]), 3)


if __name__ == '__main__':
    unittest.main()
