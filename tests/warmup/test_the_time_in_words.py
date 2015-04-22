import unittest

from warmup.the_time_in_words import time_in_words


class TestTheTimeInWords(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(time_in_words(5, 0), 'five o\' clock')
        self.assertEqual(time_in_words(5, 1), 'one minute past five')
        self.assertEqual(time_in_words(5, 10), 'ten minutes past five')
        self.assertEqual(time_in_words(5, 15), 'quarter past five')
        self.assertEqual(time_in_words(5, 30), 'half past five')
        self.assertEqual(time_in_words(5, 40), 'twenty minutes to six')
        self.assertEqual(time_in_words(5, 45), 'quarter to six')
        self.assertEqual(time_in_words(5, 47), 'thirteen minutes to six')
        self.assertEqual(time_in_words(17, 28), 'twenty eight minutes past five')


if __name__ == '__main__':
    unittest.main()
