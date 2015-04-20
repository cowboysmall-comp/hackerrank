import unittest

from warmup.cut_sticks import cut_sticks


class TestCutSticks(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(cut_sticks([5, 4, 4, 2, 2, 8]), [6, 4, 2, 1])
        self.assertEqual(cut_sticks([1, 2, 3, 4, 3, 3, 2, 1]), [8, 6, 4, 1])


if __name__ == '__main__':
    unittest.main()
