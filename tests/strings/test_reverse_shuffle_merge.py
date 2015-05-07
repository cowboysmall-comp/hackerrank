import unittest

from strings.reverse_shuffle_merge import find


class TestReverseShuffleMerge(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(find('eggegg'), 'egg')


if __name__ == '__main__':
    unittest.main()
