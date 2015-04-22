import unittest

from strings.pangrams import is_pangram


class TestPangrams(unittest.TestCase):

    def test_basic_cases(self):
        self.assertTrue(is_pangram('We promptly judged antique ivory buckles for the next prize'))
        self.assertFalse(is_pangram('We promptly judged antique ivory buckles for the prize'))


if __name__ == '__main__':
    unittest.main()
