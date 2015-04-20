import unittest

from warmup.lonely_integer import lonely_integer


class TestLoveLetter(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(lonely_integer([1]), 1)
        self.assertEqual(lonely_integer([1, 1, 2]), 2)
        self.assertEqual(lonely_integer([0, 0, 1, 2, 1]), 2)


if __name__ == '__main__':
    unittest.main()
