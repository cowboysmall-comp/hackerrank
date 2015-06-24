import unittest

from algorithms.implementation.sherlock_and_squares import count_squares


class TestSherlockAndSquares(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(count_squares(3, 9), 2)
        self.assertEqual(count_squares(4, 9), 2)
        self.assertEqual(count_squares(17, 24), 0)
        self.assertEqual(count_squares(1, 24), 4)
        self.assertEqual(count_squares(1, 25), 5)
        self.assertEqual(count_squares(1, 26), 5)
        self.assertEqual(count_squares(63, 82), 2)
        self.assertEqual(count_squares(64, 81), 2)
        self.assertEqual(count_squares(65, 80), 0)
        self.assertEqual(count_squares(80, 82), 1)
        self.assertEqual(count_squares(81, 81), 1)
        self.assertEqual(count_squares(1, 100), 10)


if __name__ == '__main__':
    unittest.main()
