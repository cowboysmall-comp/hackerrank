import unittest

from algorithms.implementation.cavity_map import cavity_map


class TestCavityMap(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(cavity_map(4, ['1112', '1912', '1892', '1234']), ['1112', '1X12', '18X2', '1234'])


if __name__ == '__main__':
    unittest.main()
