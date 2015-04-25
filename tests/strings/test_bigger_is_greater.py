import unittest

from strings.bigger_is_greater import greater_than


class TestBiggerIsGreater(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(greater_than('ab'), 'ba')
        self.assertEqual(greater_than('bb'), 'no answer')
        self.assertEqual(greater_than('hefg'), 'hegf')
        self.assertEqual(greater_than('dhck'), 'dhkc')
        self.assertEqual(greater_than('dkhc'), 'hcdk')


if __name__ == '__main__':
    unittest.main()
