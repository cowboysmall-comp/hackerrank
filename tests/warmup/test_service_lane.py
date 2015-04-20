import unittest

from warmup.service_lane import service_lane


class TestServiceLane(unittest.TestCase):

    def test_basic_cases(self):
        W = [2, 3, 1, 2, 3, 2, 3, 3]
        P = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]

        self.assertEqual(service_lane(W, P), [1, 2, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
