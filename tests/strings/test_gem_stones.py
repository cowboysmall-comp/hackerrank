import unittest

from strings.gem_stones import gem_stones


class TestGemStones(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(len(gem_stones(['abcdde', 'baccd', 'eeabg'])), 2)


if __name__ == '__main__':
    unittest.main()
