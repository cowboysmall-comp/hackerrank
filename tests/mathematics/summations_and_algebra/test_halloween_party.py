import unittest

from mathematics.summations_and_algebra.halloween_party import optimal_slices


class TestHalloweenParty(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(optimal_slices(5), 6)
        self.assertEqual(optimal_slices(6), 9)
        self.assertEqual(optimal_slices(7), 12)
        self.assertEqual(optimal_slices(8), 16)


if __name__ == '__main__':
    unittest.main()
