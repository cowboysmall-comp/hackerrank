import unittest

from strings.funny_string import is_funny_string


class TestFunnyString(unittest.TestCase):

    def test_basic_cases(self):
        self.assertTrue(is_funny_string('acxz'))
        self.assertFalse(is_funny_string('bcxz'))
        self.assertFalse(is_funny_string('ivvkxq'))
        self.assertFalse(is_funny_string('ivvkx'))


if __name__ == '__main__':
    unittest.main()
