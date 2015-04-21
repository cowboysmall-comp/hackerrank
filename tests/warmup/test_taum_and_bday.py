import unittest

from warmup.taum_and_bday import minimum_spend


class TestTaumAndBday(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(minimum_spend(10, 10, 1, 1, 1), 20)
        self.assertEqual(minimum_spend(5, 9, 2, 3, 4), 37)
        self.assertEqual(minimum_spend(3, 6, 9, 1, 1), 12)
        self.assertEqual(minimum_spend(7, 7, 4, 2, 1), 35)
        self.assertEqual(minimum_spend(3, 3, 1, 9, 2), 12)


if __name__ == '__main__':
    unittest.main()
