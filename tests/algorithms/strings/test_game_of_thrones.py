import unittest

from algorithms.strings.game_of_thrones import palindrome_anagram


class TestGameOfThrones(unittest.TestCase):

    def test_basic_cases(self):
        self.assertTrue(palindrome_anagram('aaabbbb'))
        self.assertFalse(palindrome_anagram('cdefghmnopqrstuvw'))
        self.assertTrue(palindrome_anagram('cdcdcdcdeeeef'))


if __name__ == '__main__':
    unittest.main()
