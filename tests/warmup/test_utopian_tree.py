import unittest

from warmup.utopian_tree import grow


class TestUtopianTree(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(grow(0), 1)
        self.assertEqual(grow(1), 2)
        self.assertEqual(grow(4), 7)


if __name__ == '__main__':
    unittest.main()
