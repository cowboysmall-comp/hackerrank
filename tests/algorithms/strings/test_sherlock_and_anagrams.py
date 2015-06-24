import unittest

from algorithms.strings.sherlock_and_anagrams import anagramic_pairs


class TestSherlockAndAnagrams(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(anagramic_pairs('abba'), 4)
        self.assertEqual(anagramic_pairs('abcd'), 0)


if __name__ == '__main__':
    unittest.main()
