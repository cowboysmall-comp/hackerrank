import unittest

from strings.two_strings import substring


class TestTwoStrings(unittest.TestCase):

    def test_basic_cases(self):
        self.assertTrue(substring('hello', 'world'))
        self.assertFalse(substring('hi', 'world'))


if __name__ == '__main__':
    unittest.main()
