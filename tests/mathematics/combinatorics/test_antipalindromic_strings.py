import unittest

from mathematics.combinatorics.antipalindromic_strings import antipalindromic


class TestAntipalindromicStrings(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(antipalindromic(2, 2), 2)
        self.assertEqual(antipalindromic(2, 3), 6)
        self.assertEqual(antipalindromic(5, 6), 1920)
        self.assertEqual(antipalindromic(6, 5), 1620)


if __name__ == '__main__':
    unittest.main()
