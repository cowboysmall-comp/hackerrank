import unittest

from strings.alternating_characters import deletions


class TestAlternatingCharacters(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(deletions('AAAA'), 3)
        self.assertEqual(deletions('BBBBB'), 4)
        self.assertEqual(deletions('ABABABAB'), 0)
        self.assertEqual(deletions('BABABA'), 0)
        self.assertEqual(deletions('AAABBB'), 4)


if __name__ == '__main__':
    unittest.main()
