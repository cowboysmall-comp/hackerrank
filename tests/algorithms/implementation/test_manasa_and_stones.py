import unittest

from algorithms.implementation.manasa_and_stones import last_stones


class TestManasaAndStones(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(last_stones(3, 1, 2), {2, 3, 4})
        self.assertEqual(last_stones(4, 10, 100), {30, 120, 210, 300})


if __name__ == '__main__':
    unittest.main()
