import unittest

from warmup.max_min import minimum_unfairness


class TestMaxMin(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(minimum_unfairness([10, 100, 300, 200, 1000, 20, 30], 3), 20)
        self.assertEqual(minimum_unfairness([1, 2, 3, 4, 10, 20, 30, 40, 100, 200], 4), 3)
        self.assertEqual(minimum_unfairness([10, 20, 30, 100, 101, 102], 3), 2)


if __name__ == '__main__':
    unittest.main()
