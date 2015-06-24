import unittest

from algorithms.dynamic_programming.square_subsequences import square_subsequences


class TestSquareSubsequences(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(square_subsequences('aaa'), 3)
        self.assertEqual(square_subsequences('abab'), 3)
        self.assertEqual(square_subsequences('baaba'), 6)


if __name__ == '__main__':
    unittest.main()
