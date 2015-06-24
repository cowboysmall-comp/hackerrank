import unittest

from algorithms.strings.common_child import common_child


class TestCommonChild(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(common_child('HARRY', 'SALLY'), 2)
        self.assertEqual(common_child('AA', 'BB'), 0)
        self.assertEqual(common_child('SHINCHAN', 'NOHARAAA'), 3)
        self.assertEqual(common_child('ABCDEF', 'FBDAMN'), 2)


if __name__ == '__main__':
    unittest.main()
