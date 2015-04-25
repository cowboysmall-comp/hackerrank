import unittest

from strings.palindrome_index import deletion_index


class TestPalindromeIndex(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(deletion_index('aaab'), 3)
        self.assertEqual(deletion_index('baa'), 0)
        self.assertEqual(deletion_index('aaa'), -1)
        self.assertEqual(deletion_index('xyyxy'), 4)


if __name__ == '__main__':
    unittest.main()
