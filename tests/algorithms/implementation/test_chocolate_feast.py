import unittest

from algorithms.implementation.chocolate_feast import chocolate_feast


class TestChocolateFeast(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(chocolate_feast(10, 2, 5), 6)
        self.assertEqual(chocolate_feast(12, 4, 4), 3)
        self.assertEqual(chocolate_feast(6, 2, 2), 5)


if __name__ == '__main__':
    unittest.main()
