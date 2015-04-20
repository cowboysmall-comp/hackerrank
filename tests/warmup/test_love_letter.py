import unittest

from warmup.love_letter import palindrome


class TestLoveLetter(unittest.TestCase):

    def test_basic_cases(self):
        alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz']

        self.assertEqual(palindrome(alpha, 'abc'), 2)
        self.assertEqual(palindrome(alpha, 'abcba'), 0)
        self.assertEqual(palindrome(alpha, 'abcd'), 4)
        self.assertEqual(palindrome(alpha, 'cba'), 2)


if __name__ == '__main__':
    unittest.main()
