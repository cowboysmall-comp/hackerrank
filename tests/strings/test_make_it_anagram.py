import unittest

from strings.make_it_anagram import deletions


class TestGemStones(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(deletions('cde', 'abc'), 4)


if __name__ == '__main__':
    unittest.main()
