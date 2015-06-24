import unittest

from algorithms.strings.anagram import changes


class TestAnagram(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(changes('aaabbb'), 3)
        self.assertEqual(changes('ab'), 1)
        self.assertEqual(changes('abc'), -1)
        self.assertEqual(changes('mnop'), 2)
        self.assertEqual(changes('xyyx'), 0)
        self.assertEqual(changes('xaxbbbxx'), 1)


if __name__ == '__main__':
    unittest.main()
