import unittest

from strings.substring_diff import maximum_length


class TestSubstringDiff(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(maximum_length('tabriz', 'torino', 2), 4)
        self.assertEqual(maximum_length('abacba', 'abcaba', 0), 3)
        self.assertEqual(maximum_length('helloworld', 'yellomarin', 3), 8)


if __name__ == '__main__':
    unittest.main()
